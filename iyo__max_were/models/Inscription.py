from odoo import api, fields, models

class Inscription(models.Model):
    _name = 'iyo__max_were.inscription'
    
    stagiaire = fields.Many2one(comodel_name='iyo__max_were.stagiaire', string='stagiaire')
    modules = fields.Many2many(comodel_name='iyo__max_were.module', string='modules')
    _sql_constraints = [('UQ_stagiaire', 'unique(stagiaire)', 'Ce Stagiaire déjà inscrire!'),]
    
