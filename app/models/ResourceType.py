from app import db
from flask_login import UserMixin, AnonymousUserMixin
from datetime import datetime


class ResourceType(db.Model, UserMixin):
    __tablename__ = 'SYRESOURCETYPE'
    ID = db.Column(db.String(36), primary_key=True)
    CREATEDATETIME = db.Column(db.DateTime, index=True, default=datetime.now)
    UPDATEDATETIME = db.Column(db.DateTime, index=True, default=datetime.now)
    NAME = db.Column(db.String(100))
    DESCRIPTION = db.Column(db.String(200))

    resources = db.relationship('Resource', backref='type', lazy='dynamic')

    def to_json(self):
        return {
            'id': self.ID,
            'createdatetime': self.CREATEDATETIME,
            'updatedatetime': self.UPDATEDATETIME,
            'name': self.NAME,
            'description': self.DESCRIPTION
        }

    def __repr__(self):
        return '<ResourceType %r>\n' %(self.NAME)