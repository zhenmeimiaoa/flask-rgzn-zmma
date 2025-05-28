from flask import Flask, render_template
import os
from pyngrok import ngrok
import ngrok_config  # 导入配置

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # 确保templates目录存在
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    # 启动ngrok
    http_tunnel = ngrok.connect(5000)
    print(f' * 公网访问地址: {http_tunnel.public_url}')
    
    # 启动Flask应用
    app.run(host='0.0.0.0', port=5000, debug=True) 