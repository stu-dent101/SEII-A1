#from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class AdminCreateStaff(db.Model):
    __tablename__ = 'adminCreateStaff'
    adminCSID = db.Column(db.Integer, primary_key=True, unique=True)
    adminID = db.Column(db.Integer, db.ForeignKey('administrator.adminID'))
    staffID = db.Column(db.Integer, db.ForeignKey('createStaff.staffID'))

    def __init__(self, adminCSID, adminID, staffID):
        self.adminCSID = adminCSID
        self.adminID = adminID
        self.staffID = staffID
        
    def get_json(self):
        return{
            'adminCSID': self.adminCSID,
            'adminID': self.adminID,
            'staffID': self.staffID
        }
    
    '''
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
    '''

