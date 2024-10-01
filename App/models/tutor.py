#from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from.createStaff import CreateStaff
from .createCourses import CreateCourses

class Tutor(CreateStaff):
    __tablename__ = 'tutor'
    tutorID = db.Column(db.Integer, primary_key=True, unique=True)
    staffID = db.Column(db.Integer, db.ForeignKey('createStaff.staffID'))
    courseID = db.Column(db.Integer, db.ForeignKey('createCourses.courseID'))

    #inheritance relationship with CreateStaff
    #dependent on CreateCourse

    
    def __init__(self, tutorID, staff_id, courseID, course_manager: CreateCourses):
        self.tutorID = tutorID
        self.courseID = courseID
        super().__init__(staff_id)
        self.course_manager = course_manager  # Dependency on CreateCourses
    '''
    def assign_tutor(self):
        # Dependency on CreateCourses to validate course
        valid_course = self.course_manager.get_course(self.courseID)
        
        if valid_course:
            return f"Lecture '{self.courseID}' assigned to {self.staff_id} ."
        else:
            return f"Course '{self.staff_id}' does not exist. Cannot assign lecture."
    '''
    def get_json(self):
        return{
            'tutorID': self.tutorID,
            'courseID': self.courseID
        }
'''
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
'''
