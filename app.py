from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

# Configuration for SQLAlchemy and Flask-Migrate
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define your Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    technology = db.Column(db.String(100), nullable=False)
    yearCreated = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Project('{self.title}', '{self.description}', '{self.technology}', '{self.yearCreated}')"

# Route for Home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for Projects page
@app.route('/projects')
def projects():
    # Fetch all projects from the database
    projects = Project.query.all()  # Get all the projects
    return render_template('projects.html', projects=projects)

@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        # Get data from the form
        title = request.form['title']
        description = request.form['description']
        technology = request.form['technology']
        year_created = request.form['yearCreated']

        # Create new project object
        new_project = Project(
            title=title,
            description=description,
            technology=technology,
            yearCreated=year_created
        )

        # Add the new project to the database
        db.session.add(new_project)
        db.session.commit()

        # Redirect to home or another page after successful submission
        return redirect(url_for('home'))

    return render_template('add_project.html')

# Route for About Me page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
