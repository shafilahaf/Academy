from odoo import models, fields, api

class session(models.Model):
    _name = 'academic.session'

    course_id = fields.Many2one('academic.course', 'Course')
    instructor_id = fields.Many2one('res.partner', 'Instructor')
    name = fields.Char('Name', size=100, required=True)
    start_date = fields.Date('Start Date', required=True)
    duration = fields.Integer('Duration')
    seats = fields.Integer('Number of Seats')
    active = fields.Boolean('Is Active?')
    attendee_ids = fields.One2many('academic.attendee', 'session_id', 'Attendess', ondelete="cascade")