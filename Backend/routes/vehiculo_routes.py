from models.models import vehiculos
from schemas.schemas import Vehiculo
from fastapi import APIRouter
from config.db import SessionLocal
from typing import List
from routes.validations.validations_all import Vehiculo_Valido
""" Cuando revises esta talla recuerda que a mi los json no me cuadran , asi que los diccionarios que hay ahi era pa facilitarme el trabajo por si daban error"""
vecycle= APIRouter()

@vecycle.post("/vehiculo/crear")
async def Crear_Vehiculo(veh:Vehiculo):
  print(veh)
  resultado= Vehiculo_Valido(veh)
  print(resultado)
  if resultado == True:
    diccionario_insercion={}
    diccionario_insercion["fabricante"]=veh.fabricante
    diccionario_insercion["modelo"]=veh.modelo
    diccionario_insercion["base"]=veh.base
    diccionario_insercion["matricula"]=veh.matricula
    diccionario_insercion["pais_compra"]=veh.pais_compra
    diccionario_insercion["precio_compra"]=veh.precio_compra
    db=SessionLocal()
    consulta= vehiculos.insert().values(diccionario_insercion)
    db.execute(consulta)
    db.commit()
  else:
      return resultado

@vecycle.get("/vehiculos")
async def Vehiculos_listar():
    db= SessionLocal()
    consulta= vehiculos.select()
    lista=db.execute(consulta).fetchall()
    diccionario_respuesta={}
    respuesta=[]
    for tupla in lista:
        diccionario_respuesta={"id":tupla[0],"fabricante":tupla[1],"modelo":tupla[2],"base":tupla[3],"matricula":tupla[4],"pais_compra":tupla[5],"precio_compra": tupla[6]}
        respuesta.append(diccionario_respuesta)
    return respuesta

"""@vecycle.post("vehiculo/crear/post")
async def Vehiculos_crear(vehiculo:Vehiculo):
  print(vehiculo)
  resultado= Vehiculo_Valido(vehiculo)
  if resultado == True:
    diccionario_insercion={}
    diccionario_insercion["fabricante"]=vehiculo.fabricante
    diccionario_insercion["modelo"]=vehiculo.modelo
    diccionario_insercion["base"]=vehiculo.base
    diccionario_insercion["matricula"]=vehiculo.matricula
    diccionario_insercion["pais_compra"]=vehiculo.pais_compra
    diccionario_insercion["precio_compra"]=vehiculo.precio_compra
    db=SessionLocal()
    consulta= vehiculos.insert().values(diccionario_insercion)
    db.execute(consulta)
    db.commit()
  else:
      return resultado
    """
@vecycle.delete("vehiculo/delete")
async def Vehiculos_eliminar(datos:List[int]):
    db=SessionLocal()
    consulta=None
    for elemento in datos:
     consulta= vehiculos.delete().where(vehiculos.c.id==elemento)
     db.execute(consulta)
     db.commit()
    
    
    

    
        