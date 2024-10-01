#from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class CreateStaff(db.Model):
    __tablename__ = 'createStaff'
    staffID = db.Column(db.Integer, primary_key=True, unique=True)
    fName =  db.Column(db.String(20), nullable=False)
    lName =  db.Column(db.String(20), nullable=False)
    position =  db.Column(db.String(20), nullable=False)

    def __init__(self, staffID, fName, lName, position):
        self.staffID = staffID
        self.fName = fName
        self.lName = lName
        self.position = position

    def get_json(self): 
        return{
            'staffID': self.staffID,
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
