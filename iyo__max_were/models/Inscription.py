from odoo import api, fields, models

class Inscription(models.Model):
    _name = 'iyo__max_were.inscription'
    
    stagiaire = fields.Many2one(comodel_name='iyo__max_were.stagiaire', string='Nom de stagiaire',required=True)
    name = fields.Char(string='Prenom de stagiaire',related='stagiaire.name')
    prenom = fields.Char(string='Prenom de stagiaire',related='stagiaire.prenom')
    tele = fields.Char(string='Telephone',related='stagiaire.tele')
    modules = fields.Many2many(comodel_name='iyo__max_were.module', string='modules',required=True)
    
    _sql_constraints = [('UQ_stagiaire', 'unique(stagiaire)', 'Ce Stagiaire déjà inscrire!'),]
    
