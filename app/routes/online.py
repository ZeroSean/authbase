from ..base import base
from ..models import OnLine
from flask import render_template, request, jsonify

@base.route('/securityJsp/base/Syonline.jsp', methods=['GET'])
def index_online():
    return render_template('online/index.html')

@base.route('/base/syonline!grid.action', methods=['POST'])
def grid_online():
    page = request.form.get('page', 1, type=int)
    rows = request.form.get('rows', 10, type=int)
    pagination = OnLine.query.paginate(
        page, per_page=rows, error_out=False)
    onlines = pagination.items

    return jsonify({'total': OnLine.query.count(), 'rows': [online.to_json() for online in onlines]})