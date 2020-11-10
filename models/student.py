from odoo import api, fields, models, _

from odoo.exceptions import UserError, ValidationError




class Students(models.Model):
    _name = 'student.student'
    _description = 'This model contains all students and their info'

    name = fields.Char(string='Name', required=True, size=4)
    student_identifier = fields.Char(string='StudentID')
    
    age = fields.Integer(string='Age')
    dob = fields.Date(string='Date of Birth')
    gender = fields.Selection(string='Gender', selection=[('male', 'Male'), ('female', 'Female'),],
    required=True, default='male')
    reg_fees = fields.Float(string='Registration Fees', readonly=True,
    compute='compute_reg_fees')
    note = fields.Text(string='Note')
    parent_id = fields.Many2one(comodel_name='student.parent', string='Parent')
    address = fields.Char(string='Address', related='parent_id.address')

    @api.onchange('parent_id')
    def compute_reg_fees(self):
        for rec in self:
            rec.reg_fees = rec.parent_id.salary * 0.1

    
    _sql_constraints = [
        (
            'student_identifier',
            'UNIQUE(student_identifier)',
            _('StudentID should be unique')
        )
    ]

    
    @api.constrains('age')
    def _check_age(self):
        for record in self:
            if record.age < 10:
                raise ValidationError('Student Age should be greater than 10')
    
    
      

class Parents(models.Model):
    _name = 'student.parent'
    # _description = 'New Description'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    gender = fields.Selection(string='Gender', selection=[('male', 'Male'), ('female', 'Female'),])
    job = fields.Char(string='Job')
    address = fields.Char(string='Address')
    phone = fields.Char(string='Phone')
    salary = fields.Float(string='Salary')
    
    
    
