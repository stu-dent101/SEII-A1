#from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
#from App.models import CreateCourses

class AdminCreateCourses(db.Model):
    __tablename__ = 'adminCreateCourses'
    adminCreateCoursesCount = db.Column(db.Integer, primary_key=True, autoincrement=True)
    courseID = db.Column(db.Integer, db.ForeignKey('createCourses.courseID'))
    adminID = db.Column(db.Integer, db.ForeignKey('administrator.adminID'))


    def __init__(self, courseID, adminID):
        self.courseID = courseID
        self.adminID = adminID
'''
    def get_json(self):
        return{
            'adminID': self.adminID,
            'staffID': self.staffID,
            'First Name': self.fName,
            'Last Name': self.lName
        }
    
    '''
    