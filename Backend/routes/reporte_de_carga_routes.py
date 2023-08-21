from fastapi import APIRouter
from schemas.schemas import ReporteDeCarga
from models.models import reportes_de_cargas
from config.db import SessionLocal
from typing import List
from routes.validations.validations_all import Reporte_De_Carga_Valido



carga=APIRouter()


@carga.get("/reportes_de_carga")
async def Get_Reportes_de_carga():
    db=SessionLocal()
    consulta= reportes_de_cargas.selecto()
    resultado= db.execute(consulta).fetchall()
    respuesta=[]
    diccionario_de_respuesta={}
    for tupla in resultado:
        diccionario_de_respuesta={"id":tupla[0],"fecha":tupla[1],"hora_de_inicio":tupla[2],"bateria_inicio":tupla[3],"hora_fin":tupla[4],"bateria_salida":tupla[5],"comsumpkw":tupla[6],"fuente_de_energia":tupla[7]}
        respuesta.append(diccionario_de_respuesta)
    return respuesta

@carga.post("/reportes_de_carga/crear/post")
async def Crear_Reportes_de_carga(rdc:ReporteDeCarga):
   respuesta=Reporte_De_Carga_Valido(rdc)
   print(respuesta)
   if respuesta==True:
    db=SessionLocal()
    diccionario_de_insercion={}
    diccionario_de_insercion["fecha"]=rdc.fecha
    diccionario_de_insercion["hora_de_inicio"]=rdc.hora_inicio
    diccionario_de_insercion["bateria_inicial"]=rdc.bateria_inicial
    diccionario_de_insercion["hora_fin"]=rdc.hora_fin
    diccionario_de_insercion["bateria_salida"]=rdc.bateria_salida
    diccionario_de_insercion["consumo_kw"]=rdc.consumokw
    diccionario_de_insercion["fuente_de_energia"]=rdc.fuente_de_energia
    consulta=reportes_de_cargas.insert().values(diccionario_de_insercion)
    db.execute(consulta)
    db.commit()
   else:
       return respuesta
    
@carga.delete("/reportes_de_carga/eliminar")
async def Eliminar_Reportes_de_carga(elementos:List[int]):
 db=SessionLocal()
 for elemento in elementos:
     consulta=reportes_de_cargas.delete().where(reportes_de_cargas.c.id == elemento)
     db.execute(consulta)
     db.commit()

    