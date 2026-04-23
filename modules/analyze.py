import json
import re
import os

filepath = r"C:\code\copy_skill_extends\modules\Linux curl\commands.json"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
line6 = lines[5]

print(f"Line 6 length: {len(line6)}")
print(f"Last 30 chars: {repr(line6[-30:])}")

# Count braces
opens = line6.count('{')
closes = line6.count('}')
print(f"Opens: {opens}, Closes: {closes}")

# The issue might be that extension params properties are not comma-separated
# Let me look for the pattern in the extension's params
# Find where extension's params object starts
ext_params_start = line6.find('"params": {"参数"')
print(f"Extension params section starts at character containing '参数' (display garbled)")

# Let me try a different approach - rebuild the JSON from scratch
# by understanding the structure

# The command object structure:
cmd = {
    "dirPath": "/Linux curl/",
    "name": "curl 发送请求",
    "keyword": "curl 请求",
    "description": "发送 HTTP 请求",
    "data": {
        "cmd": "curl -X %{方法}% %{URL}%",
        "extensions": [{
            "name": "带数据",
            "cmd": "curl -X POST -d '%{数据}%' %{URL}%",
            "params": {
                "方法": {"type": "string", "required": True, "description": "方法", "example": "POST", "notes": "必填"},
                "数据": {"type": "string", "required": True, "description": "数据", "example": "{\"name\":\"test\"}", "notes": "必填"},
                "URL": {"type": "string", "required": True, "description": "URL", "example": "https://api.example.com", "notes": "必填"}
            },
            "keyword": "curl post"
        }],
        "params": {
            "方法": {"type": "string", "required": True, "description": "HTTP 方法", "example": "GET", "notes": "必填"},
            "URL": {"type": "string", "required": True, "description": "目标 URL", "example": "https://api.example.com/data", "notes": "必填"}
        }
    }
}

# Try to write this back and verify
data = {
    "module": "Linux curl",
    "version": "2.0",
    "description": "Curl HTTP 客户端工具",
    "commands": [cmd]
}

try:
    output = json.dumps(data, ensure_ascii=False, indent=2)
    print("\nGenerated JSON valid!")
    print(output[:200])
except Exception as e:
    print(f"\nError generating JSON: {e}")

# Let's also try to parse the original and see where it fails
print("\n\nTrying to parse original with error recovery...")
# Try to find the issue by looking at the raw structure
# Maybe there's a missing comma between extension's param properties

# Look for the pattern: "notes": "必填"}{ pattern
pattern = r'"notes":\s*"[^"]*"\}\s*\{'
matches = list(re.finditer(pattern, line6))
print(f"Found {len(matches)} problematic patterns")

for m in matches:
    start = max(0, m.start() - 30)
    end = min(len(line6), m.end() + 30)
    print(f"Pattern at {m.start()}: {repr(line6[start:end])}")