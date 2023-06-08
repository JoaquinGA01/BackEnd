import paho.mqtt.publish as mqtt_publish
from fastapi import FastAPI, Request, HTTPException, Form
from Personas.routes.routes import persona
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI(
    title="Personas",
    version="1.0.0.0",
    docs_url = "/api/docs",
    redoc_url= "/api/docs"
)
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("inicio/index.html",{"request":request, "respuesta": ""})

@app.get("/2")
def read_root(request: Request):
    return templates.TemplateResponse("principal/index.html",{"request":request})

app.include_router(persona, prefix="/api/personas")


@app.post("/enviar-mqtt/")
async def enviar_mqtt(topic: str = Form(), message: str = Form()):
    print(message)
    print(topic)
    # Configurar opciones de autenticación
    
    # Enviar mensaje al servidor MQTT
    mqtt_broker = 'broker.hivemq.com'
    mqtt_port = 1883
    mqtt_publish.single(topic, payload=message, hostname=mqtt_broker, port=mqtt_port,)
    
    return {"message": "Mensaje enviado al servidor MQTT"}