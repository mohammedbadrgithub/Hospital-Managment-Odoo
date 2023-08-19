from odoo import models , fields 

class SpecilizeModel(models.Model):
    
    _name = 'hms.specilize'
    
    name = fields.Char(string="specilize name" , required=True)
    doctors_ids = fields.One2many('hms.doctor','specilize')