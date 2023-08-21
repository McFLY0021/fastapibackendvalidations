from schemas.schemas import Chofer,Vehiculo,Mantenimiento,InformeDiario,ReporteDeCarga
from typing import List 
from datetime import date
from models.models import choferes,vehiculos,mantenimientos,informes_diarios,reportes_de_cargas
from sqlalchemy import Table
from config.db import SessionLocal
from sqlalchemy.exc import NoResultFound

"Validaciones de datos"

def  Chofer_Valido(x:Chofer):
    errores=[]
    if not x.cid:
        errores.append("Debe de colocar un CID (Carne de Identidad) para el chofer insertado")
    if not x.nombre:
        errores.append("Debe de colocar un Nombre para el chofer insertado")
    if not x.apellido:
        errores.append("Debe de colocar un Apellido para el chofer insertado")
    if not x.base:
        errores.append("Debe de colocar una Base a la que pertenece el chofer insertado")
    if not x.cargo:
        errores.append("Debe de colocar un Cargo para el chofer insertado")
    if not x.chapa:
        errores.append("Debe de colocar una Matricula correspondiente al vehiculo del chofer insertado")
    if  not len(x.cid)==11:
        errores.append("El CID(Carne de Identidad) del chofer insertado debe contener solo 11 numeros")
    if not len(x.chapa) ==7:
        errores.append("La Matricula del vehiculo asignado solo puede poseer 7 caracteres ")
    if len(errores)>0:
     return errores
    else :
     return True

def Vehiculo_Valido(v:Vehiculo):
    errores=[] 
    if not v.fabricante:
        errores.append("Debe de colocar un Fabricante del vehiculo insertado")
    if not v.modelo:
        errores.append("Debe de colocar un Modelo del vehiculo insertado ")
    if not v.base:
        errores.append("Debe de colocar una Base a la que pertenece el vehiculo insertado ")
    if not v.matricula:
        errores.append("Debe de colocar una Matricula para el vehiculo insertado")
    if not v.pais_compra:
        errores.append("Debe de colocar el Pais donde fue comprado el vehiculo insertado")
    if not v.precio_compra:
        errores.append("Debe de colocar el Precio de compra del vehiculo insertado")
    if not type(v.precio_compra) == float:
        errores.append("El precio de compra debe colocarse con un (.) para diferenciar los valores")
    if  not v.precio_compra >= 0 :
        errores.append("El Precio de compra del vehiculo ingresado debe de ser mayor o igual a 0 ")
    if not len(v.matricula)==7:
        errores.append("La Matricula del vehiculo insertado debe contener solamente 7 caracteres")
    if len(errores)>0:
     return errores
    else :
     return True
        
def Mantenimiento_Valido(m:Mantenimiento):
    errores=[]
    "Por si vamos a comprobar el anno de ingreso del vehiculo como un dato valido "
    dato:date
    dato=date.today()
    if not m.chapa:
        errores.append("Debe de colocar la Matricula del vehiculo al que le realizara el mantenimiento insertado")
    if not m.fecha_inicio:
        errores.append("Debe de colocar una Fecha de inicio del mantenimiento insertado")
    if not m.fecha_fin:
        errores.append("Debe de colocar una Fecha de fin del mantenimiento insertado")
    if not m.decripcion:
        errores.append("Debe de colocar una Descripcion del mantenimiento insertado")
    if not m.gasto:
        errores.append("Debe de colocar un Gasto estimado del mantenimiento insertado")
    if not len(m.chapa)==7:
        errores.append("La Matricula del vehiculo en cuestion solo puede poseer 7 caracteres ")
    if not type(m.gasto)==float:
        errores.append("El gasto debe ser colocado con un (.) para diferenciar los valores")
    if m.fecha_inicio  > m.fecha_fin:
        errores.append("La Fecha de inicio del mantenimiento no puede ser posterior a la fecha de fin ")
    if not m.gasto >= 0:
        errores.append("El gasto del mantenimiento debe ser mayor o igual a 0 ")    
    if len(errores)>0:
     return errores
    else :
     return True

