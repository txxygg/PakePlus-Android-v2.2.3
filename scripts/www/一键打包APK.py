#!/usr/bin/env python3
"""
NanoBanana APK一键打包工具
使用WebView打包成本地APK
"""

import os
import sys
import webbrowser
import http.server
import socketserver
import threading
import time

PORT = 8080
APP_DIR = os.path.dirname(os.path.abspath(__file__))

def start_server():
    """启动本地HTTP服务器"""
    os.chdir(APP_DIR)
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"✅ 服务器已启动: http://localhost:{PORT}")
        httpd.serve_forever()

def main():
    print("""
╔══════════════════════════════════════════╗
║   NanoBanana APK 一键打包工具 v1.0       ║
╚══════════════════════════════════════════╝
    """)
    
    # 检查index.html是否存在
    if not os.path.exists('index.html'):
        print("❌ 错误：未找到 index.html 文件！")
        print(f"请确保在 {APP_DIR} 文件夹中运行此脚本")
        input("\n按回车键退出...")
        sys.exit(1)
    
    print(f"📁 工作目录: {APP_DIR}")
    print()
    
    # 启动服务器线程
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    time.sleep(1)
    
    # 打开AppsGeyser
    print("🌐 正在打开 AppsGeyser 在线打包工具...")
    webbrowser.open('https://appsgeyser.com')
    
    # 打开本地预览
    print("🔗 正在打开本地预览...")
    webbrowser.open(f'http://localhost:{PORT}')
    
    print("""
╔══════════════════════════════════════════════════════════╗
║                    打包步骤说明                          ║
╠══════════════════════════════════════════════════════════╣
║  1. 在 AppsGeyser 页面选择 "Website" 选项              ║
║  2. 点击 "Upload" 上传 index.html 文件                   ║
║  3. APP Name 填写: NanoBanana                          ║
║  4. 点击 "Create App" 生成APK                          ║
║  5. 下载APK文件，传到手机安装即可                        ║
╚══════════════════════════════════════════════════════════╝
    """)
    
    print("📱 本地预览已打开，可以测试功能是否正常")
    print("⏹️ 关闭此窗口即可停止本地服务器")
    print()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n👋 已退出")
        sys.exit(0)

if __name__ == '__main__':
    main()
