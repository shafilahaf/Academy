from odoo import models, fields, api

class attendee(models.Model):
    _name = 'academic.attendee'

    session_id = fields.Many2one('academic.session', 'Session')
    partner_id = fields.Many2one('res.partner', 'Partner')
    name=fields.Char('Name', size=100)