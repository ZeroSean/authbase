from ..base import base
from ..models import Resource
from ..models import Role
from ..models import User
from ..models import Organization
from flask import g, jsonify, request
from flask_login import current_user
import json
from .. import db
from flask import render_template
from datetime import datetime
import uuid

@base.route('/securityJsp/base/Syorganization.jsp', methods=['GET'])
def index_organization():
    return render_template('organization/index.html')

@base.route('/securityJsp/base/SyorganizationForm.jsp', methods=['GET'])
def form_organization():
    return render_template('organization/form.html', id=request.args.get('id', ''))

@base.route('/securityJsp/base/SyorganizationGrant.jsp', methods=['GET'])
def grant_organization_resource_page():
    return render_template('organization/grant.html', id=request.args.get('id', ''))    

@base.route('/base/syorganization!grant.action', methods=['POST'])
def grant_organization_resource():
    id = request.form.get('id')
    ids = request.form.get('ids')

    org = Organization.query.get(id)

    if not ids:
        org.resources = []
    else:
        idList = ids.split(',')
        org.resources = [Resource.query.get(rid) for rid in idList]

    db.session.add(org)

    return jsonify({'success': True})    

@base.route('/base/syorganization!treeGrid.action', methods=['POST'])
def syorganization_treeGrid():
    orgs = Organization.query.all()

    return jsonify([org.to_json() for org in orgs])

@base.route('/base/syorganization!doNotNeedSecurity_comboTree.action', methods=['POST'])
def syorganization_comboTree():
    orgs = Organization.query.all()

    return jsonify([org.to_json() for org in orgs])


@base.route('/base/syorganization!doNotNeedSecurity_getSyorganizationsTree.action', methods=['POST'])
def get_syorganizations_tree():
    orgs = Organization.query.join(User, Organization.users).filter(User.ID == current_user.ID).all()
    return jsonify([org.to_json() for org in orgs])

@base.route('/base/syorganization!doNotNeedSecurity_getSyorganizationByUserId.action', methods=['POST'])
def get_syorganization_by_userId():
    orgs = Organization.query.join(User, Organization.users).filter(User.ID == request.form.get('id')).all()
    return jsonify([org.to_json() for org in orgs])

@base.route('/base/syorganization!getById.action', methods=['POST'])
def syorganization_getById():
    org = Organization.query.get(request.form.get('id'))

    if org:
        return jsonify(org.to_json())
    else:
        return jsonify({'success': False, 'msg': 'error'})

@base.route('/base/syorganization!update.action', methods=['POST'])
def syorganization_update():
    org = Organization.query.get(request.form.get('data.id'))

    org.UPDATEDATETIME = datetime.now()
    org.NAME = request.form.get('data.name')
    org.ADDRESS = request.form.get('data.address')
    org.CODE = request.form.get('data.code')
    org.ICONCLS = request.form.get('data.iconCls')
    org.SEQ = request.form.get('data.seq')
    org.parent = Organization.query.get(request.form.get('data.syorganization.id'))

    db.session.add(org)

    return jsonify({'success': True})

@base.route('/base/syorganization!save.action', methods=['POST'])
def syorganization_save():
    org = Organization()
    org.ID = str(uuid.uuid4())
    org.NAME = request.form.get('data.name')
    org.ADDRESS = request.form.get('data.address')
    org.CODE = request.form.get('data.code')
    org.ICONCLS = request.form.get('data.iconCls')
    org.SEQ = request.form.get('data.seq')
    org.parent = Organization.query.get(request.form.get('data.syorganization.id'))

    # add organization to current user
    current_user.organizations.append(org)

    db.session.add(org)

    return jsonify({'success': True})

@base.route('/base/syorganization!delete.action', methods=['POST'])
def syorganization_delete():
    org = Organization.query.get(request.form.get('id'))
    if org:
        db.session.delete(org)

    return jsonify({'success': True})
