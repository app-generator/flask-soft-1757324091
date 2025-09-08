# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.policy import default
from apps import db
from sqlalchemy.exc import SQLAlchemyError
from apps.exceptions.exception import InvalidUsage
import datetime as dt
from sqlalchemy.orm import relationship
from enum import Enum

class CURRENCY_TYPE(Enum):
    usd = 'usd'
    eur = 'eur'

class Product(db.Model):

    __tablename__ = 'products'

    id            = db.Column(db.Integer,      primary_key=True)
    name          = db.Column(db.String(128),  nullable=False)
    info          = db.Column(db.Text,         nullable=True)
    price         = db.Column(db.Integer,      nullable=False)
    currency      = db.Column(db.Enum(CURRENCY_TYPE), default=CURRENCY_TYPE.usd, nullable=False)

    date_created  = db.Column(db.DateTime,     default=dt.datetime.utcnow())
    date_modified = db.Column(db.DateTime,     default=db.func.current_timestamp(),
                                               onupdate=db.func.current_timestamp())
    
    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.name} / ${self.price}"

    @classmethod
    def find_by_id(cls, _id: int) -> "Product":
        return cls.query.filter_by(id=_id).first() 

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)

    def delete(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)
        return


#__MODELS__
class Pedidos1(db.Model):

    __tablename__ = 'Pedidos1'

    id = db.Column(db.Integer, primary_key=True)

    #__Pedidos1_FIELDS__
    pedido = db.Column(db.String(255),  nullable=True)
    direccion_envio = db.Column(db.String(255),  nullable=True)
    fecha_pedido = db.Column(db.DateTime, default=db.func.current_timestamp())
    fecha_llegada = db.Column(db.DateTime, default=db.func.current_timestamp())
    cajas_callos = db.Column(db.Integer, nullable=True)
    cajas_albondigas = db.Column(db.Integer, nullable=True)
    cajas_fideos = db.Column(db.Integer, nullable=True)
    cajas_ensaladilla = db.Column(db.Integer, nullable=True)

    #__Pedidos1_FIELDS__END

    def __init__(self, **kwargs):
        super(Pedidos1, self).__init__(**kwargs)


class Albaran_Pedido(db.Model):

    __tablename__ = 'Albaran_Pedido'

    id = db.Column(db.Integer, primary_key=True)

    #__Albaran_Pedido_FIELDS__
    numero = db.Column(db.Integer, nullable=True)
    albaran = db.Column(db.String(255),  nullable=True)
    fecha = db.Column(db.DateTime, default=db.func.current_timestamp())
    ruta = db.Column(db.String(255),  nullable=True)

    #__Albaran_Pedido_FIELDS__END

    def __init__(self, **kwargs):
        super(Albaran_Pedido, self).__init__(**kwargs)


class Albaran_Entrega(db.Model):

    __tablename__ = 'Albaran_Entrega'

    id = db.Column(db.Integer, primary_key=True)

    #__Albaran_Entrega_FIELDS__
    numero = db.Column(db.Integer, nullable=True)
    albaran = db.Column(db.String(255),  nullable=True)
    fecha = db.Column(db.DateTime, default=db.func.current_timestamp())
    ruta = db.Column(db.String(255),  nullable=True)

    #__Albaran_Entrega_FIELDS__END

    def __init__(self, **kwargs):
        super(Albaran_Entrega, self).__init__(**kwargs)


class Entrega(db.Model):

    __tablename__ = 'Entrega'

    id = db.Column(db.Integer, primary_key=True)

    #__Entrega_FIELDS__
    producto = db.Column(db.String(255),  nullable=True)
    cajas = db.Column(db.Integer, nullable=True)
    lote = db.Column(db.Integer, nullable=True)
    fecha_caducidad = db.Column(db.DateTime, default=db.func.current_timestamp())
    entregado = db.Column(db.Integer, nullable=True)

    #__Entrega_FIELDS__END

    def __init__(self, **kwargs):
        super(Entrega, self).__init__(**kwargs)



#__MODELS__END
