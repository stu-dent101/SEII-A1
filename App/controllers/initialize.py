from .user import create_user

from .administrator import create_admin
#from .assignStaff import ...
from .createCourses import create_newCourse
from .createStaff import create_staff
from .lecture import create_lecturer
from .teachingAssistant import create_TA
from .tutor import create_tutor
from .adminAssignment import create_adminAssignment
from .adminCreateStaff import create_adminCreateStaff
from .viewCourseStaff import create_View
from .adminCreateCourses import create_adminCreateCourses
from App.database import db

def initialize():
    db.drop_all()
    db.create_all()
    #create_user('bob', 'bobpass')
    
def initializeAdmin():
    db.drop_all()
    db.create_all()
    create_admin('654', '789', 'Sam', 'Apple')

def initializeNewCourse():
    db.drop_all()
    db.create_all()
    create_newCourse('456', 'courseName')

def initializeNewStaff():
    db.drop_all()
    db.create_all()
    create_staff('321', 'Jame', 'Brown', 'lecture')

def initializeLecturer():
    db.drop_all()
    db.create_all()
    create_lecturer('123', 'COMP 0000')

def initializeTA():
    db.drop_all()
    db.create_all()
    create_TA('147', 'COMP 0000')

def initializeTutor():
    db.drop_all()
    db.create_all()
    create_tutor('258', 'COMP 000')

def initializeAdminAssignment():
    db.drop_all()
    db.create_all()
    create_adminAssignment('369', '963', '753')

def initializeAdminCreateStaff():
    db.drop_all()
    db.create_all()
    create_adminCreateStaff('357', '739', '397')

def initializeView():
    db.drop_all()
    db.create_all()
    create_View('1', '951', 'COMP 0000', 'Sam', 'Purple', 'position')

def initializeAdminCreateCourses():
    db.drop_all()
    db.create_all()
    create_adminCreateCourses('1', 'COMP 0000', '483')