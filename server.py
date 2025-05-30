from flask import Flask, request, jsonify, send_from_directory
import json
import os
import traceback

app = Flask(__name__)

# 配置文件路径
ENUMS_FILE = 'assets/config/enums.json'
STRINGS_FILE = 'assets/config/strings.json'

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/assets/config/<path:filename>')
def serve_config(filename):
    return send_from_directory('assets/config', filename)

@app.route('/api/save_enum', methods=['POST'])
def save_enum():
    try:
        data = request.json
        if not data:
            return jsonify({'success': False, 'message': '没有接收到数据'})
            
        enums_data = data.get('enums')
        strings_data = data.get('strings')
        
        if not enums_data or not strings_data:
            return jsonify({'success': False, 'message': '数据格式不正确'})
        
        # 确保目录存在
        os.makedirs('assets/config', exist_ok=True)
        
        # 写入文件
        try:
            with open(ENUMS_FILE, 'w', encoding='utf-8') as f:
                json.dump(enums_data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            return jsonify({'success': False, 'message': f'保存enums.json失败: {str(e)}'})
        
        try:
            with open(STRINGS_FILE, 'w', encoding='utf-8') as f:
                json.dump(strings_data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            return jsonify({'success': False, 'message': f'保存strings.json失败: {str(e)}'})
        
        return jsonify({'success': True, 'message': '保存成功'})
    except Exception as e:
        error_trace = traceback.format_exc()
        print(f'保存失败: {error_trace}')
        return jsonify({'success': False, 'message': f'保存失败: {str(e)}\n{error_trace}'})

if __name__ == '__main__':
    app.run(debug=True, port=5000) 