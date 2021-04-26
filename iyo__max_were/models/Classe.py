from odoo import api, fields, models


class Classe(models.Model):
    _name = 'iyo__max_were.classe'

    name = fields.Char(string='Num de Classe')
