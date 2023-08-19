from odoo import HTTP 
from odoo.http import request
class HospitalDoctors(odoo.http.Controller):
        
        # @http.route('/hospital/doctors/',auth="public", methods=['GET'], website=True ,csrf=False)
        @http.route('ar/api/', auth='public')
        def po_details(self , **kwargs):
            # response = []
            # purchase_details = env['hms.doctor'].sudo().search([])
            # for rec in purchase_details:
            #     response.append({
            #     ‘po_name’:rec.first_name,
            #     ‘po_date’:rec.last_name
            #     })
            # return json.dumps(response) 
            return 'odoo'
        