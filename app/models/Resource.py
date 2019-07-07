from app import db
from flask_login import UserMixin, AnonymousUserMixin
from datetime import datetime
from flask import jsonify


class Resource(db.Model, UserMixin):
    __tablename__ = 'SYRESOURCE'
    ID = db.Column(db.String(36), primary_key=True)
    CREATEDATETIME = db.Column(db.DateTime, index=True, default=datetime.now)
    UPDATEDATETIME = db.Column(db.DateTime, index=True, default=datetime.now)
    NAME = db.Column(db.String(100))
    URL = db.Column(db.String(200))
    DESCRIPTION = db.Column(db.String(200))
    ICONCLS = db.Column(db.String(100))
    SEQ = db.Column(db.Integer)
    TARGET = db.Column(db.String(100))

    SYRESOURCETYPE_ID = db.Column(db.String, db.ForeignKey('SYRESOURCETYPE.ID'))

    SYRESOURCE_ID = db.Column(db.String, db.ForeignKey('SYRESOURCE.ID'))

    parent = db.relationship('Resource', remote_side=[ID], backref='resource', uselist=False)

    def get_id(self):
        return str(self.ID)

    def to_json(self):
        return {
            'id': self.ID,
            'createdatetime': self.CREATEDATETIME,
            'updatedatetime': self.UPDATEDATETIME,
            'name': self.NAME,
            'url': self.URL,
            'description': self.DESCRIPTION,
            'iconCls': self.ICONCLS,
            'seq': self.SEQ,
            'target': self.TARGET,
            'pid': self.get_pid(),
            'syresourcetype': self.get_type_json()
        }

    def to_menu_json(self):
        return {
            'id': self.ID,
            'iconCls': self.ICONCLS,
            'pid': self.get_pid(),
            'state': 'open',
            'checked': False,
            'attributes': {
                'target': self.TARGET,
                'url': self.URL
            },
            'text': self.NAME
        }

    def get_pid(self):
        if self.parent:
            return self.parent.ID
        return ''

    def get_type_json(self):
        if self.type:
            return self.type.to_json()
        return {}

    def __repr__(self):
        return '<Resource name:%r url:%r>\n' %(self.NAME, self.URL)