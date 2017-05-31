
from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers
from skf.api.checklist.business import get_checklist_items_lvl
from skf.api.checklist.serializers import checklist, level, message
from skf.api.restplus import api

ns = api.namespace('checklist', description='Operations related to checklist items')


@ns.route('/level')
@api.response(404, 'Validation error')
class ChecklistItem(Resource):

    @api.expect(level)
    @api.marshal_list_with(checklist)
    @api.response(400, 'No results found', message)
    def post(self):
        """
        Returns list of checklist items based on level.
        * Privileges required: **none**
        """
        data = request.json
        lvl = data.get('level')
        result = get_checklist_items_lvl(lvl)
        return result, 200, security_headers()
                