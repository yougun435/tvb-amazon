from flask import Flask

app = Flask('tvb-amazon')

from tvb_amazon import views, api
