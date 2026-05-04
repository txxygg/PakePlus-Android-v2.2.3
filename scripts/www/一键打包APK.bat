@echo off
chcp 65001 >nul
title NanoBanana APK打包工具

echo.
echo ╔══════════════════════════════════════════╗
echo ║   NanoBanana APK 一键打包工具 v1.0       ║
echo ╚══════════════════════════════════════════╝
echo.

:: 检查文件
if not exist "index.html" (
    echo [错误] 未找到 index.html 文件！
    echo 请将此脚本放在 nanobanana-app 文件夹中运行
    pause
    exit /b 1
)

echo [1/3] 检查环境...

:: 启动本地服务器
echo [2/3] 启动本地服务器...
start "" "http://localhost:8080"
echo.

:: 尝试启动Python服务器
python -m http.server 8080 >nul 2>&1 &
if errorlevel 1 (
    :: Python不可用，尝试Node.js
    npx -y serve -l 8080 >nul 2>&1 &
    if errorlevel 1 (
        echo [提示] 未检测到本地服务器环境
        echo 请手动打开浏览器访问: http://localhost:8080
    )
)

echo [3/3] 打开在线打包工具...
timeout /t 2 /nobreak >nul

:: 打开AppsGeyser
start "" "https://appsgeyser.com"

echo.
echo ═══════════════════════════════════════════
echo 操作完成！
echo.
echo 打包步骤：
echo 1. 在AppsGeyser页面选择 "Website"
echo 2. 上传本文件夹中的 index.html
echo 3. 填写APP名称：NanoBanana
echo 4. 点击 Create App 生成APK
echo.
echo 注意：需开启手机"未知来源安装"
echo ═══════════════════════════════════════════
echo.
pause
