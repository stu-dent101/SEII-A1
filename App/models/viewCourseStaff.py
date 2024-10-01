#from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from .createCourses import CreateCourses
from .createStaff import CreateStaff


class ViewCourseStaff(db.Model): 
    __tablename__ = 'viewCourseStaff'
    staffCount = db.Column(db.Integer, primary_key=True, autoincrement=True)
    staffID = db.Column(db.Integer, db.ForeignKey('createStaff.staffID'))
    courseID = db.Column(db.Integer, db.ForeignKey('createCourses.courseID'))
    fName =  db.Column(db.String(20), nullable=False)
    lName =  db.Column(db.String(20), nullable=False)
    position =  db.Column(db.String(20), nullable=False)

    #this table is dependent on CreateCourses and CreateStaff

    def __init__(self, staffCount, staffID, courseID, fName, lName, position, course_manager1: CreateCourses, course_manager2: CreateStaff ):
        self.staffCount = staffCount
        self.staffID = staffID
        self.courseID = courseID
        self.fName = fName
        self.lName = lName
        self.position = position
        self.course_manager1 = course_manager1  # Dependency on CreateCourses
        self.course_manager2 = course_manager2  # Dependency on CreateStaff
    
    def get_json(self):
        return{
            'staffCount': self.staffCount,
            'staffID': self.staffID,
            'courseID': self.courseID,
            'fName': self.fName,
            'lName': self.lName,
            'position': self.position
        }

'''
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
'''
