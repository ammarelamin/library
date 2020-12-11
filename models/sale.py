from odoo import api, fields, models

from odoo.exceptions import UserError, ValidationError



class saleOrder(models.Model):
    _inherit = 'sale.order'

    ref = fields.Char(string='Reference')
    state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('sent', 'Sent'),
    ('sale', 'Sale'),
    ('done', 'Done'),
    ('cancel', 'Cancel'),
    ('reject', 'Reject'),])
    

    def action_test(self):
        print('--------------testing function-------------')


    
    @api.model
    def create(self, values):
        if values['ref'] == False:
            print('//////////////// Null Value for ref ///////////////////')
        else:
            print('///////////// Ref contains value /////////////////')
        result = super(saleOrder, self).create(values)
        return result
    

    def action_confirm(self):
        print('//////////////inside action conirm function//////////////')
        for rec in self:
            if not rec.order_line:
                raise ValidationError('Please add products!')
        result = super(saleOrder, self).action_confirm()
        return result



class saleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    productID = fields.Char(string='ProductID')
