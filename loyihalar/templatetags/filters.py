import uuid

from django import template
from datetime import datetime

register = template.Library()

uzbek_month = {
    1: 'Yanvar',
    2: 'Fevral',
    3: 'Mart',
    4: 'Aprel',
    5: 'May',
    6: 'Iyun',
    7: 'Iyul',
    8: 'Avgust',
    9: 'Sentyabr',
    10: 'Oktyabr',
    11: 'Noyabr',
    12: 'Dekabr',
}


@register.filter
def format_date(value):
    if isinstance(value, datetime):
        month = uzbek_month[value.month]
        return f"{value.day}-{month} {value.year} yil"
    return value


@register.simple_tag
def generate_random(value):
    return f"{value}{uuid.uuid4()}"
