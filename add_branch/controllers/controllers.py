# -*- coding: utf-8 -*-
# from odoo import http


# class AddBranch(http.Controller):
#     @http.route('/add_branch/add_branch', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/add_branch/add_branch/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('add_branch.listing', {
#             'root': '/add_branch/add_branch',
#             'objects': http.request.env['add_branch.add_branch'].search([]),
#         })

#     @http.route('/add_branch/add_branch/objects/<model("add_branch.add_branch"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('add_branch.object', {
#             'object': obj
#         })
