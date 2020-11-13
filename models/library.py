from odoo import api, fields, models


class bookBorrow(models.Model):
    _name = 'book.borrow'
    _description = 'Tracking borrowed books'

    # name = fields.Char(string='Name')
    state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('confirm', 'Confirmed'),('reject', 'Rejected')],
    readonly=True)
    date = fields.Date(string='Date', default=fields.Date.context_today,)
    user_id = fields.Many2one(comodel_name='res.users', string='Responsible',
    default=lambda self: self.env.user)
    student_id = fields.Many2one(comodel_name='student.student', string='Student',
    required=True)
    book_id = fields.Many2one(comodel_name='book.book', string='Book',
    required=True)
    note = fields.Text(string='Note')
    




class bookRetention(models.Model):
    _name = 'book.return'
    _description = 'Return Book'

    # name = fields.Char(string='Name')
    state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('confirm', 'Confirmed')],
    readonly=True)
    date = fields.Date(string='Date', default=fields.Date.context_today)
    user_id = fields.Many2one(comodel_name='res.users', string='Responsible',
    default=lambda self: self.env.user)
    student_id = fields.Many2one(comodel_name='student.student', string='Student',
    required=True)
    book_id = fields.Many2one(comodel_name='book.book', string='Book',
    required=True)
    note = fields.Text(string='Note')

    
    

    