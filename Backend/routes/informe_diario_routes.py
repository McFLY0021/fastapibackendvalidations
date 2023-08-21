from fastapi import APIRouter
from models.models import informes_diarios
from schemas.schemas import InformeDiario
from config.db import SessionLocal
from typing import List
from routes.validations.validations_all import Informe_Diario_Valido

Idiario=APIRouter()

@Idiario.get("/Informes")
async def Get_Informes_Diarios():
    db=SessionLocal()
    consulta=informes_diarios.select()
    resultado=[]
    resultado=db.execute(consulta).fetchall()
    respuesta=[]
    diccionario_respuesta={}
    for tupla in resultado:
        diccionario_respuesta={"id":tupla[0],"fecha":tupla[1],"salida":tupla[2],"bateriaS":tupla[3],"destino":tupla[4],"kmAprox":tupla[5],"entrada":tupla[6],"bateriaE":tupla[7]}
        respuesta.append(diccionario_respuesta)
    return respuesta

@Idiario.post("/Informes/crear/post")
async def Crear_Informes_Diarios(inf:InformeDiario):
  resultado =Informe_Diario_Valido(inf)
  print(resultado)
  if resultado == True:
    db=SessionLocal()
    diccionario_inserscion={}
    diccionario_inserscion["fecha"]=inf.fecha
    diccionario_inserscion["salida"]=inf.salida
    diccionario_inserscion["batSalida"]=inf.batSalida
    diccionario_inserscion["destino"]=inf.destino
    diccionario_inserscion["kmAproxDestino"]=inf.kmAproxDestino
    diccionario_inserscion["entrada"]= inf.entrada
    diccionario_inserscion["batEntrada"]= inf.batEntrada
    consulta=informes_diarios.insert().values(diccionario_inserscion)
    db.execute(consulta)
    db.commit()
  else : 
      return resultado
    
@Idiario.delete("/Informes/eliminar")
async def Eliminiar_Informes_Diarios(elementos:List[int]):
    db=SessionLocal()
    consulta=None
    for dato in elementos:
        consulta=informes_diarios.delete().where(informes_diarios.c.id ==dato)
        db.execute(consulta)
        db.commit()
        
        
        """Este es para eliminar todos los informes diarios relacionados a una chapa de vehiculo"""
@Idiario.delete("/Informes/eliminar/todos")
async def Eliminar_Todos_Informes_Diarios(chapa:str):
    pass
   
    
    
    