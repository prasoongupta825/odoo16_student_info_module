from odoo import models, fields

class StudentRollNumberSequence(models.Model):
    _name = 'student.roll.number.sequence'
    _description = 'Student Roll Number Sequence'

    name = fields.Char(string='Name')

    def next_by_code(self, code):
        sequence = self.env['ir.sequence'].sudo().search([('code', '=', code)])
        next_number = sequence._next()
        parts = next_number.split('-')
        if len(parts) >= 3 and parts[2].isdigit():
            formatted_sequence = f"{parts[0]}-{parts[1]}-{int(parts[2]):03d}"
        else:
            formatted_sequence = next_number
        return formatted_sequence