def Informe_Diario_Valido(inf:InformeDiario):
    errores=[]
    if not inf.fecha:
        errores.append("Debe de colocar una fehca en la que fue realizado el informe imsertado")
    if not inf.salida:
        errores.append("Debe de colocar una Hora de salida del vehiculo para el informe insertado")
    if not inf.batSalida:
        errores.append("Debe de colocar una Bateria de salida del vehiculo para el informe insertado")
    if not inf.destino:
        errores.append("Debe de colocar un Destino del vehiculo para el informe insertado ")
    if not inf.kmAproxDestino:
        errores.append("Debe de colocar una cantidad de Kilometros aproximados de viaje  del vehiculo para el informe insertado ")
    if not inf.entrada:
        errores.append("Debe de colocar una Hora de entrada del vehiculo para el informe insertado")
    if not inf.batEntrada:
        errores.append("Debe de colocar una Bateria de entrada del vehiculo para el informe insertado")
    if inf.salida > inf.entrada:
        errores.append("La Hora de salida del vehiculo no puede ser posterior a la Hora de entrada ")
    if not inf.batSalida >= 0:
        errores.append("La Bateria de salida del vehiculo en cuestion debe de ser mayor o igual a 0 ")
    if not inf.kmAproxDestino >= 0 :
        errores.append("Los Km aproximados para llegar al destino deben de ser mayores o igual a 0 ")
    if not inf.batEntrada >=  0 :
        errores.append("La Bateria de entrada del vehiculo debe de ser mayor o igual a 0 ") 
    if inf.batEntrada> inf.batSalida:
        errores.append("La Bateria de entrada no debe de ser mayor a la bateria de salida ")
    if len(errores)>0:
     return errores
    else :
     return True
 
def Reporte_De_Carga_Valido(rdc:ReporteDeCarga):
    errores=[]
    if not rdc.fecha:
        errores.append("Debe de colocar una Fecha del reporte de carga insertado")
    if not rdc.hora_inicio:
        errores.append("Debe de colocar una Hora de inicio del reporte de carga insertado")
    if not rdc.bateria_inicial:
        errores.append("Debe de colocar una Batria inicial  del repote de carga insertado")
    if not rdc.hora_fin:
        errores.append("Debe de colocar una Hora de fin del reporte de carga insertado")
    if not rdc.bateria_salida:
        errores.append("Debe de colocar una Batira de salida del reporte de carga insertado")
    if not rdc.consumokw:
        errores.append("Debe de colocar un Consumo en Kw del reporte de carga insertado")
    if not rdc.fuente_de_energia:
        errores.append("Debe de colocar una Fuente de energia utilizada para el reporte de carga insertado ")
    if rdc.hora_inicio> rdc.hora_fin:
        errores.append("La hora de Inicio no puede ser posterior a la de hora fin del reporte de carga insertado")
    if rdc.bateria_inicial>rdc.bateria_salida:
        errores.append("La Bateria inicial no debe ser mayor a la bateria de salida del reporte de carga insertado")
    if not rdc.bateria_inicial >=0:
        errores.append("La Bateria inicial debe de ser mayor o igual a 0")
    if not rdc.bateria_salida>=0:
        errores.append("La Bateria de salida debe de ser mayor o igual a 0 ")
    if not type(rdc.consumokw)==float:
        errores.append("El Consumo en Kw debe de colocarse con un (.) para diferenciar los valores")
    if not rdc.consumokw >= 0:
        errores.append("El Consumo en Kw del reporte de carga insertado debe de ser mayor o igual a 0")
    if len(errores)==0:
        return True
    else:
        return errores
     
 
"Comprobacion de existencia de dato en base de datos(le pasas la tabla y el dato unico por el que se va a comparar)"
async def Existe_en_Bd_chofer(ch:Chofer):
    conexion=SessionLocal()
    try :
        existe=conexion.query(choferes).filter(choferes.c.cid == ch.cid).one()
        return True
    except NoResultFound:
        conexion.close()
        return False

async def Existe_en_Bd_vehiculo(veh:Vehiculo):
    conexion=SessionLocal()
    try :
        existe=conexion.query(vehiculos).filter(vehiculos.c.matricula == veh.matricula).one()
        return True
    except NoResultFound:
        conexion.close()
        return False
    
        
    
     



        
        
        
        
        
    
    
    
        
    