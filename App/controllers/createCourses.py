from App.models import CreateCourses
from App.database import db

def create_newCourse(courseID, courseName):
    newCourse = CreateCourses(courseID = courseID, courseName = courseName)
    db.session.add(newCourse)
    db.session.commit()
    return newCourse

'''
def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()
'''

def get_all_courses_json():
    c = CreateCourses.query.all()
    if not c:
        return []
    c = [courses.get_json() for courses in c]
    return c

'''
def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    '''