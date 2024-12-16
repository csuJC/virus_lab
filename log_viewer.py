from flask import Flask, render_template_string
import os
import re
from datetime import datetime

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>病毒程序日志查看器</title>
    <meta charset="utf-8">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f0f0f0;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 30px;
        }
        .log-entry {
            margin-bottom: 20px;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            background-color: #f9f9f9;
        }
        .timestamp {
            color: #666;
            font-size: 0.9em;
        }
        .level {
            font-weight: bold;
            margin-right: 10px;
        }
        .info { color: #2196F3; }
        .warning { color: #FF9800; }
        .error { color: #F44336; }
        .stats {
            margin-top: 20px;
            padding: 15px;
            background-color: #e3f2fd;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>病毒程序日志查看器</h1>
        
        <div class="stats">
            <h3>统计信息</h3>
            <p>总执行次数: {{ execution_count }}</p>
            <p>最后执行时间: {{ last_execution }}</p>
            <p>成功感染文件数: {{ infected_files }}</p>
        </div>

        {% for entry in log_entries %}
        <div class="log-entry">
            <span class="timestamp">{{ entry.timestamp }}</span>
            <span class="level {{ entry.level.lower() }}">{{ entry.level }}</span>
            <span class="message">{{ entry.message }}</span>
        </div>
        {% endfor %}
    </div>
</body>
</html>
'''

def parse_log_file(log_file_path):
    log_entries = []
    execution_count = 0
    infected_files = 0
    last_execution = None
    
    if os.path.exists(log_file_path):
        with open(log_file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) - (\w+) - (.+)', line)
                if match:
                    timestamp, level, message = match.groups()
                    log_entries.append({
                        'timestamp': timestamp,
                        'level': level,
                        'message': message
                    })
                    
                    if '病毒程序开始执行' in message:
                        execution_count += 1
                        last_execution = timestamp
                    elif '成功感染文件' in message:
                        infected_files += 1
    
    return {
        'log_entries': reversed(log_entries),  # 最新的日志显示在前面
        'execution_count': execution_count,
        'infected_files': infected_files,
        'last_execution': last_execution or '无记录'
    }

@app.route('/')
def view_logs():
    log_file_path = 'test/virus.log'  # 日志文件路径
    log_data = parse_log_file(log_file_path)
    return render_template_string(HTML_TEMPLATE, **log_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000) 