from odoo import models , fields 

class WardModel(models.Model):
    
    _name = 'hms.ward'
    
    name = fields.Char(string="ward name" , required=True)
    resposible =  fields.Many2one('hms.doctor',required=True)
    patients_ids = fields.One2many('hms.patient','locate')
    nurses = fields.Many2many('hms.nurse')   