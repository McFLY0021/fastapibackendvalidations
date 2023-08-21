from pydantic import BaseModel
from datetime import date,time,datetime
from typing import  Text

class Vehiculo(BaseModel):
    fabricante:str
    modelo:str
    base:str
    matricula:str
    pais_compra:str
    precio_compra:float
    

class Chofer(BaseModel):
   cid:str
   nombre:str
   apellido:str
   base:str
   cargo:str
   chapa:str
   
   
class Mantenimiento(BaseModel):
    chapa:str
    fecha_inicio:date
    fecha_fin:date
    decripcion:Text
    gasto:float
    
class InformeDiario(BaseModel):
    fecha:date
    salida:time
    batSalida:int
    destino:str
    kmAproxDestino:float
    entrada:time
    batEntrada:int
    

class ReporteDeCarga(BaseModel):
    fecha:date
    hora_inicio:time
    bateria_inicial:int
    hora_fin:time
    bateria_salida:int
    consumokw:float
    fuente_de_energia:str
    
    
    
    
    
    
    