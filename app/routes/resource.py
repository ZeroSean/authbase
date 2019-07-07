from ..base import base
from ..models import Resource, Organization
from ..models import Role
from ..models import User
from flask import g, jsonify
from flask_login import current_user
import json
from ..models import ResourceType
from flask import render_template, request
from .. import  db
import uuid
from datetime import datetime

@base.route('/base/syresource!doNotNeedSecurity_getMainMenu.action', methods=['POST'])
def resource_grid():
    rs = Resource.query.join(Role, Resource.roles).join(User, Role.users).filter(User.ID == current_user.ID).all()

    return jsonify([r.to_menu_json() for r in rs])


@base.route('/base/syresourcetype!doNotNeedSecurity_combobox.action', methods=['POST'])
def resource_type_combox():
    rt = ResourceType.query.all()
    return jsonify([r.to_json() for r in rt])

@base.route('/securityJsp/base/Syresource.jsp', methods=['GET'])
def index_resource():
    return render_template('resource/index.html')

@base.route('/securityJsp/base/SyresourceForm.jsp', methods=['GET'])
def form_resource():
    return render_template('resource/form.html', id=request.args.get('id', ''))


@base.route('/base/syresource!doNotNeedSecurity_getRoleResources.action', methods=['POST'])
def get_role_resources():
    resources = Resource.query.join(Role, Resource.roles).filter(Role.ID == request.form.get('id')).all()
    return jsonify([res.to_json() for res in resources])


@base.route('/base/syresource!doNotNeedSecurity_getResourcesTree.action', methods=['POST'])
def get_resources_tree():
    return syresource_treeGrid()

@base.route('/base/syresource!doNotNeedSecurity_getOrganizationResources.action', methods=['POST'])
def get_organization_resources():
    resources = Resource.query.join(Organization, Resource.organizations).filter(Organization.ID == request.form.get('id')).all()
    return jsonify([res.to_json() for res in resources])    

@base.route('/base/syresource!treeGrid.action', methods=['POST'])
def syresource_treeGrid():
    res_list = Resource.query.all()

    return jsonify([org.to_json() for org in res_list])

@base.route('/base/syresource!doNotNeedSecurity_comboTree.action', methods=['POST'])
def syresource_comboTree():
    res_list = Resource.query.all()

    return jsonify([org.to_json() for org in res_list])

@base.route('/base/syresource!getById.action', methods=['POST'])
def syresource_getById():
    res = Resource.query.get(request.form.get('id'))

    if res:
        return jsonify(res.to_json())
    else:
        return jsonify({'success': False, 'msg': 'error'})

@base.route('/base/syresource!update.action', methods=['POST'])
def syresource_update():
    res = Resource.query.get(request.form.get('data.id'))

    res.UPDATEDATETIME = datetime.now()
    res.NAME = request.form.get('data.name')
    res.URL = request.form.get('data.url')
    res.DESCRIPTION = request.form.get('data.description')
    res.ICONCLS = request.form.get('data.iconCls')
    res.SEQ = request.form.get('data.seq')
    res.TARGET = request.form.get('data.target')
    res.SYRESOURCETYPE_ID = request.form.get('data.syresourcetype.id')
    res.parent = Resource.query.get(request.form.get('data.syresource.id'))

    db.session.add(res)

    return jsonify({'success': True})

@base.route('/base/syresource!save.action', methods=['POST'])
def syresource_save():
    res = Resource()

    res.ID = str(uuid.uuid4())
    res.NAME = request.form.get('data.name')
    res.URL = request.form.get('data.url')
    res.DESCRIPTION = request.form.get('data.description')
    res.ICONCLS = request.form.get('data.iconCls')
    res.SEQ = request.form.get('data.seq')
    res.TARGET = request.form.get('data.target')
    res.SYRESOURCETYPE_ID = request.form.get('data.syresourcetype.id')
    res.parent = Resource.query.get(request.form.get('data.syresource.id'))

    db.session.add(res)

    return jsonify({'success': True})

@base.route('/base/syresource!delete.action', methods=['POST'])
def syresource_delete():
    res = Resource.query.get(request.form.get('id'))
    if res:
        db.session.delete(res)

    return jsonify({'success': True})

