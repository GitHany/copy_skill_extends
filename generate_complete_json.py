# -*- coding: utf-8 -*-
"""
重新生成完整的 commands.json，包含所有命令类别
"""

import json
import re
from pathlib import Path

def parse_markdown_table(text):
    """解析 Markdown 表格"""
    lines = text.strip().split('\n')
    if len(lines) < 3:
        return []
    
    results = []
    for line in lines[2:]:  # 跳过表头和分隔行
        cells = [c.strip() for c in line.split('|')[1:-1]]
        if len(cells) >= 2:
            results.append({
                'scenario': cells[0],
                'cmd': cells[1]
            })
    
    return results

def clean_command_name(name):
    """清理命令名称，移除数字、连字符等"""
    # 移除 1-01、1.01 等数字前缀
    name = re.sub(r'^[\d\-\.]+\s*', '', name)
    # 移除多余的空格
    name = re.sub(r'\s+', ' ', name).strip()
    return name

def extract_command_examples(md_content, category):
    """从 markdown 内容中提取命令示例"""
    commands = []
    
    sections = re.split(r'\n### ', md_content)
    
    for section in sections[1:]:
        lines = section.split('\n')
        if not lines:
            continue
        
        header_match = re.match(r'(.+?) - (.+)', lines[0])
        if not header_match:
            continue
        
        keyword = header_match.group(1).strip()
        description = header_match.group(2).strip()
        
        # 清理描述
        description = clean_command_name(description)
        
        # 提取基础命令
        base_cmd = ""
        for i, line in enumerate(lines[1:10]):
            line = line.strip()
            if line.startswith('`') and ('git ' in line or 'docker ' in line or 'cd ' in line or 'ls ' in line):
                base_cmd = line.strip('`')
                break
            elif line.startswith('```bash'):
                if i+1 < len(lines):
                    next_line = lines[i+2].strip() if i+2 < len(lines) else ''
                    if next_line and not next_line.startswith('```'):
                        base_cmd = next_line
                        break
        
        if not base_cmd:
            for line in lines[1:]:
                line = line.strip()
                if line.startswith('`') and not line.startswith('``'):
                    base_cmd = line.strip('`')
                    break
        
        # 提取扩展示例
        extensions = []
        table_start = -1
        for i, line in enumerate(lines):
            if '扩展示例' in line:
                table_start = i
                break
        
        if table_start >= 0:
            table_lines = '\n'.join(lines[table_start:])
            examples = parse_markdown_table(table_lines)
            
            for ex in examples:
                cmd = ex['cmd']
                if cmd and cmd.startswith('`'):
                    cmd = cmd.strip('`')
                
                if cmd and ('git ' in cmd or 'docker ' in cmd or 'cd ' in cmd or 'ls ' in cmd):
                    # 清理扩展名称
                    scenario = clean_command_name(ex['scenario'])
                    extensions.append({
                        "name": scenario,
                        "cmd": cmd,
                        "params": {},
                        "keyword": f"{keyword} {scenario}"
                    })
        
        # 提取参数
        params = {}
        param_pattern = r'%\{([^}]+)\}%'
        all_text = '\n'.join(lines)
        for match in re.finditer(param_pattern, all_text):
            param_name = match.group(1)
            if param_name not in params:
                params[param_name] = {
                    "type": "string",
                    "required": True,
                    "description": f"{param_name}参数",
                    "example": "",
                    "notes": ""
                }
        
        if base_cmd:
            commands.append({
                "dirPath": f"/{category}/",
                "name": f"{keyword} {description}",
                "keyword": keyword,
                "description": description,
                "data": {
                    "cmd": base_cmd,
                    "extensions": extensions,
                    "params": params
                }
            })
    
    return commands

