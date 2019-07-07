from ..base import base
from flask import render_template
from flask_login import login_user, logout_user, login_required, \
    current_user

@base.route('/')
@login_required
def index():
    return render_template('index.html')


@base.route('/base/north', methods=['POST'])
@login_required
def north():
    return render_template('layout/north.html')

@base.route('/base/west', methods=['POST'])
@login_required
def west():
    return render_template('layout/west.html')

@base.route('/base/south', methods=['POST'])
@login_required
def south():
    return render_template('layout/south.html')

@base.route('/style/icons.jsp')
def icons():
    return render_template('icons/icons.html')
