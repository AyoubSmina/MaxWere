# -*- coding: utf-8 -*-
# from odoo import http


# class IyoMaxWere(http.Controller):
#     @http.route('/iyo__max_were/iyo__max_were/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/iyo__max_were/iyo__max_were/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('iyo__max_were.listing', {
#             'root': '/iyo__max_were/iyo__max_were',
#             'objects': http.request.env['iyo__max_were.iyo__max_were'].search([]),
#         })

#     @http.route('/iyo__max_were/iyo__max_were/objects/<model("iyo__max_were.iyo__max_were"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('iyo__max_were.object', {
#             'object': obj
#         })