def get_claude_skills_commands():
    """获取 Claude Skills 相关命令"""
    commands = [
        # Oh-My-Claude
        {
            "dirPath": "/Claude Skills/oh-my-claude/",
            "name": "安装 oh-my-claude",
            "keyword": "/plugin marketplace add",
            "description": "安装 oh-my-claude 插件",
            "data": {
                "cmd": "/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode",
                "extensions": [
                    {
                        "name": "安装插件",
                        "cmd": "/plugin install oh-my-claudecode",
                        "params": {},
                        "keyword": "/plugin install oh-my-claudecode"
                    },
                    {
                        "name": "初始化配置",
                        "cmd": "/omc-setup",
                        "params": {},
                        "keyword": "/omc-setup"
                    },
                    {
                        "name": "更新插件",
                        "cmd": "/plugin update oh-my-claudecode",
                        "params": {},
                        "keyword": "/plugin update"
                    },
                    {
                        "name": "查看插件列表",
                        "cmd": "/plugin list",
                        "params": {},
                        "keyword": "/plugin list"
                    },
                    {
                        "name": "卸载插件",
                        "cmd": "/plugin uninstall oh-my-claudecode",
                        "params": {},
                        "keyword": "/plugin uninstall"
                    }
                ],
                "params": {}
            }
        },
        {
            "dirPath": "/Claude Skills/oh-my-claude/",
            "name": "autopilot 自动执行任务",
            "keyword": "/oh-my-claudecode:autopilot",
            "description": "AI 自动执行完整任务流程",
            "data": {
                "cmd": "/oh-my-claudecode:autopilot %{任务描述}%",
                "extensions": [
                    {
                        "name": "详细日志模式",
                        "cmd": "/oh-my-claudecode:autopilot %{任务}% --verbose",
                        "params": {},
                        "keyword": "--verbose 详细日志"
                    },
                    {
                        "name": "交互确认模式",
                        "cmd": "/oh-my-claudecode:autopilot %{任务}% --interactive",
                        "params": {},
                        "keyword": "--interactive 交互确认"
                    },
                    {
                        "name": "查看历史",
                        "cmd": "/oh-my-claudecode:autopilot --history",
                        "params": {},
                        "keyword": "--history 查看历史"
                    },
                    {
                        "name": "实现完整功能",
                        "cmd": "/oh-my-claudecode:autopilot \"实现完整的用户认证模块\"",
                        "params": {},
                        "keyword": "autopilot 实现完整功能"
                    },
                    {
                        "name": "修复 Bug",
                        "cmd": "/oh-my-claudecode:autopilot \"修复登录页面性能问题\"",
                        "params": {},
                        "keyword": "autopilot 修复 Bug"
                    },
                    {
                        "name": "开发 API",
                        "cmd": "/oh-my-claudecode:autopilot \"开发 RESTful API\"",
                        "params": {},
                        "keyword": "autopilot API 开发"
                    }
                ],
                "params": {
                    "任务描述": {
                        "type": "string",
                        "required": True,
                        "description": "要执行的任务描述",
                        "example": "实现用户登录功能",
                        "notes": "越详细 AI 理解越准确"
                    },
                    "任务": {
                        "type": "string",
                        "required": True,
                        "description": "任务参数",
                        "example": "",
                        "notes": ""
                    }
                }
            }
        },
        {
            "dirPath": "/Claude Skills/oh-my-claude/",
            "name": "deep-interview 深度访谈",
            "keyword": "/oh-my-claudecode:deep-interview",
            "description": "系统化提问以明确需求",
            "data": {
                "cmd": "/oh-my-claudecode:deep-interview %{问题领域}%",
                "extensions": [
                    {
                        "name": "技术选型咨询",
                        "cmd": "/oh-my-claudecode:deep-interview \"技术栈选型\"",
                        "params": {},
                        "keyword": "deep-interview 技术选型"
                    },
                    {
                        "name": "需求澄清",
                        "cmd": "/oh-my-claudecode:deep-interview \"功能需求澄清\"",
                        "params": {},
                        "keyword": "deep-interview 需求澄清"
                    },
                    {
                        "name": "架构设计讨论",
                        "cmd": "/oh-my-claudecode:deep-interview \"系统架构设计\"",
                        "params": {},
                        "keyword": "deep-interview 架构设计"
                    },
                    {
                        "name": "Bug 复现分析",
                        "cmd": "/oh-my-claudecode:deep-interview \"Bug 复现与根因分析\"",
                        "params": {},
                        "keyword": "deep-interview Bug 分析"
                    }
                ],
                "params": {
                    "问题领域": {
                        "type": "string",
                        "required": True,
                        "description": "需要讨论的问题领域",
                        "example": "项目优化方向",
                        "notes": "AI 会通过系统性提问明确需求"
                    }
                }
            }
        },
        {
            "dirPath": "/Claude Skills/oh-my-claude/",
            "name": "ralph 代码审查",
            "keyword": "/ralph",
            "description": "AI 代码审查助手",
            "data": {
                "cmd": "/ralph %{审查内容}%",
                "extensions": [
                    {
                        "name": "审查代码质量",
                        "cmd": "/ralph \"审查 src/utils/helpers.ts 的代码质量\"",
                        "params": {},
                        "keyword": "ralph 代码质量"
                    },
                    {
                        "name": "安全漏洞检查",
                        "cmd": "/ralph \"检查登录模块的安全漏洞\"",
                        "params": {},
                        "keyword": "ralph 安全检查"
                    },
                    {
                        "name": "性能问题诊断",
                        "cmd": "/ralph \"诊断 API 性能瓶颈\"",
                        "params": {},
                        "keyword": "ralph 性能诊断"
                    }
                ],
                "params": {
                    "审查内容": {
                        "type": "string",
                        "required": True,
                        "description": "需要审查的内容",
                        "example": "用户认证模块",
                        "notes": ""
                    }
                }
            }
        },
        {
            "dirPath": "/Claude Skills/ultrawork/",
            "name": "ultrawork 最大并行",
            "keyword": "/ultrawork",
            "description": "多 agent 最大并行执行模式",
            "data": {
                "cmd": "/ultrawork %{任务描述}%",
                "extensions": [
                    {
                        "name": "快速修复 Bug",
                        "cmd": "/ultrawork \"修复项目中所有的 TypeScript 类型错误\"",
                        "params": {},
                        "keyword": "ultrawork 修复 Bug"
                    },
                    {
                        "name": "批量重构",
                        "cmd": "/ultrawork \"重构 src/components 目录下所有组件\"",
                        "params": {},
                        "keyword": "ultrawork 重构"
                    },
                    {
                        "name": "并行测试",
                        "cmd": "/ultrawork \"为所有 API 端点编写集成测试\"",
                        "params": {},
                        "keyword": "ultrawork 测试"
                    },
                    {
                        "name": "安全扫描",
                        "cmd": "/ultrawork \"对整个项目进行安全扫描\"",
                        "params": {},
                        "keyword": "ultrawork 安全扫描"
                    },
                    {
                        "name": "性能优化",
                        "cmd": "/ultrawork \"优化数据库查询和缓存策略\"",
                        "params": {},
                        "keyword": "ultrawork 性能优化"
                    },
                    {
                        "name": "文档生成",
                        "cmd": "/ultrawork \"生成项目 API 文档\"",
                        "params": {},
                        "keyword": "ultrawork 文档生成"
                    }
                ],
                "params": {
                    "任务描述": {
                        "type": "string",
                        "required": True,
                        "description": "并行执行的任务描述",
                        "example": "重构并测试所有模块",
                        "notes": "任务会被分解并最大并行执行"
                    }
                }
            }
        },
        {
            "dirPath": "/Claude Skills/ultrawork/",
            "name": "ulw 快速最大并行",
            "keyword": "/ulw",
            "description": "ultrawork 快捷命令",
            "data": {
                "cmd": "/ulw %{任务}%",
                "extensions": [
                    {
                        "name": "批量代码审查",
                        "cmd": "/ulw \"审查所有新增代码\"",
                        "params": {},
                        "keyword": "ulw 代码审查"
                    },
                    {
                        "name": "批量依赖更新",
                        "cmd": "/ulw \"更新所有过时的依赖包\"",
                        "params": {},
                        "keyword": "ulw 更新依赖"
                    },
                    {
                        "name": "批量测试",
                        "cmd": "/ulw \"运行完整的测试套件\"",
                        "params": {},
                        "keyword": "ulw 批量测试"
                    }
                ],
                "params": {
                    "任务": {
                        "type": "string",
                        "required": True,
                        "description": "要执行的任务",
                        "example": "重构",
                        "notes": "/ulw 是 /ultrawork 的快捷方式"
                    }
                }
            }
        },
        {
            "dirPath": "/Claude Skills/ccg/",
            "name": "ccg Codex Gemini 合成审查",
            "keyword": "/ccg",
            "description": "多模型协作的综合审查",
            "data": {
                "cmd": "/ccg %{审查类型}%",
                "extensions": [
                    {
                        "name": "架构审查",
                        "cmd": "/ccg \"架构审查：分析微服务设计\"",
                        "params": {},
                        "keyword": "ccg 架构审查"
                    },
                    {
                        "name": "性能审查",
                        "cmd": "/ccg \"性能审查：分析查询优化\"",
                        "params": {},
                        "keyword": "ccg 性能审查"
                    },
                    {
                        "name": "安全审查",
                        "cmd": "/ccg \"安全审查：检查认证授权\"",
                        "params": {},
                        "keyword": "ccg 安全审查"
                    },
                    {
                        "name": "UI 一致性审查",
                        "cmd": "/ccg \"UI 审查：检查组件一致性\"",
                        "params": {},
                        "keyword": "ccg UI 审查"
                    }
                ],
                "params": {
                    "审查类型": {
                        "type": "string",
                        "required": True,
                        "description": "审查类型",
                        "example": "代码审查",
                        "notes": "ccg 会调用多个模型进行综合分析"
                    }
                }
            }
        },
        {
            "dirPath": "/Claude Skills/providers/",
            "name": "ask claude Claude 顾问",
            "keyword": "/ask claude",
            "description": "使用 Claude 模型解答技术问题",
            "data": {
                "cmd": "/ask claude %{问题}%",
                "extensions": [
                    {
                        "name": "代码重构建议",
                        "cmd": "/ask claude \"如何重构这个复杂的函数\"",
                        "params": {},
                        "keyword": "ask claude 重构"
                    },
                    {
                        "name": "性能分析",
                        "cmd": "/ask claude \"如何优化这个数据库查询\"",
                        "params": {},
                        "keyword": "ask claude 性能"
                    },
                    {
                        "name": "安全审计",
                        "cmd": "/ask claude \"这段代码有什么安全风险\"",
                        "params": {},
                        "keyword": "ask claude 安全"
                    },
                    {
                        "name": "代码审查",
                        "cmd": "/ask claude \"帮我审查这段代码\"",
                        "params": {},
                        "keyword": "ask claude 审查"
                    }
                ],
                "params": {
                    "问题": {
                        "type": "string",
                        "required": True,
                        "description": "技术问题",
                        "example": "如何实现热更新",
                        "notes": ""
                    }
                }
            }
        },
        {
            "dirPath": "/Claude Skills/providers/",
            "name": "autoresearch 自动研究",
            "keyword": "/autoresearch",
            "description": "自动研究技术问题和最佳实践",
            "data": {
                "cmd": "/autoresearch %{研究主题}%",
                "extensions": [
                    {
                        "name": "技术选型研究",
                        "cmd": "/autoresearch \"React vs Vue 技术选型\"",
                        "params": {},
                        "keyword": "autoresearch 技术选型"
                    },
                    {
                        "name": "架构探索",
                        "cmd": "/autoresearch \"微服务架构最佳实践\"",
                        "params": {},
                        "keyword": "autoresearch 架构"
                    },
                    {
                        "name": "算法研究",
                        "cmd": "/autoresearch \"排序算法性能对比\"",
                        "params": {},
                        "keyword": "autoresearch 算法"
                    },
                    {
                        "name": "测试策略",
                        "cmd": "/autoresearch \"前端测试策略\"",
                        "params": {},
                        "keyword": "autoresearch 测试"
                    }
                ],
                "params": {
                    "研究主题": {
                        "type": "string",
                        "required": True,
                        "description": "研究主题",
                        "example": "缓存策略",
                        "notes": "会自动搜索和分析相关信息"
                    }
                }
            }
        },
        {
            "dirPath": "/Claude Skills/oh-my-claude/",
            "name": "omc-doctor 诊断检查",
            "keyword": "/omc-doctor",
            "description": "检查 Claude Code 配置和状态",
            "data": {
                "cmd": "/omc-doctor",
                "extensions": [
                    {
                        "name": "检查配置",
                        "cmd": "/omc-doctor --config",
                        "params": {},
                        "keyword": "omc-doctor 配置"
                    },
                    {
                        "name": "检查插件",
                        "cmd": "/omc-doctor --plugins",
                        "params": {},
                        "keyword": "omc-doctor 插件"
                    },
                    {
                        "name": "检查网络",
                        "cmd": "/omc-doctor --network",
                        "params": {},
                        "keyword": "omc-doctor 网络"
                    },
                    {
                        "name": "重置配置",
                        "cmd": "/omc-doctor --reset",
                        "params": {},
                        "keyword": "omc-doctor 重置"
                    }
                ],
                "params": {}
            }
        },
        {
            "dirPath": "/Claude Skills/oh-my-claude/",
            "name": "omc-hud 平视显示",
            "keyword": "/omc-hud",
            "description": "显示任务执行状态的平视显示器",
            "data": {
                "cmd": "/omc-hud",
                "extensions": [
                    {
                        "name": "显示详细信息",
                        "cmd": "/omc-hud --detailed",
                        "params": {},
                        "keyword": "omc-hud 详细"
                    },
                    {
                        "name": "最小化显示",
                        "cmd": "/omc-hud --minimal",
                        "params": {},
                        "keyword": "omc-hud 最小化"
                    },
                    {
                        "name": "关闭 HUD",
                        "cmd": "/omc-hud --off",
                        "params": {},
                        "keyword": "omc-hud 关闭"
                    },
                    {
                        "name": "刷新显示",
                        "cmd": "/omc-hud --refresh",
                        "params": {},
                        "keyword": "omc-hud 刷新"
                    }
                ],
                "params": {}
            }
        },
        {
            "dirPath": "/Claude Skills/oh-my-claude/",
            "name": "omc-wait 等待任务",
            "keyword": "/omc-wait",
            "description": "等待后台任务完成",
            "data": {
                "cmd": "/omc-wait %{任务ID}%",
                "extensions": [
                    {
                        "name": "等待所有任务",
                        "cmd": "/omc-wait --all",
                        "params": {},
                        "keyword": "omc-wait 全部"
                    },
                    {
                        "name": "查看状态",
                        "cmd": "/omc-wait --status",
                        "params": {},
                        "keyword": "omc-wait 状态"
                    },
                    {
                        "name": "等待恢复",
                        "cmd": "/omc-wait --resume",
                        "params": {},
                        "keyword": "omc-wait 恢复"
                    }
                ],
                "params": {
                    "任务ID": {
                        "type": "string",
                        "required": True,
                        "description": "任务 ID",
                        "example": "task-123",
                        "notes": ""
                    }
                }
            }
        },
        {
            "dirPath": "/Claude Skills/oh-my-claude/",
            "name": "team 多 Agent 协作",
            "keyword": "/team",
            "description": "多 Agent 团队协作模式",
            "data": {
                "cmd": "/team %{任务描述}%",
                "extensions": [
                    {
                        "name": "前端开发团队",
                        "cmd": "/team \"组建前端开发团队\"",
                        "params": {},
                        "keyword": "team 前端团队"
                    },
                    {
                        "name": "全栈开发团队",
                        "cmd": "/team \"组建全栈开发团队\"",
                        "params": {},
                        "keyword": "team 全栈团队"
                    },
                    {
                        "name": "审查团队",
                        "cmd": "/team \"组建代码审查团队\"",
                        "params": {},
                        "keyword": "team 审查团队"
                    }
                ],
                "params": {
                    "任务描述": {
                        "type": "string",
                        "required": True,
                        "description": "团队任务描述",
                        "example": "开发用户系统",
                        "notes": "会自动分配 Agent 角色"
                    }
                }
            }
        },
        {
            "dirPath": "/Claude Skills/superpowers/",
            "name": "superpowers TDD 开发",
            "keyword": "/superpowers",
            "description": "测试驱动开发工作流",
            "data": {
                "cmd": "/superpowers %{功能描述}%",
                "extensions": [
                    {
                        "name": "TDD 红色阶段",
                        "cmd": "/superpowers \"编写失败的测试\"",
                        "params": {},
                        "keyword": "superpowers 红色"
                    },
                    {
                        "name": "TDD 绿色阶段",
                        "cmd": "/superpowers \"编写使测试通过的代码\"",
                        "params": {},
                        "keyword": "superpowers 绿色"
                    },
                    {
                        "name": "TDD 重构阶段",
                        "cmd": "/superpowers \"重构代码\"",
                        "params": {},
                        "keyword": "superpowers 重构"
                    },
                    {
                        "name": "完整 TDD 流程",
                        "cmd": "/superpowers \"实现用户登录功能（完整 TDD）\"",
                        "params": {},
                        "keyword": "superpowers 完整流程"
                    }
                ],
                "params": {
                    "功能描述": {
                        "type": "string",
                        "required": True,
                        "description": "要实现的功能",
                        "example": "购物车功能",
                        "notes": "会按照 TDD 流程执行"
                    }
                }
            }
        },
        {
            "dirPath": "/Claude Skills/ecc/",
            "name": "ecc ECC 工作流",
            "keyword": "/ecc",
            "description": "Everything Claude Code 工作流",
            "data": {
                "cmd": "/ecc %{任务}%",
                "extensions": [
                    {
                        "name": "ECC 计划",
                        "cmd": "/ecc plan \"项目计划\"",
                        "params": {},
                        "keyword": "ecc plan"
                    },
                    {
                        "name": "ECC 开发",
                        "cmd": "/ecc develop \"功能开发\"",
                        "params": {},
                        "keyword": "ecc develop"
                    },
                    {
                        "name": "ECC 审查",
                        "cmd": "/ecc review \"代码审查\"",
                        "params": {},
                        "keyword": "ecc review"
                    },
                    {
                        "name": "ECC 构建",
                        "cmd": "/ecc build \"项目构建\"",
                        "params": {},
                        "keyword": "ecc build"
                    }
                ],
                "params": {
                    "任务": {
                        "type": "string",
                        "required": True,
                        "description": "任务类型",
                        "example": "开发",
                        "notes": ""
                    }
                }
            }
        },
        {
            "dirPath": "/Claude Skills/openspec/",
            "name": "openspec 规范管理",
            "keyword": "/openspec",
            "description": "OpenSpec 规范变更管理",
            "data": {
                "cmd": "/openspec %{操作}%",
                "extensions": [
                    {
                        "name": "初始化规范库",
                        "cmd": "/openspec init",
                        "params": {},
                        "keyword": "openspec init"
                    },
                    {
                        "name": "提议新规范",
                        "cmd": "/openspec propose \"新功能规范\"",
                        "params": {},
                        "keyword": "openspec propose"
                    },
                    {
                        "name": "应用规范变更",
                        "cmd": "/openspec apply",
                        "params": {},
                        "keyword": "openspec apply"
                    },
                    {
                        "name": "归档规范",
                        "cmd": "/openspec archive",
                        "params": {},
                        "keyword": "openspec archive"
                    },
                    {
                        "name": "浏览现有规范",
                        "cmd": "/openspec explore",
                        "params": {},
                        "keyword": "openspec explore"
                    }
                ],
                "params": {
                    "操作": {
                        "type": "string",
                        "required": True,
                        "description": "操作类型",
                        "example": "propose",
                        "notes": ""
                    }
                }
            }
        }
    ]
    
    return commands

