from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

def load_projects():
    with open('projects.json') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects_page():
    projects = load_projects()
    return render_template('projects.html', projects=projects)

@app.route('/projects/<int:project_id>')
def project_detail(project_id):
    projects = load_projects()
    project = next((proj for proj in projects if proj["id"] == project_id), None)
    if project is None:
        return "Project not found", 404
    return render_template('project_detail.html', project=project)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)