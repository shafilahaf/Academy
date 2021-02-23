from odoo import models, fields, api

class attendee(models.Model):
    _name = 'academic.attendee'

    session_id = fields.Many2one('academic.session', 'Session')
    partner_id = fields.Many2one('res.partner', 'Partner')
    name=fields.Char('Name', size=100)


    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(attendee, self).copy(default)

    _sql_constraints = [
        ('partner_session_unique',
         'UNIQUE(partner_id,name)',
         "You cannot insert the same attendee multiple times!"),

         ('name_unique',
         'UNIQUE(name)',
         "The Attendee must be different"),
        ]