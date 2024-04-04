from fastapi import FastAPI, Query
from typing import Dict

app = FastAPI()

@app.get("/endpoint1/")
def get_parameter(param: str = Query(..., description="Parâmetro de entrada")):
    return {"parametro_recebido": param}

@app.get("/endpoint2/")
def return_dictionary():
    example_dict = {"chave1": "valor1", "chave2": "valor2"}
    return example_dict

@app.post("/endpoint3/")
def receive_parameters(param1: str, param2: int):
    return {"parametro1": param1, "parametro2": param2}
