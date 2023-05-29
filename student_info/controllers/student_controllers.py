from odoo import http
from odoo.http import request

class StudentController(http.Controller):
    @http.route('/students', auth='public', website=True)
    def student_list(self, **kwargs):
        students = request.env['student.info'].sudo().search([])
        return request.render('student_info_your_name.student_list', {'students': students})

    @http.route('/students/<int:student_id>', auth='public', website=True)
    def student_info(self, student_id, **kwargs):
        student = request.env['student.info'].sudo().browse(student_id)
        return request.render('student_info_your_name.student_info', {'student': student})
