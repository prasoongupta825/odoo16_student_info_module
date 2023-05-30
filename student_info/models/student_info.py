from odoo import models, fields, api
from . import student_roll_number_sequence
import re


class Student(models.Model):
    _name = 'student.info'
    _description = 'Student Information'

    name = fields.Char(string='Student Name', required=True)
    roll_number = fields.Char(string='Roll Number', readonly=True, default=False)
    father_name = fields.Char(string='Father Name')
    email = fields.Char(string='Email')
    contact_info = fields.Char(string='Contact Info')
    
    # Academic Info
    class_id = fields.Many2one('student.class', string='Class')
    semester = fields.Char(string='Semester')
    section = fields.Char(string='Section')

    # Assessment Info
    assessment_ids = fields.One2many('student.assessment', 'student_id', string='Assessments')

    # Overall Grade
    overall_grade = fields.Char(string='Overall Grade', compute='_compute_overall_grade', store=True)
    total_marks = fields.Float(string='Total Marks', compute='_compute_total_marks', store=True)
    total_percentage = fields.Float(string='Total Percentage', compute='_compute_total_percentage', store=True)

    # Button to assign roll number
    def assign_roll_number(self):
        if not self.roll_number:
            sequence = self.env['student.roll.number.sequence'].next_by_code('student.roll.number')
            if sequence:
                numeric_part = re.sub("[^0-9]", "", sequence)
                formatted_sequence = "{}-{}-{}".format(sequence[:2], sequence[2:4], numeric_part.zfill(3))
                self.roll_number = formatted_sequence


    # Hide the assign_roll_number button if roll number is assigned
    @api.onchange('roll_number')
    def _onchange_roll_number(self):
        if self.roll_number:
            sequence = self.env['student.roll.number.sequence'].sudo().search([('name', '=', 'Student Roll Number Sequence')])
            if sequence:
                sequence.active = False
    
    # Compute overall grade based on assessments
    @api.depends('assessment_ids.grade')
    def _compute_overall_grade(self):
        for student in self:
            if student.assessment_ids:
                grades = [assessment.grade for assessment in student.assessment_ids if assessment.grade]
                student.overall_grade = max(grades) if grades else ''

    # Compute total marks based on assessments
    @api.depends('assessment_ids.total_marks')
    def _compute_total_marks(self):
        for student in self:
            if student.assessment_ids:
                student.total_marks = sum(assessment.total_marks for assessment in student.assessment_ids)

    # Compute total percentage based on assessments
    @api.depends('assessment_ids.percentage')
    def _compute_total_percentage(self):
        for student in self:
            if student.assessment_ids:
                total_percentage = sum(assessment.percentage for assessment in student.assessment_ids)
                student.total_percentage = total_percentage / len(student.assessment_ids)


class StudentAssessment(models.Model):
    _name = 'student.assessment'
    _description = 'Student Assessment'

    student_id = fields.Many2one('student.info', string='Student')
    subject = fields.Char(string='Subject')
    teacher = fields.Char(string='Teacher')
    total_marks = fields.Float(string='Total Marks')
    obtained_marks = fields.Float(string='Obtained Marks')
    percentage = fields.Float(string='Percentage', compute='_compute_percentage', store=True)
    grade = fields.Char(string='Grade', compute='_compute_grade', store=True)

    @api.depends('obtained_marks', 'total_marks')
    def _compute_percentage(self):
        for assessment in self:
            if assessment.total_marks:
                assessment.percentage = (assessment.obtained_marks / assessment.total_marks) * 100

    @api.depends('percentage')
    def _compute_grade(self):
        for assessment in self:
            if assessment.percentage >= 90:
                assessment.grade = 'A+'
            elif assessment.percentage >= 80:
                assessment.grade = 'A'
            elif assessment.percentage >= 70:
                assessment.grade = 'B'
            elif assessment.percentage >= 60:
                assessment.grade = 'C'
            elif assessment.percentage >= 50:
                assessment.grade = 'D'
            else:
                assessment.grade = 'F'


class StudentClass(models.Model):
    _name = 'student.class'
    _description = 'Student Class'

    name = fields.Char(string='Name')





    
