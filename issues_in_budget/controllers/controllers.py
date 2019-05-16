# -*- coding: utf-8 -*-
from odoo import http

# class IssuesInBudget(http.Controller):
#     @http.route('/issues_in_budget/issues_in_budget/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/issues_in_budget/issues_in_budget/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('issues_in_budget.listing', {
#             'root': '/issues_in_budget/issues_in_budget',
#             'objects': http.request.env['issues_in_budget.issues_in_budget'].search([]),
#         })

#     @http.route('/issues_in_budget/issues_in_budget/objects/<model("issues_in_budget.issues_in_budget"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('issues_in_budget.object', {
#             'object': obj
#         })