# © 2021 by Maharaj.

from odoo.addons.base_jalali_convert.convert_jalali import convert_jalali, convert_jalali_wt
from odoo import models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    def convert_jalali(self, obj):
        self.ensure_one()
        return convert_jalali_wt(obj.date_order)

    def convert_jalali_q(self, obj):
        self.ensure_one()
        return convert_jalali(obj.date_order)

    def convert_jalali_val(self, obj):
        self.ensure_one()
        return convert_jalali(obj.validity_date)
