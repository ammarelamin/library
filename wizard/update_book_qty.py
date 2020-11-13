from odoo import api, fields, models


class updateBook(models.TransientModel):
    _name = 'update.book'
    _description = 'Update Book Quantity'

    name = fields.Char(string='Name')
    book_id = fields.Many2one(comodel_name='book.book', string='Book', required=True,
    readonly=True)
    qty = fields.Integer(string='Quantity', required=True, default=1)


    def update_qty(self):
        for rec in self:
            book_id = self.env['book.book'].search([('id','=',rec.book_id.id)])
            book_id.qty_available = rec.qty

    
