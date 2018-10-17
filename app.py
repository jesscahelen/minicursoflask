import os

from flask import Flask
from flask_restful import Api

from controller.item import ItemController, ItemListController
from controller.store import StoreController, StoreListController

app = Flask(__name__)

URL: str = 'postgres://rdvzjmedqsuutd:91da5eb510e9cfff1d50f8141a581043ac02b1993aaa2d002893454373919744@ec2-23-23-80-20.compute-1.amazonaws.com:5432/d5v9m1hvmpj9k3'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', URL)
app.config['SQLALCHEMY_TRACK_MODIFICATONS'] = False
api = Api(app)


@app.route('/')
def hello_world():
    return 'Minicourse - Web API with Python and Flask!'


api.add_resource(ItemController, '/item/<string:name>')
api.add_resource(ItemListController, '/items')
api.add_resource(StoreController, '/store/<string:name>')
api.add_resource(StoreListController, '/stores')

if __name__ == '__main__':
    from db import db

    db.init_app(app)


    @app.before_first_request
    def create_tables():
        db.create_all()


    app.run(host='0.0.0.0', debug=True, port=80)