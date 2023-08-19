from odoo import models , fields , api
from odoo.exceptions import ValidationError 
from datetime import datetime
class NurseModel(models.Model):
    _name='hms.nurse'
    _rec_name = 'first_name' 
    
    first_name = fields.Char(string="first name",required=True)
    last_name = fields.Char(string="last name",required=True)
    email = fields.Char(string="email",required=True)
    description = fields.Text(string="description",required=True)
    birthdate = fields.Date(required=True)
    avatar = fields.Image()
    phone_number = fields.Char(string="phone number",required=True)
    shift = fields.Selection(
        string='',
        selection=[('day', 'Day'), ('night', 'Night')]
        ,required=True
    )
    gender = fields.Selection(
        [
            ('male','Male'),
            ('female','Female')
        ],required=True
    )
    
        # computed age
    age = fields.Integer(compute='computed_tourist_age')
    wards =  fields.Many2many('hms.ward')
    res_patients =  fields.One2many('hms.patient' , 'charge')
    
    @api.depends('birthdate')
    def computed_tourist_age(self):
        for record in self :
            if record.birthdate:
                record.age = datetime.now().year - record.birthdate.year
                if record.age <  20 :
                    raise ValidationError('nurse can not be little like that ! ')
            else :
                record.age = 0
    
   
    words_ids = fields.One2many('hms.ward','resposible')
    _sql_constraints = [
        ('unique_email','UNIQUE(email)','email is already existed'),
        ('unique_number','UNIQUE(phone_number)','phone number is already existed'),    
        ]
    # validate email
    @api.constrains('email')
    def email_validation(self):
        for record in self :
            if record.email:
                if '@' not in record.email :
                    raise ValidationError('please enter valid email')
    # validate phone number
    @api.constrains('phone_number')
    def phone_number_validation(self):
        for record in self :
            if record.phone_number:
                if not record.phone_number.isnumeric():
                        raise ValidationError('phone number must be numeric')
                elif len(record.phone_number) != 11 and record.phone_number[0] != 0 :
                        raise ValidationError('please enter valid phone number ')