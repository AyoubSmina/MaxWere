from odoo import api, fields, models

class Module(models.Model):
    _name = 'iyo__max_were.module'

    name = fields.Char(string='Nom de Module')
    masse_H = fields.Float(string='Nembre d`heurs')    
    n_max_Stagiaire = fields.Integer(string='Numbre max de stagiaire')
    prix = fields.Float(string='Prix')

    _sql_constraints = [('UQ_module', 'unique(name,masse_H,n_max_Stagiaire,prix)', 'Ce module déjà existe'),]
