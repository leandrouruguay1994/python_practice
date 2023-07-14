from datetime import date
from datetime import datetime


def date_to_str(date: date) -> str:
    return date.strftime('%d/%m/%Y')


def str_to_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')


def format_float_str_curr(val: float) -> str:
    return f'USD {val:,.2f}'

