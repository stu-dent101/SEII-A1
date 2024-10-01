#from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class CreateCourses(db.Model):
    __tablename__ = 'createCourses'
    courseID = db.Column(db.String(20), primary_key=True, unique=True)
    courseName =  db.Column(db.String(20), nullable=False)
    
    def __init__(self, courseID, courseName):
        self.courseID = courseID
        self.courseName = courseName

    def get_json(self):
        return{
            'courseID': self.courseID,
            'courseName': self.courseName,
        }
    
    def createCourse(self, courseName, courseID):
        try:
            new_course = CreateCourses(courseName=courseName, courseID=courseID)
            self.createCourses.append(new_course)
            db.session.add(new_course)
            db.session.commit()
            print(f"Course Created")
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error creating course: {e}")
            return False
    
    def get_course(courseID):
        return CreateCourses.query.get(courseID)

'''
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
'''
