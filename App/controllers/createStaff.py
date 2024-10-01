from App.models import CreateStaff
from App.database import db

def create_staff(staffID, fName, lName, position):
    newStaff = CreateStaff(staffID = staffID, fName = fName, lName = lName, position = position)
    db.session.add(newStaff)
    db.session.commit()
    return newStaff

    '''
def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()
'''
def get_all_staff_json():
    members = CreateStaff.query.all()
    if not members:
        return []
    members = [staff.get_json() for staff in members]
    return members

'''
def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    '''