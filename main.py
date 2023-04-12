from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse, JSONResponse, FileResponse
import json
import yaml
from templates import deployment
from typing import Union

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola mundo"}

@app.post("/generator")
async def template_generator(request: Request):
    try:
        datos = await request.json()
    except json.decoder.JSONDecodeError:
        response = {
            "message": "La solicitud llegó vacía."
        }
        return JSONResponse(content=response, status_code=400)
    
    if not datos:
        response = {
            "message": "La solicitud llegó vacía."
        }
        return JSONResponse(content=response, status_code=400)
    else:
        contenido = deployment.render(
            nombre=datos["nombre"],
            replicas=datos["replicas"],
            imagen=datos["imagen"],
            puerto=datos["puerto"]
        )
        contenido_yaml = yaml.dump(yaml.safe_load(contenido))
        return PlainTextResponse(content=contenido_yaml, media_type="application/x-yaml")
