from odoo import models , fields , api

class UserCustomize(models.Model):
    name = 'mohammed'
    first_name = fields.Char(string="first name",required=True)
    last_name = fields.Char(string="last name",required=True)
    email = fields.Char(string="email",required=True)
    description = fields.Text(string="first name",required=True)
    birthdate = fields.Date()
    avatar = fields.Image()
    gender = fields.Selection(
        [
            ('male','Male'),
            ('female','Female')
        ]
    )
    
        # computed age
    age = fields.Integer(compute='computed_tourist_age')
    @api.depends('birthdate')
    def computed_tourist_age(self):
        for record in self :
            if record.birthdate:
                record.computed_age = datetime.now().year - record.birthdate.year
            else :
                record.computed_age = 0
