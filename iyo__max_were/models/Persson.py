from odoo import api, fields, models

class Persson(models.Model):
    _name = 'iyo__max_were.persson'

    name = fields.Char(string='Nom')
    prenom = fields.Char(string='Prenom')
    date_naiss = fields.Date(string='Date Naissance')
    adresse = fields.Text(string='Adresse')
    tele = fields.Char(string='Telephone')
    sexe = fields.Selection(string='Sexe', selection=[('F', 'Femme'), ('H', 'Homme'),])
    