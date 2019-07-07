# coding:utf-8
from ..base import base
from ..models import Role, Resource, User
from flask import render_template, request
from flask_login import current_user
from flask import jsonify
from datetime import datetime
from .. import  db
import uuid

@base.route('/securityJsp/base/Syrole.jsp', methods=['GET'])
def index_role():
    return render_template('role/index.html')

@base.route('/securityJsp/base/SyroleForm.jsp', methods=['GET'])
def form_role():
    return render_template('role/form.html', id=request.args.get('id', ''))


@base.route('/securityJsp/base/SyroleGrant.jsp', methods=['GET'])
def grant_role_page():
    return render_template('role/grant.html', id=request.args.get('id', ''))

@base.route('/base/syrole!doNotNeedSecurity_getRolesTree.action', methods=['POST'])
def get_roles_tree():
    roles = Role.query.join(User, Role.users).filter(User.ID == current_user.ID).all()
    return jsonify([role.to_json() for role in roles])

@base.route('/base/syrole!doNotNeedSecurity_getRoleByUserId.action', methods=['POST'])
def get_roles_by_userId():
    roles = Role.query.join(User, Role.users).filter(User.ID == request.form.get('id')).all()
    return jsonify([role.to_json() for role in roles])


@base.route('/base/syrole!grant.action', methods=['POST'])
def grant_role():
    id = request.form.get('id')
    ids = request.form.get('ids')

    role = Role.query.get(id)

    if not ids: #授权资源为空
        role.resources = []
    else:       #授权资源访问，资源之间以逗号分割
        idList = ids.split(',')
        role.resources = [Resource.query.get(rid) for rid in idList]

    db.session.add(role)

    return jsonify({'success': True})

@base.route('/base/syrole!grid.action', methods=['POST'])
def grid():
    page = request.form.get('page', 1, type=int)
    rows = request.form.get('rows', 10, type=int)
    pagination = current_user.roles.paginate(
        page, per_page=rows, error_out=False)
    roles = pagination.items

    return jsonify([role.to_json() for role in roles])

@base.route('/base/syrole!getById.action', methods=['POST'])
def syrole_getById():
    role = Role.query.get(request.form.get('id'))

    if role:
        return jsonify(role.to_json())
    else:
        return jsonify({'success': False, 'msg': 'error'})

@base.route('/base/syrole!update.action', methods=['POST'])
def syrole_update():
    role = Role.query.get(request.form.get('data.id'))

    role.UPDATEDATETIME = datetime.now()
    role.NAME = request.form.get('data.name')
    role.DESCRIPTION = request.form.get('data.description')
    role.SEQ = request.form.get('data.seq')

    db.session.add(role)

    return jsonify({'success': True})

@base.route('/base/syrole!save.action', methods=['POST'])
def syrole_save():
    role = Role()

    role.ID = str(uuid.uuid4())
    role.NAME = request.form.get('data.name')
    role.DESCRIPTION = request.form.get('data.description')
    role.SEQ = request.form.get('data.seq')

    # add current use to new role
    current_user.roles.append(role)

    db.session.add(role)

    return jsonify({'success': True})

@base.route('/base/syrole!delete.action', methods=['POST'])
def syrole_delete():
    role = Role.query.get(request.form.get('id'))
    if role:
        db.session.delete(role)

    return jsonify({'success': True})