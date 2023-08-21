
from fastapi import APIRouter
from models.models import choferes
from config.db import SessionLocal
from schemas.schemas import Chofer
from typing import List
from routes.validations.validations_all import Chofer_Valido

""" Cuando revises esta talla recuerda que a mi los json no me cuadran , asi que los diccionarios que hay ahi era pa facilitarme el trabajo por si daban error"""

chofe=APIRouter()

@chofe.get("/choferes")
async def Get_choferes():
    db= SessionLocal()
    consulta= choferes.select()
    resultado=db.execute(consulta).fetchall()
    print(resultado)
    respuesta=[]
    diccionario_respuesta={}
    for tupla in resultado:
        diccionario_respuesta={"id":tupla[0],"cid":tupla[1],"nombre":tupla[2],"apellido":tupla[3],"base":tupla[4],"cargo":tupla[5],"chapa":tupla[6]}
        respuesta.append(diccionario_respuesta)
    return respuesta
       
@chofe.post("/choferes/crear/post")
async def Crear_choferes(ch:Chofer):
  resultado=Chofer_Valido(ch)
  print(resultado)
  if resultado==True:
   db=SessionLocal()
   diccionario_insercion={}
   diccionario_insercion["cid"]=ch.cid
   diccionario_insercion["nombre"]=ch.nombre
   diccionario_insercion["apellido"]=ch.apellido
   diccionario_insercion["base"]=ch.base
   diccionario_insercion["cargo"]=ch.cargo
   diccionario_insercion["chapa"]=ch.chapa
   consulta= choferes.insert().values(diccionario_insercion)
   db.execute(consulta)
   db.commit()
  else:
      return resultado

   

@chofe.delete("/choferes/eliminar")
async def Eliminar_choferes(datos:List[int]):
    db=SessionLocal()
    consulta=None
    for elemento in datos:
     consulta=choferes.delete().where(choferes.c.id==elemento)
     db.execute(consulta)
     db.commit()
    
    
    
    
    
    
    
    