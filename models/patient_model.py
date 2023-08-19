from odoo import models , fields , api
from odoo.exceptions import ValidationError 
from datetime import datetime
class DoctorModel(models.Model):
    _name='hms.patient'
    _rec_name = 'first_name' 
    
    first_name = fields.Char(string="first name",required=True)
    last_name = fields.Char(string="last name",required=True)
    email = fields.Char(string="email",required=True)
    description = fields.Text(string="description",required=True)
    birthdate = fields.Date(required=True)
    phone_number = fields.Char(string="phone number",required=True)
    charge = fields.Many2one('hms.nurse')
    
    avatar = fields.Image()
    gender = fields.Selection(
        [
            ('male','Male'),
            ('female','Female')
        ],
        required=True
    )
    
        # computed age
    age = fields.Integer(compute='computed_tourist_age')
    @api.depends('birthdate')
    def computed_tourist_age(self):
        for record in self :
            if record.birthdate:
                record.age = datetime.now().year - record.birthdate.year
            else :
                record.age = 0
    
    state = fields.Selection(
        [
            ('well','Well'),
            ('heal','Heal'),
            ('serious','Serious')
        ]
        ,required=True
    )
    locate =  fields.Many2one('hms.ward')
    
    _sql_constraints = [
        ('unique_email','UNIQUE(email)','email is already existed'),
        ('unique_number','UNIQUE(phone_number)','phone number is already existed'),    
        ]
    @api.constrains('email')
    def email_validation(self):
        for record in self :
            if record.email:
                if '@' not in record.email :
                    raise ValidationError('please enter valid email')
    
    @api.constrains('phone_number')
    def phone_number_validation(self):
        for record in self :
            if record.phone_number:
                if not record.phone_number.isnumeric():
                        raise ValidationError('phone number must be numeric')
                elif len(record.phone_number) != 11 and record.phone_number[0] != 0 :
                        raise ValidationError('please enter valid phone number ')