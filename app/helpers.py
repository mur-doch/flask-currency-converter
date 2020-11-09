from app import app, db
from app.models import Currency 

def get_currencies():
    curs = Currency.query.all()
    acronyms = []
    for c in curs:
        acronyms.append(c.acronym)
    return acronyms

def convert_currency(in_cur, in_amt, out_cur):
    in_cur_obj = Currency.query.filter_by(acronym=in_cur).first()
    out_cur_obj = Currency.query.filter_by(acronym=out_cur).first()
    
    if in_cur_obj is None or out_cur_obj is None:
        return None

    in_cur_value = in_cur_obj.usd_value
    out_cur_value = out_cur_obj.usd_value
    out_cur_min = out_cur_obj.min_size

    return round(in_amt * (out_cur_value / in_cur_value), 2)
