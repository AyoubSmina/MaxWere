from odoo import api, fields, models

class Seance(models.Model):
    _name = 'iyo__max_were.seance'

    # name = fields.Char(string='')
    date_debut = fields.Datetime(string='Date Début')
    date_fin = fields.Datetime(string='Date Fin')
    
    id_formateur = fields.Many2one(comodel_name='iyo__max_were.formateur', string='Formateur')
    id_module = fields.Many2many(comodel_name='iyo__max_were.module', string='module')
