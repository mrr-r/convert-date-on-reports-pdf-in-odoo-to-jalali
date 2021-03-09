# © 2021 by Maharaj.

from odoo.addons.base_jalali_convert.convert_jalali import convert_jalali, convert_jalali_wt
from odoo import models, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'


    def convert_jalali(self, obj):
        self.ensure_one()
        return convert_jalali_wt(obj.date_order)



class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'


    def convert_jalali_P(self, obj):
        self.ensure_one()
        return convert_jalali_wt(obj.date_planned)

