from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError

class session(models.Model):
    _name = 'academic.session'


    course_id = fields.Many2one('academic.course', 'Course')
    instructor_id = fields.Many2one('res.partner', 'Instructor')
    name = fields.Char('Name', size=100, required=True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Integer('Duration')
    seats = fields.Integer('Number of Seats')
    active = fields.Boolean(default=True)
    attendee_ids = fields.One2many('academic.attendee', 'session_id', 'Attendess', ondelete="cascade")
    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats', store=False)


    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats


    #The “onchange” mechanism provides a way for the client interface to 
    # update a form whenever the user has filled in a value in a field, 
    # without saving anything to the database.


    #change the number of seats or participants,
    # and the taken_seats progressbar is automatically updated.

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "The number of available seats may not be negative",
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase seats or remove excess attendees",
                },
            }

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
        ]


    #A Python constraint is defined as a method decorated with constrains(),
    # and invoked on a recordset.

    #Add a constraint that checks that the instructor is not present in the attendees of his/her own session.

    #@api.constrains('instructor_id', 'attendee_ids')
    #def _check_instructor_not_in_attendees(self):
     #  for r in self:
      #      if r.instructor_id and r.instructor_id in r.attendee_ids:
       #          raise exceptions.ValidationError("A session's instructor can't be an attendee")