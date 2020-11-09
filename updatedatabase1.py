from coinbase.wallet.client import Client
import json

from app import db
from app.models import Currency 
from config import Config

client = Client(Config.COINBASE_KEY1, Config.COINBASE_KEY2)
prices = client.get_exchange_rates(currency = 'USD')

for a in prices['rates'].keys():
    c = db.session.query(Currency).filter(Currency.acronym == a).first()
    if c is not None:
        c.usd_value = prices['rates'][a]
db.session.commit()
