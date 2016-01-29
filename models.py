from __init__ import db
from sqlalchemy.dialects.postgresql import JSON
import datetime
from sqlalchemy.types import Integer, Boolean
from flask.ext.restless import APIManager


class Result(db.Model):
    __tablename__ = 'results'
    
    id = db.Column(db.Integer, primary_key=True)
    store = db.Column(db.String())
    product = db.Column(JSON)
    asin = db.Column(db.String())
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, store, product, asin):
        self.store = store
        self.product = product
        self.asin = asin

    def __repr__(self):
        return '<id %r>' % self.id


class Target(db.Model):
    __tablename__ = 'target'

    store = db.Column(db.String())
    product = db.Column(JSON)
    asin = db.Column(db.String(), primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, store, product, asin):
        self.store = store
        self.product = product
        self.asin = asin

    def __repr__(self):
        return '<id %r>' % self.asin


class Icc(db.Model):
    __tablename__ = 'icc'

    store = db.Column(db.String())
    product = db.Column(JSON)
    asin = db.Column(db.Unicode, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, store, product, asin):
        self.store = store
        self.product = product
        self.asin = asin

    def __repr__(self):
        return '<id %r>' % self.asin


class Eedistribution(db.Model):
    __tablename__ = 'eedistribution'

    store = db.Column(db.String())
    product = db.Column(JSON)
    asin = db.Column(db.Unicode, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, store, product, asin):
        self.store = store
        self.product = product
        self.asin = asin

    def __repr__(self):
        return '<id %r>' % self.asin


class Kristy(db.Model):
    __tablename__ = 'kristy'

    store = db.Column(db.String())
    product = db.Column(JSON)
    asin = db.Column(db.Unicode, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, store, product, asin):
        self.store = store
        self.product = product
        self.asin = asin

    def __repr__(self):
        return '<id %r>' % self.asin


class Mattel(db.Model):
    __tablename__ = 'mattel'

    store = db.Column(db.String())
    product = db.Column(JSON)
    asin = db.Column(db.Unicode, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, store, product, asin):
        self.store = store
        self.product = product
        self.asin = asin

    def __repr__(self):
        return '<id %r>' % self.asin


class Kmart(db.Model):
    __tablename__ = 'kmart'

    store = db.Column(db.String())
    product = db.Column(JSON)
    asin = db.Column(db.Unicode, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, store, product, asin):
        self.store = store
        self.product = product
        self.asin = asin

    def __repr__(self):
        return '<id %r>' % self.asin


class Cherylsdolls(db.Model):
    __tablename__ = 'cherylsdolls'

    store = db.Column(db.String())
    product = db.Column(JSON)
    asin = db.Column(db.Unicode, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, store, product, asin):
        self.store = store
        self.product = product
        self.asin = asin

    def __repr__(self):
        return '<id %r>' % self.asin


class Americangirl(db.Model):
    __tablename__ = 'americangirl'

    store = db.Column(db.String())
    product = db.Column(JSON)
    asin = db.Column(db.Unicode, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, store, product, asin):
        self.store = store
        self.product = product
        self.asin = asin

    def __repr__(self):
        return '<id %r>' % self.asin


class Hasbro(db.Model):
    __tablename__ = 'hasbro'

    store = db.Column(db.String())
    product = db.Column(JSON)
    asin = db.Column(db.Unicode, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, store, product, asin):
        self.store = store
        self.product = product
        self.asin = asin

    def __repr__(self):
        return '<id %r>' % self.asin


class Lego(db.Model):
    __tablename__ = 'lego'

    store = db.Column(db.String())
    product = db.Column(JSON)
    asin = db.Column(db.Unicode, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, store, product, asin):
        self.store = store
        self.product = product
        self.asin = asin

    def __repr__(self):
        return '<id %r>' % self.asin


class Scraped(db.Model):
    __tablename__ = 'scraped'

    id = db.Column(db.Integer, primary_key=True)
    store = db.Column(db.String())
    product = db.Column(JSON)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    seen = db.Column(db.Boolean, unique=False, default=False)

    def __init__(self, store, product):
        self.store = store
        self.product = product


    def __repr__(self):
        return '<id %r>' % self.id


