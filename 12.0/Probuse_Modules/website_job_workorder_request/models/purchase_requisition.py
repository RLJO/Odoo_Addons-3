# -*- coding: utf-8 -*-

from odoo import fields, models, api

class MaterialPurchaseRequisition(models.Model):
    _inherit = 'material.purchase.requisition'
    
    joborder_id = fields.Many2one(
        'project.task',
        string='Job Order',
    )
    project_id = fields.Many2one(
        'project.project',
        string='Project',
    )
    
    
    @api.onchange('joborder_id')
    def _set_project(self):
        for rec in self:
            rec.project_id = rec.joborder_id.project_id.id
            
    @api.onchange('project_id')
    def _set_analytic_account(self):
        for rec in self:
            rec.analytic_account_id = rec.project_id.analytic_account_id.id

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
