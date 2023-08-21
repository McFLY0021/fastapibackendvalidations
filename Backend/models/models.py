from sqlalchemy.types import VARCHAR,Integer,Float
from sqlalchemy import Table,ForeignKey,MetaData,Column,Date,Text,DateTime,Time
from config.db import engine

metadata=MetaData()

vehiculos= Table("vehiculos",metadata,
                 Column("id",Integer,primary_key=True),
                 Column("fabricante",VARCHAR(255)),
                 Column("modelo",VARCHAR(255)),
                 Column("base",VARCHAR(255)),
                 Column("matricula",VARCHAR(255)),
                 Column("pais_compra",VARCHAR(255)),
                 Column("precio_compra",Float),
                 )

choferes=Table("choferes",metadata,
               Column("id",Integer,primary_key=True),
               Column("cid",VARCHAR(11)),
               Column("nombre",VARCHAR(255)),
               Column("apellido", VARCHAR(255)),
               Column("base",VARCHAR(255)),
               Column("cargo",VARCHAR(255)),
               Column("chapa",VARCHAR(7)))

mantenimientos= Table("manteninimientos",metadata,
                      Column("id",Integer,primary_key=True),
                      Column("chapa",VARCHAR(7)),
                      Column("fecha_inicio",Date),
                      Column("fecha_fin",Date),
                      Column("descripcion",Text),
                      Column("gasto",Float))

informes_diarios= Table("informes_diarios", metadata,
                        Column("id",Integer,primary_key=True),
                        Column("fecha",Date),
                        Column("salida",Time),
                        Column("batSalida", Integer),
                        Column("destino",VARCHAR(255)),
                        Column("kmAproxDestino",Float),
                        Column("entrada",Time),
                        Column("batEntrada",Integer)
                        )

reportes_de_cargas=Table("reporte_de_carga",metadata,
                       Column("id",Integer,primary_key=True),
                       Column("fecha",Date),
                       Column("hora_de_inicio",Time),
                       Column("bateria_inicial",Integer),
                       Column("hora_fin",Time),
                       Column("bateria_salida",Integer),
                       Column("consumo_kw",Float),
                       Column("fuente_de_energia",VARCHAR(255))
                       
    
)


metadata.create_all(engine)
               