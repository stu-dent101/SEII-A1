from App.models import AssignStaff
from App.database import db

def assignStaffMember(assignmentID, staffID, courseID, position, courseLocation):
    assignment = AssignStaff(assignmentID = assignmentID, staffID = staffID, courseID = courseID, position = position, courseLocation = courseLocation)
    db.session.add(assignment)
    db.session.commit()
    return assignment


'''
def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    '''