# © 2021 by Maharaj.

import datetime
import pytz
import logging
_logger = logging.getLogger(__name__)
try:
    import jdatetime
except (ImportError, IOError) as err:
    _logger.debug(err)
	
def convert_jalali(original_date):
    if original_date:
        original_date_list = original_date.strftime('%Y-%m-%d %H:%M:%S')
        original_date_t = datetime.datetime.strptime(str(original_date_list), '%Y-%m-%d %H:%M:%S')
        jalali_date = jdatetime.date.fromgregorian(day=original_date_t.day, month=original_date_t.month, year=original_date_t.year)
        return ' '.join((original_date_t.strftime(""),
                         jalali_date.strftime('%Y/%m/%d')))
						 						 

def convert_jalali_wt(original_date):
    if original_date:
        iran = pytz.timezone('Asia/Tehran')
        original_date_i = original_date.astimezone(iran)
        original_date_list = original_date_i.strftime('%Y-%m-%d %H:%M:%S')
        original_date_t = datetime.datetime.strptime(str(original_date_list), '%Y-%m-%d %H:%M:%S')
        jalali_date = jdatetime.date.fromgregorian(day=original_date_t.day, month=original_date_t.month, year=original_date_t.year)
        return ' '.join((original_date_t.strftime("%H:%M:%S"),
                         jalali_date.strftime('%Y/%m/%d')))