# © 2021 by Maharaj. 

from odoo.addons.base_jalali_convert.convert_jalali import convert_jalali
from odoo import models, api


class AccountInvoice(models.Model):
    _inherit = 'account.move'


    def convert_jalali(self, obj):
        self.ensure_one()
        return convert_jalali(obj.invoice_date)


    def convert_jalali_Due(self, obj):
        self.ensure_one()
        return convert_jalali(obj.invoice_date_due)