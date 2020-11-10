from odoo import api, fields, models, _


class Books(models.Model):
    _name = 'book.book'
    # _description = ''

    name = fields.Char(string='',required=True, readonly=True, 
    index=True, default=lambda self: _('New'))
    book_name = fields.Char(string='Book Name')
    author = fields.Char(string='Author')
    number_of_pages = fields.Integer(string='Number of Pages')
    price = fields.Float(string='Price')
    

    @api.model
    def create(self, vals):
        print('-------------------Vals------------', vals)
        vals['name'] = self.env['ir.sequence'].get('book.book') or _('New')
        result = super(Books, self).create(vals)
        return result



    