import http.server
import socketserver
import os
import webbrowser
from urllib.parse import urlparse

# 设置端口
PORT = 8000

# 获取当前目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 切换到当前目录
os.chdir(current_dir)

# 创建处理器
Handler = http.server.SimpleHTTPRequestHandler

# 创建服务器
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"🚀 服务器已启动在 http://localhost:{PORT}")
    print("📂 当前目录:", current_dir)
    print("💡 请在浏览器中访问以下地址：")
    print(f"   http://localhost:{PORT}/test_index.html")
    print("\n⚠️ 按 Ctrl+C 停止服务器")
    
    # 自动打开浏览器
    webbrowser.open(f"http://localhost:{PORT}/test_index.html")
    
    # 启动服务器
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 服务器已停止") 