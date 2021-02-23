from odoo import models, fields, api

class attendee(models.Model):
    _name = 'academic.attendee'

    session_id = fields.Many2one('academic.session', 'Session')
    partner_id = fields.Many2one('res.partner', 'Partner')
    name=fields.Char('Name', size=100)

    _sql_constraints = [
        ('partner_session_unique',
         'UNIQUE(partner_id,session_id )',
         "You cannot insert the same attendee multiple times!"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
        ]