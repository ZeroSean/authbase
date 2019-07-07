#!/usr/bin/env python  
import os
from app import create_app, db
from app.models import User, Role, Resource, ResourceType, Organization
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask import g, render_template

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

with app.app_context():
    g.contextPath = ''

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Resource=Resource,
                ResourceType=ResourceType, Organization=Organization)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def myprint():
    print('hello world')


if __name__ == '__main__':
    manager.run()