class AmazonMatch(db.Model):
    __tablename__ = 'amazonmatch'

    id = db.Column(db.Integer, primary_key=True)
    listed_price = db.Column(db.String())
    sales_price = db.Column(db.String())
    title = db.Column(db.String())
    promo = db.Column(db.String())
    upc = db.Column(db.String())
    link = db.Column(db.String())
    emailtocart = db.Column(db.String())
    addtocart = db.Column(db.String())
    store = db.Column(db.String())
    amazon_matched = db.Column(db.Boolean, unique=False, default=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, listed_price, sales_price, title, promo, upc, link, emailtocart, addtocart, store, amazon_matched):
        self.store = store
        self.listed_price = listed_price
        self.sales_price = sales_price
        self.title = title
        self.promo = promo
        self.upc = upc
        self.link = link
        self.emailtocart = emailtocart
        self.addtocart = addtocart
        self.amazon_matched = amazon_matched

    def __repr__(self):
        return '<id %r>' % self.id


class Disney(db.Model):
    __tablename__ = 'disney'

    store = db.Column(db.String())
    product = db.Column(JSON)
    asin = db.Column(db.Unicode, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, store, product, asin):
        self.store = store
        self.product = product
        self.asin = asin

    def __repr__(self):
        return '<id %r>' % self.asin


