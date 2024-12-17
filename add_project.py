from app import db, Project
from app import app 

# Create a new project - SkillsMaster
new_project = Project(
    title="SkillsMaster",
    description="Frontend developer - working in a team in an internship",
    technology="ReactJS, Java Spring Boot",  # same technologies as The Great Outdoors
    yearCreated=2023
)

# Adding the new project to the database
with app.app_context():
    db.session.add(new_project)
    db.session.commit()  # Commit the new project to the database

    # Query and print all projects to verify
    projects = Project.query.all()
    print(projects)  # This will print the list of all projects in the database
