#from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class AdminAssignment(db.Model):
    __tablename__ = 'adminAssignment'
    adminAssignmentID = db.Column(db.Integer, primary_key=True, unique=True)
    adminID = db.Column(db.Integer, db.ForeignKey('administrator.adminID'))
    assignmentID = db.Column(db.Integer, db.ForeignKey('assignStaff.assignmentID'))
    
    def __init__(self, adminAssignmentID, adminID, assignmentID):
        self.adminAssignmentID = adminAssignmentID
        self.adminID = adminID
        self.assignmentID = assignmentID
        
    def get_json(self):
        return{
            'adminAssignmentID': self.adminAssignmentID,
            'adminID': self.adminID,
            'assignmentID': self.assignmentID
        }
    
    '''
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
    '''

