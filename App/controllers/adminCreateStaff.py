from App.models import AdminCreateStaff
from App.database import db

def create_adminCreateStaff(adminCSID, adminID, staffID):
    newAdminCreateStaff = AdminCreateStaff(adminCSID = adminCSID, adminID = adminID, staffID = staffID)
    db.session.add(newAdminCreateStaff)
    db.session.commit()
    return newAdminCreateStaff

'''
def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

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