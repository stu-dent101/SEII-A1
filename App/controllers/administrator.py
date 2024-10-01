from App.models import Administrator

'''
from App.models import CreateCourses
from App.models import CreateStaff
from App.models import AssignStaff
from App.models import CreateStaff
'''

from App.database import db

def create_admin(adminID, staffID, fName, lName):
    existing_admin = Administrator.query.filter_by(adminID=adminID).first()
    
    if existing_admin:
        print(f"Administrator with ID {adminID} already exists.")
        return
    
    newAdmin = Administrator(adminID = adminID, staffID = staffID, fName = fName, lName = lName)
    db.session.add(newAdmin)
    db.session.commit()
    return newAdmin
'''
def createCourse(courseName, courseID):
        try:
            new_course = Administrator(courseName=courseName, courseID=courseID)
            #self.createCourses.append(new_course)
            db.session.add(new_course)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error creating course: {e}")
            return False

    # Method to view course staff as a dictionary
def viewStaff(self):
        try:
            course_staff_dict = {}
            for course in self.createCourses:
                course_staff_dict[course.courseName] = [staff.fName for staff in course.viewStaffs]
            return course_staff_dict
        except Exception as e:
            print(f"Error viewing course staff: {e}")
            return {}

    # Method to create a new staff member
def createS(self, staffID, fName, lName):
        try:
            new_staff = CreateStaff(staffID=staffID, fName=fName, lName=lName)
            self.createS.append(new_staff)
            db.session.add(new_staff)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error creating staff: {e}")
            return False

    # Method to assign staff to a course
def assignS(self, staffID, courseID):
        try:
            staff = AssignStaff.query.filter_by(staffID=staffID).first()
            course = CreateCourses.query.filter_by(courseID=courseID).first()
            if staff and course:
                course.assignS.append(staff)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            print(f"Error assigning staff: {e}")
            return False
'''

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