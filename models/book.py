from odoo import api, fields, models, _


class Books(models.Model):
    _name = 'book.book'
    _rec_name = 'book_name'
    # _description = ''

    name = fields.Char(string='',required=True, readonly=True, 
    index=True, default=lambda self: _('New'))
    book_name = fields.Char(string='Book Name')
    author = fields.Char(string='Author')
    number_of_pages = fields.Integer(string='Number of Pages')
    price = fields.Float(string='Price')
    qty_available = fields.Integer(string='Available Quantity', readonly=True)
    line_ids = fields.One2many(comodel_name='borrowed.book', inverse_name='book_id', string='')
    

    @api.model
    def create(self, vals):
        print('-------------------Vals------------', vals)
        vals['name'] = self.env['ir.sequence'].get('book.book') or _('New')
        result = super(Books, self).create(vals)
        return result


    def print_qty(self):
        print('//////////////',self.qty_available)




class borrowedBooks(models.Model):
    _name = 'borrowed.book'

    # name = fields.Char(string='Name')
    book_id = fields.Many2one(comodel_name='book.book', string='')
    date = fields.Date(string='Date')
    user_id = fields.Many2one(comodel_name='res.users', string='Responsible')
    student_id = fields.Many2one(comodel_name='student.student', string='Student',)
