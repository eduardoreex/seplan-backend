from ninja import Router
from .models import Territorio
from django.shortcuts import  get_object_or_404
from .schemas import TerritorioSchema
from typing import List

router = Router()

@router.get("/territorios", response=List[TerritorioSchema])
def listar_territorios(request):
    return Territorio.objects.all()

@router.post("/territorios", response=TerritorioSchema)
def criar_territorio(request, data: TerritorioSchema):
    territorio = Territorio.objects.create(nome=data.nome)
    return territorio


@router.put("/territorios/{territorio_id}", response=TerritorioSchema)
def editar_territorio(request, territorio_id: int, data: TerritorioSchema):
    territorio = get_object_or_404(Territorio, id = territorio_id)
    territorio.nome = data.nome
    
    territorio.save()
    
    return territorio

@router.delete("/territorios/{territorio_id}")
def remover_territorio(request, territorio_id: int):
    territorio = get_object_or_404(Territorio, id=territorio_id)
    
    territorio.delete()
    
    return {
        "sucesso": True , "mensagem": "Território removido com sucesso"}