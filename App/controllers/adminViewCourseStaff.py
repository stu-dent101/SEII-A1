from App.models import AdminViewCourseStaff 
from App.database import db

def adminViewCourseStaff(adminVCSID, staffCount, adminID):
    view = AdminViewCourseStaff(adminVCSID = adminVCSID, staffCount = staffCount, adminID = adminID)
    db.session.add(view)
    db.session.commit()
    return view


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