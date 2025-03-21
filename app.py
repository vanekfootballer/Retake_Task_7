from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import requests

load_dotenv()
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def resume():
    if request.method == 'POST':
        return jsonify({"status": "success", "message": "Форма обработана"})
    
    # Загрузка данных из .env
    context = {
        'full_name': os.getenv('FULL_NAME'),
        'city': os.getenv('CITY'),
        'telegram': os.getenv('TELEGRAM'),
        'university': os.getenv('UNIVERSITY'),
        'program': os.getenv('PROGRAM'),
        'course': os.getenv('COURSE')
    }
    
    # Запрос к GitHub API
    headers = {"Authorization": f"token {os.getenv('GITHUB_TOKEN')}"}
    response = requests.get("https://api.github.com/user/repos", headers=headers)
    context['repos'] = response.json() if response.status_code == 200 else []
    
    return render_template('resume.html', **context)

if __name__ == '__main__':
    app.run(debug=True)
