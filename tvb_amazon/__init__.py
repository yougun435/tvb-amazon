from flask import Flask

app = Flask('tvb-amazon',
            static_folder='./tvb_amazon/static',
            static_url_path='',
            template_folder='./tvb_amazon/templates')

from tvb_amazon import views, api
