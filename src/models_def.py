# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Enum
import enum

# Instância global do SQLAlchemy
db = SQLAlchemy()

# Enum para o status do carro
class CarStatus(enum.Enum):
    LIBERADO = "liberado"
    EM_CONSERTO = "em_conserto"
    LIBERADO_COM_RESSALVAS = "liberado_com_ressalvas"

#Modelo de dados para as categorias
import enum

class CategoriaEnum(enum.Enum):
    URBANO = "URBANO"
    RODOVIARIO = "RODOVIARIO"
    FRETAMENTO = "FRETAMENTO"

# Modelo de dados para os carros
class Car(db.Model):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True, autoincrement=True)
    prefixo = Column(String(50), unique=True, nullable=False)
    status = Column(Enum(CarStatus), nullable=False, default=CarStatus.LIBERADO)
    categoria = db.Column(db.Enum(CategoriaEnum), nullable=False, default=CategoriaEnum.FRETAMENTO)
    observacao = Column(String(200), nullable=True)

    def __repr__(self):
        return f'<Car {self.prefixo}>'
