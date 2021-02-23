from odoo import models, fields, api

class course(models.Model):
	_name = 'academic.course'

	name = fields.Char('Name', size=100, required=True)
	description = fields.Text('Description')
	responsible_id = fields.Many2one('res.users', string="Responsible")
	session_ids = fields.One2many ('academic.session', 'course_id', 'Sessions', ondelete="cascade")
