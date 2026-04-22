# 移动开发命令文档

移动端跨平台开发完整参考文档，包含 React Native、Flutter、跨平台框架（Ionic、Capacitor、Cordova、Tauri）以及移动端工具（Android SDK、Xcode）命令。

## 目录

- [React Native](#react-native)
- [Flutter](#flutter)
- [Android SDK](#android-sdk)
- [Xcode 工具](#xcode-工具)
- [Ionic 跨平台](#ionic-跨平台)
- [Capacitor](#capacitor)
- [Cordova](#cordova)
- [Tauri](#tauri)
- [实用场景](#实用场景)
- [命令速查表](#命令速查表)

---

## React Native

### npx create-react-native-app 创建项目

**基础用法**:
```bash
npx create-react-native-app %{项目名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建 TypeScript 项目 | `npx create-react-native-app %{项目名称}% --template react-native-template-typescript` | TS 支持 【常用】 |
| 指定版本创建 | `npx create-react-native-app %{项目名称}% --version 0.70.0` | 指定版本 |
| 查看帮助 | `npx create-react-native-app --help` | 查看所有选项 |

### npx react-native init 初始化项目

**基础用法**:
```bash
npx react-native@latest init %{项目名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 初始化最新项目 | `npx react-native@latest init %{项目名称}%` | 使用最新版本 【常用】 |
| 指定版本初始化 | `npx react-native@0.72.0 init %{项目名称}%` | 指定 RN 版本 |
| 跳过安装依赖 | `npx react-native init %{项目名称}% --skip-install` | 仅生成项目结构 |
| TypeScript 项目 | `npx react-native init %{项目名称}% --template react-native-template-typescript` | TS 模板 |

### npx react-native run-android 运行 Android 应用

**基础用法**:
```bash
npx react-native run-android
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定设备运行 | `npx react-native run-android --deviceId %{设备ID}%` | 指定模拟器/真机 【常用】 |
| 开启调试 | `npx react-native run-android --variant=debug` | Debug 模式 |
| 发布模式 | `npx react-native run-android --variant=release` | Release 模式 |
| 清缓存重新构建 | `npx react-native run-android --reset-cache` | 清除 Metro 缓存 |
| 仅构建 APK | `cd android && ./gradlew assembleRelease` | 生成 APK |

### npx react-native run-ios 运行 iOS 应用

**基础用法**:
```bash
npx react-native run-ios
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 指定模拟器 | `npx react-native run-ios --simulator="%{模拟器名}%"` | 指定模拟器 【常用】 |
| 指定设备 | `npx react-native run-ios --device="%{设备名}%"` | 真机调试 |
| 指定 Bundle ID | `npx react-native run-ios --variant=Release --configuration=Release` | 发布配置 |
| 列出可用设备 | `xcrun simctl list devices available` | 查看模拟器列表 |

### react-native bundle 打包 JS Bundle

**基础用法**:
```bash
npx react-native bundle --platform ios --entry-file index.js --bundle-output ios/main.jsbundle --assets-dest ios
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 打包 iOS Bundle | `npx react-native bundle --platform ios --entry-file index.js --bundle-output ios/main.jsbundle --assets-dest ios` | iOS 【常用】 |
| 打包 Android Bundle | `npx react-native bundle --platform android --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle --assets-dest android/app/src/main/res` | Android 【常用】 |
| 生成生产 Bundle | `npx react-native bundle --platform ios --entry-file index.js --bundle-output ios/main.jsbundle --dev false --minify true` | 生产优化 |
| 监视模式 | `npx react-native bundle --platform ios --entry-file index.js --bundle-output ios/main.jsbundle --watch` | 热更新 |

### npx react-native start 启动 Metro 开发服务器

**基础用法**:
```bash
npx react-native start
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 重置缓存启动 | `npx react-native start --reset-cache` | 清除缓存 【常用】 |
| 指定端口 | `npx react-native start --port %{端口}%` | 端口示例：`8081` |
| 开启 HTTPS | `npx react-native start --https` | HTTPS 调试 |
| 自定义配置文件 | `npx react-native start --config metro.config.js` | 指定配置 |

### Expo 命令

**基础用法**:
```bash
npx expo start
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动 Expo 开发 | `npx expo start` | 启动 Metro 【常用】 |
| 启动并打开 iOS | `npx expo start --ios` | 自动打开 iOS 模拟器 |
| 启动并打开 Android | `npx expo start --android` | 自动打开 Android 模拟器 |
| 启动并打开 Web | `npx expo start --web` | 打开浏览器 |
| 发布应用 | `npx expo publish` | 发布到 Expo 【常用】 |
| 发布到 EAS | `eas update --branch preview --message "%{更新说明}%"` | EAS 线上更新 |
| 构建 Android APK | `eas build --platform android --profile preview` | 构建 APK |
| 构建 iOS | `eas build --platform ios --profile preview` | 构建 IPA |
| 预构建原生项目 | `npx expo prebuild` | 生成 android/ios 目录 |
| 导出 Web | `npx expo export --platform web` | 导出 Web 应用 |

---

## Flutter

### flutter create 创建项目

**基础用法**:
```bash
flutter create %{项目名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建项目 | `flutter create %{项目名称}%` | 【常用】 |
| 指定组织 | `flutter create --org %{组织名}% %{项目名称}%` | 包名示例：`com.example` |
| 指定平台 | `flutter create --platforms=ios,android %{项目名称}%` | 仅指定平台 |
| 创建桌面应用 | `flutter create --platforms=windows,macos,linux %{项目名称}%` | 桌面应用 |
| 创建 Web 应用 | `flutter create --platforms=web %{项目名称}%` | Web 应用 |

### flutter run 运行应用

**基础用法**:
```bash
flutter run
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 运行调试版 | `flutter run` | 默认调试模式 【常用】 |
| 指定设备 | `flutter run -d %{设备ID}%` | 设备示例：`chrome` |
| 热重载模式 | `flutter run --hot` | 热重载启用 |
| 发布模式 | `flutter run --release` | Release 模式 |
| 调试模式 | `flutter run --debug` | 明确调试模式 |
| 指定 Observatory 端口 | `flutter run --observatory-port=12345` | 调试端口 |

### flutter build apk 构建 Android APK

**基础用法**:
```bash
flutter build apk
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 构建调试 APK | `flutter build apk` | 生成调试包 【常用】 |
| 构建发布 APK | `flutter build apk --release` | 生成发布包 【常用】 |
| 构建应用包 (AAB) | `flutter build appbundle` | Google Play 发布 【常用】 |
| 指定目标架构 | `flutter build apk --target-platform android-arm,android-arm64` | 多架构 |
| 代码压缩 | `flutter build apk --shrink` | 精简 APK |
| 分析构建 | `flutter build apk --verbose` | 详细日志 |

### flutter build ios 构建 iOS 应用

**基础用法**:
```bash
flutter build ios --simulator --no-codesign
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 模拟器构建 | `flutter build ios --simulator --no-codesign` | 模拟器版本 【常用】 |
| 真机构建 (Release) | `flutter build ios --release --no-codesign` | 真机测试 |
| 导出 IPA | `flutter build ios --release`（需签名配置） | 正式发布 |
| 查看可用构建 | `flutter devices` | 查看连接设备 |

### flutter doctor 环境诊断

**基础用法**:
```bash
flutter doctor
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 完整诊断 | `flutter doctor` | 检查所有依赖 【常用】 |
| 详细输出 | `flutter doctor -v` | 详细诊断信息 |
| 检查 Android 许可 | `flutter doctor --android-licenses` | 接受 Android 许可 |
| 指定路径检查 | `flutter doctor -d "%{路径}%"` | 检查指定环境 |

### flutter --version 版本信息

**基础用法**:
```bash
flutter --version
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 查看版本 | `flutter --version` | 当前版本 【常用】 |
| 查看 Dart 版本 | `dart --version` | Dart 版本 |
| 升级 Flutter | `flutter upgrade` | 升级到最新版 |
| 查看渠道 | `flutter channel` | 查看/切换发布渠道 |
| 切换稳定版 | `flutter channel stable` | 切换到稳定版 |

### dart pub get / dart run 包管理

**基础用法**:
```bash
dart pub get
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 获取依赖 | `dart pub get` | 安装 pubspec.yaml 中的依赖 【常用】 |
| 添加依赖 | `dart pub add %{依赖名}%` | 添加包 【常用】 |
| 添加开发依赖 | `dart pub add --dev %{依赖名}%` | 开发依赖 |
| 升级依赖 | `dart pub upgrade` | 升级到最新兼容版本 |
| 获取特定版本 | `dart pub get --%{版本约束}%` | 指定版本 |
| 运行 Dart 脚本 | `dart run %{脚本名}%.dart` | 运行 Dart 文件 |
| 格式化代码 | `dart format .` | 格式化 Dart 代码 |
| 静态分析 | `dart analyze` | 代码静态分析 |

---

## Android SDK

### sdkmanager 管理 SDK 组件

**基础用法**:
```bash
sdkmanager --list
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 列出已安装包 | `sdkmanager --list_installed` | 查看已安装 【常用】 |
| 安装平台工具 | `sdkmanager "platform-tools"` | 安装 platform-tools 【常用】 |
| 安装 SDK 平台 | `sdkmanager "platforms;android-34"` | 安装 Android 34 |
| 安装构建工具 | `sdkmanager "build-tools;34.0.0"` | 安装构建工具 |
| 接受许可 | `yes | sdkmanager --licenses` | 接受所有许可 |
| 卸载包 | `sdkmanager --uninstall "platforms;android-33"` | 卸载旧版本 |

### adb Android 调试桥

**基础用法**:
```bash
adb devices
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 列出设备 | `adb devices` | 查看连接设备 【常用】 |
| 安装 APK | `adb install %{apk路径}%` | 安装应用 【常用】 |
| 安装并替换 | `adb install -r %{apk路径}%` | 覆盖安装 |
| 卸载应用 | `adb uninstall %{包名}%` | 卸载应用 |
| 推送文件到设备 | `adb push %{本地路径}% %{设备路径}%` | 传输文件 【常用】 |
| 从设备拉取文件 | `adb pull %{设备路径}% %{本地路径}%` | 拉取文件 |
| 屏幕截图 | `adb exec-out screencap -p > screen.png` | 截图 |
| 屏幕录制 | `adb shell screenrecord /sdcard/video.mp4` | 录屏 |
| 查看日志 | `adb logcat` | 实时日志 【常用】 |
| 清除应用数据 | `adb shell pm clear %{包名}%` | 重置应用 |
| 启动 Activity | `adb shell am start -n %{包名}%/%{activity名}%` | 启动组件 |
| 重启设备 | `adb reboot` | 重启设备 |
| 重启到 Recovery | `adb reboot recovery` | 进入恢复模式 |
| 通过 WiFi 连接 | `adb tcpip 5555 && adb connect %{设备IP}%:5555` | 无线调试 【常用】 |
| 转发端口 | `adb forward tcp:8080 tcp:8080` | 端口转发 |

---

## Xcode 工具

### xcrun simctl 模拟器管理

**基础用法**:
```bash
xcrun simctl list devices available
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 列出可用模拟器 | `xcrun simctl list devices available` | 查看所有模拟器 【常用】 |
| 列出已运行模拟器 | `xcrun simctl list devices booted` | 查看运行中的 |
| 创建模拟器 | `xcrun simctl create "%{设备名}%" --family %{机型}% --os %{系统版本}%` | 创建新模拟器 |
| 删除模拟器 | `xcrun simctl delete %{设备名}%` | 删除模拟器 |
| 开机 | `xcrun simctl boot %{设备UUID}%` | 启动模拟器 |
| 关机 | `xcrun simctl shutdown %{设备UUID}%` | 关闭模拟器 |

### xcodebuild Xcode 构建

**基础用法**:
```bash
xcodebuild -project %{项目名}%.xcodeproj -scheme %{scheme}% -sdk iphonesimulator -destination 'platform=iOS Simulator,name=iPhone 15' build
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 构建 iOS 项目 | `xcodebuild -project %{项目名}%.xcodeproj -scheme %{scheme}% build` | 编译项目 【常用】 |
| 模拟器构建 | `xcodebuild -project App.xcodeproj -scheme App -sdk iphonesimulator -destination 'platform=iOS Simulator,name=iPhone 15' build` | 模拟器构建 |
| 真机构建 | `xcodebuild -project App.xcodeproj -scheme App -sdk iphoneos -configuration Release build` | Release 构建 |
| 清理构建 | `xcodebuild clean` | 清除构建缓存 |
| 查看 Schemes | `xcodebuild -list` | 列出可用 Schemes |
| 导出 Archive | `xcodebuild -project App.xcodeproj -scheme App -exportArchive -archivePath App.xcarchive -exportPath ./output -exportOptionsPlist ExportOptions.plist` | 导出 IPA |

---

## Ionic 跨平台

### ionic start 创建 Ionic 项目

**基础用法**:
```bash
ionic start %{项目名称}% blank
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建空白项目 | `ionic start %{项目名称}% blank` | 空白模板 【常用】 |
| 创建标签页项目 | `ionic start %{项目名称}% tabs` | 底部标签页模板 |
| 创建侧边菜单项目 | `ionic start %{项目名称}% sidemenu` | 侧边菜单模板 |
| 指定框架 | `ionic start %{项目名称}% blank --capacitor` | 使用 Capacitor |
| 指定 Vue | `ionic start %{项目名称}% blank --type vue` | Vue 框架 |
| 指定 React | `ionic start %{项目名称}% blank --type react` | React 框架 |

### ionic build 构建应用

**基础用法**:
```bash
ionic build
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 构建 Web 应用 | `ionic build` | 构建 PWA 【常用】 |
| 生产构建 | `ionic build --prod` | 生产优化构建 |
| 指定平台构建 | `ionic build --platform android` | Android 平台 |
| 指定平台构建 | `ionic build --platform ios` | iOS 平台 |

### ionic serve 启动开发服务器

**基础用法**:
```bash
ionic serve
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 启动服务 | `ionic serve` | 启动开发服务器 【常用】 |
| 指定端口 | `ionic serve --port %{端口}%` | 端口示例：`8100` |
| 打开浏览器 | `ionic serve --open` | 自动打开浏览器 |
| 实时重载 | `ionic serve --livereload` | 热重载 |

---

## Capacitor

### npx cap init 初始化 Capacitor

**基础用法**:
```bash
npx cap init %{应用名}% %{包名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 初始化项目 | `npx cap init %{应用名}% %{包名}%` | 配置 Capacitor 【常用】 |
| 添加平台 | `npx cap add ios` | 添加 iOS 【常用】 |
| 添加平台 | `npx cap add android` | 添加 Android 【常用】 |
| 添加平台 | `npx cap add electron` | 添加 Electron |
| 查看状态 | `npx cap doctor` | 检查配置 【常用】 |

### npx cap sync 同步原生项目

**基础用法**:
```bash
npx cap sync
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 同步所有平台 | `npx cap sync` | 同步 Web 到原生 【常用】 |
| 同步 iOS | `npx cap sync ios` | 仅同步 iOS |
| 同步 Android | `npx cap sync android` | 仅同步 Android |
| 打开 IDE | `npx cap open ios` | 用 Xcode 打开 |
| 打开 IDE | `npx cap open android` | 用 Android Studio 打开 |

### npx cap copy 复制 Web 资源

**基础用法**:
```bash
npx cap copy
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 复制 Web 资源 | `npx cap copy` | 复制到原生目录 【常用】 |
| 复制到 iOS | `npx cap copy ios` | 仅 iOS |
| 复制到 Android | `npx cap copy android` | 仅 Android |

---

## Cordova

### ionic cordova create 创建 Cordova 项目

**基础用法**:
```bash
ionic cordova create %{项目名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建项目 | `ionic cordova create %{项目名称}%` | 创建 Cordova 项目 |
| 指定 ID | `ionic cordova create %{项目名称}% %{包名}%` | 指定包名 |
| 指定模板 | `ionic cordova create %{项目名称}% --template %{模板名}%` | 使用模板 |

### ionic cordova platform add 添加平台

**基础用法**:
```bash
ionic cordova platform add ios
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 添加 iOS | `ionic cordova platform add ios` | 添加 iOS 【常用】 |
| 添加 Android | `ionic cordova platform add android` | 添加 Android 【常用】 |
| 指定版本 | `ionic cordova platform add ios@6.0.0` | 指定 Cordova 版本 |
| 移除平台 | `ionic cordova platform remove ios` | 移除平台 |

### ionic cordova build 构建应用

**基础用法**:
```bash
ionic cordova build ios
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 构建 iOS | `ionic cordova build ios` | iOS 构建 【常用】 |
| 构建 Android | `ionic cordova build android` | Android 构建 【常用】 |
| 发布构建 | `ionic cordova build ios --release` | 发布模式 |
| 调试构建 | `ionic cordova build android --debug` | 调试模式 |

### ionic cordova run 在设备运行

**基础用法**:
```bash
ionic cordova run ios
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| iOS 运行 | `ionic cordova run ios` | iOS 设备运行 【常用】 |
| Android 运行 | `ionic cordova run android` | Android 设备运行 【常用】 |
| 指定设备 | `ionic cordova run ios --device` | 真机运行 |
| 模拟器运行 | `ionic cordova run ios --emulator` | 模拟器运行 |

### Cordova plugin 管理

**基础用法**:
```bash
ionic cordova plugin add %{插件名}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 添加插件 | `ionic cordova plugin add %{插件名}%` | 添加插件 【常用】 |
| 列出已装插件 | `ionic cordova plugin list` | 查看已安装 |
| 移除插件 | `ionic cordova plugin rm %{插件名}%` | 移除插件 |
| 搜索插件 | `cordova plugin search %{关键词}%` | 搜索插件 |

---

## Tauri

### npm create tauri-app 创建 Tauri 项目

**基础用法**:
```bash
npm create tauri-app@latest %{项目名称}%
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 创建项目 | `npm create tauri-app@latest %{项目名称}%` | 创建 Tauri 项目 【常用】 |
| 指定模板 | `npm create tauri-app@latest %{项目名称}% --template vanilla` | 无框架模板 |
| 指定模板 | `npm create tauri-app@latest %{项目名称}% --template vue-ts` | Vue+TS 模板 |
| 指定模板 | `npm create tauri-app@latest %{项目名称}% --template react-ts` | React+TS 模板 |
| 非交互式创建 | `npm create tauri-app@latest %{项目名称}% --yes` | 自动选择默认选项 |

### tauri build 构建 Tauri 应用

**基础用法**:
```bash
npm run tauri build
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 构建生产版本 | `npm run tauri build` | 生成可执行文件 【常用】 |
| 开发模式 | `npm run tauri dev` | 启动开发模式 【常用】 |
| 指定平台 | `tauri build --target x86_64-pc-windows-msvc` | 指定目标架构 |
| 调试构建 | `TAURI_DEBUG=1 npm run tauri build` | 带调试信息 |
| 查看构建配置 | `cat src-tauri/tauri.conf.json` | 查看 Tauri 配置 |

### tauri init 初始化 Tauri

**基础用法**:
```bash
npm run tauri init
```

**扩展示例**:

| 场景 | 命令 | 说明 |
|------|------|------|
| 初始化配置 | `npm run tauri init` | 生成 Tauri 配置 【常用】 |
| 指定应用名 | `npm run tauri init --app-name "%{应用名}%" --window-title "%{窗口标题}%"` | 定制化初始化 |
| 查看配置文档 | `npx tauri help init` | 帮助信息 |

---

## 实用场景

### 场景 1: React Native 完整开发流程

```bash
# 1. 创建新项目
npx react-native@latest init MyReactApp

# 2. 进入项目目录
cd MyReactApp

# 3. 安装额外依赖（如导航）
npm install @react-navigation/native @react-navigation/stack
npm install react-native-screens react-native-safe-area-context

# 4. 启动开发服务器
npx react-native start

# 5. 在新终端运行 iOS 应用
npx react-native run-ios

# 6. 在新终端运行 Android 应用
npx react-native run-android

# 7. 打包 JS Bundle（用于离线或发布）
npx react-native bundle --platform ios --entry-file index.js --bundle-output ios/main.jsbundle --assets-dest ios
npx react-native bundle --platform android --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle --assets-dest android/app/src/main/res
```

### 场景 2: Flutter 完整开发流程

```bash
# 1. 创建新项目
flutter create --org com.example my_flutter_app

# 2. 进入项目目录
cd my_flutter_app

# 3. 获取依赖
flutter pub get

# 4. 添加依赖（如 http）
flutter pub add http

# 5. 检查环境
flutter doctor

# 6. 运行应用
flutter run

# 7. 构建 Android APK
flutter build apk --release

# 8. 构建 iOS（模拟器）
flutter build ios --simulator --no-codesign
```

### 场景 3: Capacitor 跨平台开发

```bash
# 1. 创建 Web 项目
npm create vite@latest my-cap-app -- --template react-ts
cd my-cap-app && npm install

# 2. 安装 Capacitor
npm install @capacitor/core @capacitor/cli

# 3. 初始化 Capacitor
npx cap init MyApp com.example.myapp

# 4. 添加平台
npx cap add ios
npx cap add android

# 5. 构建 Web 应用
npm run build

# 6. 同步到原生
npx cap sync

# 7. 打开 IDE 进行原生开发
npx cap open ios
npx cap open android
```

### 场景 4: Android 设备调试

```bash
# 1. 连接设备并检查
adb devices

# 2. 安装应用
adb install -r app-debug.apk

# 3. 清除应用数据并重启
adb shell pm clear com.example.app
adb shell am start -n com.example.app/.MainActivity

# 4. 查看日志
adb logcat | grep com.example.app

# 5. 屏幕录制（最多 3 分钟）
adb shell screenrecord /sdcard/demo.mp4
adb pull /sdcard/demo.mp4 ./

# 6. 通过 WiFi 无线调试
adb tcpip 5555
adb connect 192.168.1.100:5555
```

---

## 命令速查表

| 操作 | 命令 | 说明 |
|------|------|------|
| 创建 React Native 项目 | `npx react-native@latest init %{项目名}%` | React Native 【推荐】 |
| 运行 Android | `npx react-native run-android` | Android 【常用】 |
| 运行 iOS | `npx react-native run-ios` | iOS 【常用】 |
| 启动 Metro | `npx react-native start` | 开发服务器 【常用】 |
| Expo 启动 | `npx expo start` | Expo 开发 【常用】 |
| Expo 发布 | `npx expo publish` | 发布到 Expo |
| 创建 Flutter 项目 | `flutter create %{项目名}%` | Flutter 【推荐】 |
| 运行 Flutter | `flutter run` | 运行应用 【常用】 |
| 构建 Android APK | `flutter build apk` | APK 【常用】 |
| 构建 iOS | `flutter build ios --simulator --no-codesign` | iOS 模拟器 |
| Flutter 环境检查 | `flutter doctor` | 诊断 【常用】 |
| Flutter 版本 | `flutter --version` | 版本信息 |
| Dart 获取依赖 | `dart pub get` | 依赖 【常用】 |
| Dart 运行脚本 | `dart run %{脚本}%.dart` | 运行脚本 |
| 列出 Android 设备 | `adb devices` | 设备列表 【常用】 |
| 安装 APK | `adb install %{apk路径}%` | 安装应用 【常用】 |
| Android 日志 | `adb logcat` | 日志 【常用】 |
| Android 无线调试 | `adb tcpip 5555 && adb connect %{IP}%:5555` | WiFi 调试 |
| 列出 iOS 模拟器 | `xcrun simctl list devices available` | 模拟器 【常用】 |
| Xcode 构建 | `xcodebuild -project App.xcodeproj -scheme App build` | 构建 |
| 创建 Ionic 项目 | `ionic start %{项目名}% tabs` | Ionic |
| Ionic 构建 | `ionic build --prod` | 生产构建 |
| Capacitor 初始化 | `npx cap init %{应用名}% %{包名}%` | 初始化 【常用】 |
| Capacitor 添加平台 | `npx cap add ios && npx cap add android` | 添加平台 |
| Capacitor 同步 | `npx cap sync` | 同步 【常用】 |
| Cordova 添加平台 | `ionic cordova platform add ios` | 添加平台 |
| Cordova 构建 | `ionic cordova build ios` | iOS 构建 |
| Tauri 创建项目 | `npm create tauri-app@latest %{项目名}%` | Tauri |
| Tauri 开发 | `npm run tauri dev` | 开发模式 |
| Tauri 构建 | `npm run tauri build` | 生产构建 |

---

## 相关资源

- [前端包管理器文档](../前端包管理器/README.md)
- [React 命令文档](../React 命令/README.md)
- [Node.js 后端命令文档](../Node.js 后端命令/README.md)
- [Git 命令文档](../Git 命令/README.md)
- [React Native 官方文档](https://reactnative.dev/)
- [Flutter 官方文档](https://flutter.dev/)
- [Expo 官方文档](https://docs.expo.dev/)
- [Capacitor 官方文档](https://capacitorjs.com/)
- [Ionic 官方文档](https://ionicframework.com/)
- [Tauri 官方文档](https://tauri.app/)