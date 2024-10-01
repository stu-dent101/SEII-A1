from App.models import ViewCourseStaff
from App.database import db

def create_View(staffCount, staffID, courseID, fName, lName, position):
    newView = ViewCourseStaff(staffCount = staffCount, staffID = staffID, courseID = courseID, fName = fName, lName = lName, position = position)
    db.session.add(newView)
    db.session.commit()
    return newView

def get_staff_by_ID(staffID):
    return ViewCourseStaff.query.filter_by(staffID = staffID).first()

def get_user(staffID):
    return ViewCourseStaff.query.get(staffID)

def get_all_staff():
    return ViewCourseStaff.query.all()

def get_all_staffMembers_json():
    staffMembers = ViewCourseStaff.query.all()
    if not staffMembers:
        return []
    staffMembers= [staff.get_json() for staff in staffMembers]
    return staffMembers

'''
def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    '''