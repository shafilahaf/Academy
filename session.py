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
    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats', store=False)


    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats