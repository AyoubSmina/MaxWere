from odoo import api, fields, models

class Persson(models.Model):
    _name = 'iyo__max_were.formateur'
    _inherit = "iyo__max_were.persson"
    
    cin = fields.Char(string='CIN',required=True)
    # module = fields.Many2one('iyo__max_were.module', string='Module qui enseigne',ondelete='set null',index=True)module
    module = fields.Many2many(comodel_name='iyo__max_were.module', string='Module qui enseigne',required=True)
    image = fields.Binary()
    
  
