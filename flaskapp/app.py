import os
import zipfile
#import toml
from hashlib import sha256
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
PROJECTS_DIR = os.environ.get('PROJECTS_DIR', 'projects')

if not os.path.exists(PROJECTS_DIR):
    os.makedirs(PROJECTS_DIR)

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer, unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def generate_token(self):
        token = sha256(bytes(str(self.id), 'utf-8')).hexdigest()
        db.session.add(Token(user_id=self.id, token=token))
        db.session.commit()
        return token

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    project_name = db.Column(db.String(120), nullable=False)
    language = db.Column(db.String(20), nullable=False)
    program_code = db.Column(db.Text, nullable=False)
    readme = db.Column(db.Text, nullable=False)
    zip_path = db.Column(db.String(255), nullable=False)
    user = db.relationship('User', backref=db.backref('projects', lazy=True))

class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    token = db.Column(db.String(255), nullable=False)
    user = db.relationship('User', backref=db.backref('tokens', lazy=True))


# Tournament data (stored as JSON for simplicity)
tournament_data = []

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.before_request
def create_tables():
    app.before_request_funcs[None].remove(create_tables)
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.check_password(request.form['password']):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if User.query.filter_by(username=request.form['username']).first():
            flash('Username already exists. Please choose another one.', 'danger')
            return redirect(url_for('register'))
        user = User(username=request.form['username'], password="")
        user.set_password(request.form['password'])

        db.session.add(user)
        db.session.commit()

        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/live')
@login_required
def live_feed():
    return render_template('live_feed.html')

@app.route('/download')
@login_required
def download_tool():
    # Serve different files based on OS (just example paths)
    user_agent = request.headers.get('User-Agent')
    if 'Windows' in user_agent:
        return redirect('/static/tools/windows_tool.exe')
    elif 'Mac' in user_agent:
        return redirect('/static/tools/mac_tool.dmg')
    else:
        return redirect('/static/tools/linux_tool.sh')

@app.route('/submit', methods=['GET', 'POST'])
@login_required
def submit_project():
    if request.method == 'POST':
        project_name = request.form['project_name']
        program_code = request.form['program_code']
        readme = request.form['readme']
        language = request.form['language']

        # Create zip file path based on username and project name
        zip_filename = f"{current_user.username}_{project_name}.zip"
        zip_path = os.path.join(PROJECTS_DIR, zip_filename)

        # Write program_code and readme to zip file
        with zipfile.ZipFile(zip_path, 'w') as zip_file:
            zip_file.writestr('program_code.txt', program_code)
            zip_file.writestr('README.md', readme)

        # Save project details to database
        project = Project(
            user_id=current_user.id,
            project_name=project_name,
            language=language,
            program_code=program_code,
            readme=readme,
            zip_path=zip_path
        )
        db.session.add(project)
        db.session.commit()

        return render_template('submit_project.html', success=True)
    return render_template('submit_project.html')

@app.route('/admin')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    return render_template('admin.html')

@app.route('/admin/generate_token')
@login_required
def generate_token():
    if not current_user.is_admin:
        return redirect(url_for('index'))
    # Generate token logic
    return current_user.generate_token()

@app.route('/api/live_feed', methods=['POST'])
def api_live_feed():
    token = request.headers.get('Authorization')
    if token != "your_token":  # Replace with actual token check
        return jsonify({'error': 'Unauthorized'}), 403
    data = request.get_json()
    tournament_data.append(data)
    return jsonify({'message': 'Data received'}), 200

@app.route('/api/live_feed', methods=['GET'])
def get_live_feed():
    return jsonify(tournament_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)