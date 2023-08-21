from fastapi import APIRouter
from models.models import mantenimientos
from config.db import SessionLocal
from schemas.schemas import Mantenimiento
from typing import List
from routes.validations.validations_all import Mantenimiento_Valido

""" Cuando revises esta talla recuerda que a mi los json no me cuadran , asi que los diccionarios que hay ahi era pa facilitarme el trabajo por si daban error"""

manten=APIRouter()

@manten.get("/mantenimientos")
async def Get_mantenimientos():
    db=SessionLocal()
    consulta=mantenimientos.select()
    resultado=db.execute(consulta).fetchall()
    respuesta=[]
    diccionario_respuesta={}
    for tupla in resultado:
       diccionario_respuesta={"id":tupla[0],"chapa":tupla[1],"fecha_inicio":tupla[2],"fecha_fin":tupla[3],"descripcion":tupla[4],"gasto":tupla[5]}
       respuesta.append(diccionario_respuesta)
    return respuesta

@manten.post("/manteniminetos/crear")
async def Mantenimientos_crear(man:Mantenimiento):
   resultado=Mantenimiento_Valido(man) 
   print(resultado)
   if resultado== True:
    db=SessionLocal()
    diccionario_insercion={}
    diccionario_insercion["chapa"]= man.chapa
    diccionario_insercion["fecha_inicio"]=man.fecha_inicio
    diccionario_insercion["fecha_fin"]=man.fecha_fin
    diccionario_insercion["descripcion"]=man.decripcion
    diccionario_insercion["gasto"]=man.gasto
    consulta=mantenimientos.insert().values(diccionario_insercion)
    db.execute(consulta)
    db.commit()
   else:
       return resultado


@manten.delete("/mantenimientos/eliminar")
async def Mantenimientos_eliminar(datos:List[int]):
    db=SessionLocal()
    consulta=None
    for elemento in datos:
     consulta= mantenimientos.delete().where(mantenimientos.c.id == elemento)
     db.execute(consulta)
     db.commit()