from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="API do Unipao",
    description="Essa API serve para cálcular a previsão de preço de uma ação na bolsa.",
    docs_url='/docs' # Habilitar o swagger
)

class InfoPrevisao(BaseModel):
    empresa : str
    volume : float
    prev_fecham : float

@app.get("/")
async def principal():
    return {"status" : True,
            "mensagem": "Serviço rodando"}

@app.get("/previsoes")
def previsoes(infoPrevisao : InfoPrevisao):

    if infoPrevisao.empresa == "aapl":
        w0, w1, w2 = [-15.364324084645187, 1.0639578280039346, -3.2354336426203774e-09]
        previsao = w0 + w1 * infoPrevisao.prev_fecham + w2 * infoPrevisao.volume
    else:
        previsao = None

    return { "profecia" : previsao }