from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Evento(BaseModel):
    id: int
    nome: str
    descricao: str
    data: str
    localizacao: str

# Dados em memória
eventos = [
    {
        "id": 1,
        "nome": "Conferência de Tecnologia",
        "descricao": "Uma conferência sobre as últimas tendências em tecnologia.",
        "data": "2024-05-10",
        "localizacao": "Centro de Convenções"
    },
    {
        "id": 2,
        "nome": "Workshop de Marketing Digital",
        "descricao": "Um workshop prático sobre estratégias de marketing digital.",
        "data": "2024-06-15",
        "localizacao": "Sala de Treinamento 1"
    }
]

ids_existente = [evento["id"] for evento in eventos]

@app.get("/")
def pagina_inicial():
    return {"detail": "Acesse /eventos para ver os eventos."}

@app.get("/eventos/", response_model=List[Evento])
def listar_eventos():
    return eventos

@app.get("/eventos/{evento_id}", response_model=Evento)
def obter_evento(evento_id: int):
    for evento in eventos:
        if evento.get("id") == evento_id:
            return evento
    raise HTTPException(status_code=404, detail="Evento não encontrado")

@app.post("/eventos/", response_model=Evento, status_code=201)
def criar_evento(evento: Evento):
    if not all([evento.id, evento.nome, evento.descricao, evento.data, evento.localizacao]):
        raise HTTPException(status_code=400, detail="Todos os campos são obrigatórios.")
    
    if evento.id in ids_existente:
        raise HTTPException(status_code=400, detail="ID do evento deve ser único.")
    
    eventos.append(evento)
    ids_existente.append(evento.id)
    return evento

@app.put("/eventos/{evento_id}", response_model=Evento)
def atualizar_evento(evento_id: int, evento: Evento):
    for index, evt in enumerate(eventos):
        if evt.get("id") == evento_id:
            if not all([evento.nome, evento.descricao, evento.data, evento.localizacao]):
                raise HTTPException(status_code=400, detail="Todos os campos são obrigatórios.")
            
            eventos[index]["nome"] = evento.nome
            eventos[index]["descricao"] = evento.descricao
            eventos[index]["data"] = evento.data
            eventos[index]["localizacao"] = evento.localizacao
            return evento
    raise HTTPException(status_code=404, detail="Evento não encontrado")

@app.delete("/eventos/{evento_id}", response_model=dict)
def deletar_evento(evento_id: int):
    for index, evento in enumerate(eventos):
        if evento.get("id") == evento_id:
            del eventos[index]
            return {"detail": "Evento deletado"}
    raise HTTPException(status_code=404, detail="Evento não encontrado")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
