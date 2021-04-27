from odoo import api, fields, models

class Module(models.Model):
    _name = 'iyo__max_were.module'

    name = fields.Char(string='Nom de Module',required=True)
    masse_H = fields.Float(string='Nembre d`heurs',required=True)    
    n_max_Stagiaire = fields.Integer(string='Numbre max de stagiaire',required=True)
    prix = fields.Float(string='Prix',required=True)
    
    
    _sql_constraints = [('UQ_module', 'unique(name,prix)', 'Ce module déjà existe'),]
    # ,masse_H,prix