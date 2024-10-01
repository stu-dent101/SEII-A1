#from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from .createCourses import CreateCourses
from .createStaff import CreateStaff

class AssignStaff(db.Model):
    __tablename__ = 'assignStaff'
    assignmentID = db.Column(db.Integer, primary_key=True, unique=True)
    staffID = db.Column(db.Integer, db.ForeignKey('createStaff.staffID'))
    courseID = db.Column(db.Integer, db.ForeignKey('createCourses.courseID'))
    position =  db.Column(db.String(20), nullable=False)
    courseLocation = db.Column(db.String(20), nullable=False)

    #this table is dependent on CreateStaff and CreateCourses

    def __init__(self, assignmentID, staffID, position, courseID, courseLocation, course_manager1: CreateCourses, course_manager2: CreateStaff):
        self.assignmentID = assignmentID
        self.staffID = staffID
        self.position = position
        self.courseID = courseID
        self.courseLocation = courseLocation
        self.course_manager1 = course_manager1  # Dependency on CreateCourses
        self.course_manager2 = course_manager2  # Dependency on CreateStaff

    def assign_staff(self):
        # Dependency on CreateCourses to validate course
        valid_course = self.course_manager.get_course(self.courseID)
        
        if valid_course:
            return f"Staff '{self.courseID}' of position '{self.position}'assigned to '{self.staff_id}' at location '{self.courseLocation}'."
        else:
            return f"Course '{self.staff_id}' does not exist. Cannot assign lecture."   
        

    def get_json(self):
        return{
            'assignmentID': self.assignmentID,
            'staffID': self.staffID,
            'position': self.position,
            'courseID': self.courseID,
            'courseLocation': self.courseLocation
        }
'''
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
'''
