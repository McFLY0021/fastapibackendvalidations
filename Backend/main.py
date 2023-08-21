from fastapi_offline import FastAPIOffline
from routes.vehiculo_routes import vecycle
from routes.chofer_routes import chofe
from routes.mantenimiento_rotues import manten
from routes.informe_diario_routes import Idiario
from routes.reporte_de_carga_routes import carga

"""Agregale los depends() en los metodos pa que pinche el oauth y el jwt"""


app= FastAPIOffline()
app.include_router(vecycle)
app.include_router(chofe)
app.include_router(manten)
app.include_router(Idiario)
app.include_router(carga)



@app.get("/")
def Root():
    return "Pagina Principal"