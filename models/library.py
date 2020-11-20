from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class bookBorrow(models.Model):
    _name = 'book.borrow'
    _description = 'Tracking borrowed books'

    # name = fields.Char(string='Name')
    state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('confirm', 'Confirmed'),('reject', 'Rejected')],
    readonly=True, default='draft')
    date = fields.Date(string='Date', default=fields.Date.context_today,)
    user_id = fields.Many2one(comodel_name='res.users', string='Responsible',
    default=lambda self: self.env.user)
    student_id = fields.Many2one(comodel_name='student.student', string='Student',
    required=True)
    book_id = fields.Many2one(comodel_name='book.book', string='Book',
    required=True)
    note = fields.Text(string='Note')
    
    def action_confirm(self):
        print('-------------- Confirmed---------------')
        for rec in self:
            if rec.book_id.qty_available < 1:
                raise ValidationError("You don't have enough quantity")

            print('/////////user id///////////', rec.user_id.id)

            custody_id = rec.book_id.line_ids.create({
                'student_id': rec.student_id.id,
                'date': rec.date,
                'user_id': rec.user_id.id,
                'book_id': rec.book_id.id,
            })

            rec.book_id.qty_available -= 1
            rec.write({'state':'confirm'})

    def action_reject(self):
        for rec in self:
            rec.write({'state':'reject'})
            # rec.state = 'reject'



class bookRetention(models.Model):
    _name = 'book.return'
    _description = 'Return Book'

    # name = fields.Char(string='Name')
    state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('confirm', 'Confirmed')],
    readonly=True, default='draft')
    date = fields.Date(string='Date', default=fields.Date.context_today)
    user_id = fields.Many2one(comodel_name='res.users', string='Responsible',
    default=lambda self: self.env.user)
    student_id = fields.Many2one(comodel_name='student.student', string='Student',
    required=True)
    book_id = fields.Many2one(comodel_name='book.book', string='Book',
    required=True)
    note = fields.Text(string='Note')

    
    def action_confirm(self):
        for rec in self:
            #check if the book is in student custody
            custody = self.env['borrowed.book'].search([('student_id','=',rec.student_id.id),
            ('book_id','=',rec.book_id.id)])
            if len(custody) >= 1:
                print('-------------Custody---------------- = ', custody)
                custody.unlink()
                rec.book_id.qty_available += 1
                rec.write({'state': 'confirm'})

    

    