class Toysrus(db.Model):
    __tablename__ = 'toysrus'

    store = db.Column(db.String())
    product = db.Column(JSON)
    asin = db.Column(db.String(), primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def rank_by_salesrank(self):
        return Toysrus.query.order_by(Toysrus.product['salesrank'].cast(Integer))

    def __init__(self, store, product, asin):
        self.store = store
        self.product = product
        self.asin = asin

    def __repr__(self):
        return '<id %r>' % self.asin


class Lots(db.Model):
    __tablename__ = 'lots'

    store = db.Column(db.String())
    product = db.Column(JSON)
    asin = db.Column(db.String(), primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def rank_by_salesrank(self):
        return Lots.query.order_by(Lots.product['salesrank'].cast(Integer))

    def __init__(self, store, product, asin):
        self.store = store
        self.product = product
        self.asin = asin

    def __repr__(self):
        return '<id %r>' % self.asin


class Walmart(db.Model):
    __tablename__ = 'walmart'

    store = db.Column(db.String())
    product = db.Column(JSON)
    asin = db.Column(db.String(), primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def rank_by_salesrank(self):
        return Walmart.query.order_by(Walmart.product['salesrank'].cast(Integer))

    def __init__(self, store, product, asin):
        self.store = store
        self.product = product
        self.asin = asin

    def __repr__(self):
        return '<id %r>' % self.asin


class Plushzoo(db.Model):
    __tablename__ = 'plushzoo'

    store = db.Column(db.String())
    product = db.Column(JSON)
    asin = db.Column(db.String(), primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def rank_by_salesrank(self):
        return Plushzoo.query.order_by(Plushzoo.product['salesrank'].cast(Integer))

    def __init__(self, store, product, asin):
        self.store = store
        self.product = product
        self.asin = asin

    def __repr__(self):
        return '<id %r>' % self.asin


class Genco(db.Model):
    __tablename__ = 'genco'

    store = db.Column(db.String())
    product = db.Column(JSON)
    asin = db.Column(db.String(), primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def rank_by_salesrank(self):
        return Genco.query.order_by(Genco.product['salesrank'].cast(Integer))

    def __init__(self, store, product, asin):
        self.store = store
        self.product = product
        self.asin = asin

    def __repr__(self):
        return '<id %r>' % self.asin


class Bestbuy(db.Model):
    __tablename__ = 'bestbuy'

    store = db.Column(db.String())
    product = db.Column(JSON)
    asin = db.Column(db.String(), primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def rank_by_salesrank(self):
        return Bestbuy.query.order_by(Bestbuy.product['salesrank'].cast(Integer))

    def __init__(self, store, product, asin):
        self.store = store
        self.product = product
        self.asin = asin

    def __repr__(self):
        return '<id %r>' % self.asin


class Xsdepot(db.Model):
    __tablename__ = 'xsdepot'

    store = db.Column(db.String())
    product = db.Column(JSON)
    asin = db.Column(db.String(), primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def rank_by_salesrank(self):
        return Xsdepot.query.order_by(Xsdepot.product['salesrank'].cast(Integer))

    def __init__(self, store, product, asin):
        self.store = store
        self.product = product
        self.asin = asin

    def __repr__(self):
        return '<id %r>' % self.asin


class Shopping(db.Model):
    __tablename__ = 'shopping'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String())
    store = db.Column(db.String())
    product = db.Column(JSON)
    asin = db.Column(db.String())
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def rank_by_salesrank(self):
        return Shopping.query.order_by(Shopping.product['salesrank'].cast(Integer))

    def __init__(self, user, store, product, asin):
        self.user = user
        self.store = store
        self.product = product
        self.asin = asin

    def __repr__(self):
        return '<id %r>' % self.id


class Inventory(db.Model):
    __tablename__ = 'inventory'

    store = db.Column(db.String())
    sku = db.Column(db.String(), primary_key=True)
    fnsku = db.Column(db.String())
    asin = db.Column(db.String())
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    cost = db.Column(db.Float())
    myprice = db.Column(db.Float())
    myprofit = db.Column(db.Float())
    quantity = db.Column(db.Integer())
    active = db.Column(db.Boolean(create_constraint=False))
    datecreated = db.Column(db.DateTime)
    buyboxprice = db.relationship('Buybox', backref='inventory', cascade="all, delete-orphan", lazy='dynamic')
    pagelink = db.Column(db.String())
    kristinid = db.Column(db.Integer())
    upc = db.Column(db.String())
    ean = db.Column(db.String())
    name = db.Column(db.String())
    salesrank = db.Column(db.Integer())
    condition = db.Column(db.String())
    productgroup = db.Column(db.String())
    height = db.Column(db.Float())
    length = db.Column(db.Float())
    width = db.Column(db.Float())
    weight = db.Column(db.Float())
    image = db.Column(db.String())
    model = db.Column(db.String())
    rf = db.Column(db.Float())
    vcf = db.Column(db.Float())
    promo = db.Column(db.Float())
    shipping = db.Column(db.String())
    prices = db.relationship('Prices', backref='inventory', cascade="all, delete-orphan", lazy='dynamic')
    seller = db.Column(db.String())
    datecreated = db.Column(db.String())

    def rank_by_salesrank(self):
        return Inventory.query.order_by(
            Inventory.salesrank)

    def __init__(self, sku, kristinid):
        self.sku = sku
        self.kristinid = kristinid

    def __repr__(self):
        return '<id %r>' % self.sku


class Prices(db.Model):
    __tablename__ = 'prices'

    id = db.Column(db.Integer, primary_key=True)
    landedprice = db.Column(db.Float())
    sku = db.Column(db.String(), db.ForeignKey('inventory.sku'))
    asin = db.Column(db.String())
    profit = db.Column(db.Float())
    condition = db.Column(db.String())
    seller = db.Column(db.String())

    def __init__(self, sku, landedprice,
                 seller, condition, asin):
        self.sku = sku
        self.landedprice = landedprice
        self.condition = condition
        self.seller = seller
        self.profit = None
        self.asin = asin

    def __repr__(self):
        return '<id %r>' % self.id


class Buybox(db.Model):
    __tablename__ = 'buybox'

    id = db.Column(db.Integer, primary_key=True)
    landedprice = db.Column(db.Float())
    sku = db.Column(db.String(), db.ForeignKey('inventory.sku'))
    asin = db.Column(db.String())
    profit = db.Column(db.Float())
    condition = db.Column(db.String())
    buybox = db.Column(db.Boolean(create_constraint=False))
    seller = db.Column(db.String())

    def __init__(self, sku, landedprice,
                 condition, asin):
        self.sku = sku
        self.landedprice = landedprice
        self.condition = condition
        self.profit = None
        self.asin = asin
        self.buybox = True
        self.seller = 'Buybox'

    def __repr__(self):
        return '<id %r>' % self.id


class Upc(db.Model):
    __tablename__ = 'upc'

    upc = db.Column(db.String(), primary_key=True)
    asin = db.Column(db.String())
    buyboxprice = db.Column(db.Float())
    pagelink = db.Column(db.String())
    title = db.Column(db.String())
    image = db.Column(db.String())
    seller = db.Column(db.String())
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    location = db.Column(JSON)
    myprice = db.Column(db.Float())
    salesrank = db.Column(db.Integer())

    def __init__(self, upc):
        self.upc = upc

    def __repr__(self):
        return '<id %r>' % self.upc


class Uploads(db.Model):
    __tablename__ = 'uploads'

    email = db.Column(db.String())
    file = db.Column(JSON)
    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, file, email):
        self.email = email
        self.file = file

    def __repr__(self):
        return '<id %r>' % self.id
