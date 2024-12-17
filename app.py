from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Configure SQLAlchemy with your database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite database in the current directory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking for performance reasons

# Initialize the database extension
db = SQLAlchemy(app)

# Define a Project model (table)
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # ID for each project
    title = db.Column(db.String(100), nullable=False)  # Project title
    description = db.Column(db.Text, nullable=False)  # Project description

    def __repr__(self):
        return f"Project('{self.title}', '{self.description}')"

# Route for Home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for Projects page (fetching data from the database)
@app.route('/projects')
def projects():
    # Fetch all projects from the database
    all_projects = Project.query.all()  # Get all projects
    return render_template('projects.html', projects=all_projects)

# Route for About Me page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
