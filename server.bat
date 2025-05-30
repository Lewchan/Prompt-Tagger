@echo off
echo 🚀 正在启动服务器...
start http://localhost:8000/test_index.html
python -m http.server 8000 