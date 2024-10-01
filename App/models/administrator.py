#from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from App.models import adminCreateCourses

class Administrator(db.Model):
    __tablename__ = 'administrator'
    adminID = db.Column(db.Integer, primary_key=True, unique=True)
    staffID = db.Column(db.Integer, db.ForeignKey('createStaff.staffID'))
    fName =  db.Column(db.String(20), nullable=False)
    lName = db.Column(db.String(20), nullable=False)
    adminCourses = db.relationship('CreateCourses', secondary = "adminCreateCourses", backref=db.backref('administrator', lazy=True))
    view = db.relationship('ViewCourseStaff', secondary = "adminViewCourseStaff", backref=db.backref('administrator', lazy=True))
    assign = db.relationship('AssignStaff', secondary = "adminAssignment", backref=db.backref('administrator', lazy=True))
    createStaff = db.relationship('CreateStaff', secondary = "adminCreateStaff", backref=db.backref('administrator', lazy=True))


    def __init__(self, adminID, staffID, fName, lName):
        self.adminID = adminID
        self.staffID = staffID
        self.fName = fName
        self.lName = lName

    def get_json(self):
        return{
            'adminID': self.adminID,
            'staffID': self.staffID,
            'First Name': self.fName,
            'Last Name': self.lName
        }
    
    '''
    def createCourse(self, courseName, courseCode):
        try:
            new_course = CreateCourses(courseName=courseName, courseCode=courseCode)
            self.createCourses.append(new_course)
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

