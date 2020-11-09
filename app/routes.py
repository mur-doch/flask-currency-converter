from flask import render_template, flash, redirect, url_for, jsonify, request
from app import app 
from app.forms import ConvertForm
from app.helpers import convert_currency

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ConvertForm()
    return render_template('index.html', form=form)

@app.route('/ajax', methods=['POST'])
def ajax():
    src_cur = request.form['source_currency']
    tgt_cur = request.form['target_currency']
    
    # If the src_amt isn't a valid float, return with an empty string for the target
    # amt.
    src_amt = request.form['source_amount']
    try:
        src_amt = float(src_amt)
    except: 
        return jsonify({'source_currency': src_cur, 'source_amount': src_amt, 'target_currency': tgt_cur, 'target_amount': ""})
    
    result = convert_currency(src_cur, src_amt, tgt_cur) 
    return jsonify({'source_currency': request.form['source_currency'], 'source_amount':request.form['source_amount'], 'target_currency': request.form['target_currency'], 'target_amount': result})