def main():
    docs_dir = Path("docs")
    
    all_commands = []
    
    # Claude Skills 命令（放在最前面）
    claude_commands = get_claude_skills_commands()
    all_commands.extend(claude_commands)
    print(f"Claude Skills 命令: {len(claude_commands)}")
    
    # Git commands
    git_md = (docs_dir / "git-commands" / "README.md").read_text(encoding='utf-8')
    git_commands = extract_command_examples(git_md, "Git 命令")
    all_commands.extend(git_commands)
    print(f"Git 命令: {len(git_commands)}")
    
    # Docker commands
    docker_md = (docs_dir / "docker-commands" / "README.md").read_text(encoding='utf-8')
    docker_commands = extract_command_examples(docker_md, "Docker 命令")
    all_commands.extend(docker_commands)
    print(f"Docker 命令: {len(docker_commands)}")
    
    # Linux commands
    linux_md = (docs_dir / "linux-commands" / "README.md").read_text(encoding='utf-8')
    linux_commands = extract_command_examples(linux_md, "Linux 命令")
    all_commands.extend(linux_commands)
    print(f"Linux 命令: {len(linux_commands)}")
    
    # 保存为 JSON
    output = {"data": all_commands}
    output_path = docs_dir / "public" / "commands.json"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"\n总命令数: {len(all_commands)}")
    print(f"输出文件: {output_path}")
    
    # 显示按目录分组的统计
    print("\n按目录分组:")
    categories = {}
    for cmd in all_commands:
        cat = cmd['dirPath'].strip('/')
        categories[cat] = categories.get(cat, 0) + 1
    
    for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat}: {count} 个")

if __name__ == "__main__":
    main()
