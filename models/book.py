from odoo import api, fields, models


class Books(models.Model):
    _name = 'book.book'
    # _description = ''

    name = fields.Char(string='Name')
    author = fields.Char(string='Author')
    number_of_pages = fields.Integer(string='Number of Pages')
    price = fields.Float(string='Price')
    