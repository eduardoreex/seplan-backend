from ninja import Router
from .models import Territorio, Cidade
from django.shortcuts import  get_object_or_404
from .schemas import TerritorioSchema
from typing import List
from .schemas import TerritorioSchema, CidadeIn, CidadeOut

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
    

@router.get("/cidades", response=List[CidadeOut])
def listar_cidades(request, nome: str = None, territorio_id: int = None):
    cidades = Cidade.objects.all()
    if nome:
        cidades = cidades.filter(nome__icontains=nome) 
    if territorio_id:
        cidades = cidades.filter(territorio_id=territorio_id)
    return cidades

@router.post("/cidade", response=CidadeOut)
def criar_cidade(request, data: CidadeIn):
    cidade =  Cidade.objects.create(codigo_ibge=data.codigo_ibge,nome = data.nome , territorio_id= data.territorio_id)
    return  cidade

@router.put("/cidades/{codigo_ibge}", response=CidadeOut)
def editar_cidade(request, codigo_ibge: int, data : CidadeIn):
    cidade = get_object_or_404(Cidade, codigo_ibge= codigo_ibge)
    cidade.nome = data.nome
    cidade.territorio_id = data.territorio_id
    cidade.save()
    return cidade

@router.delete("/cidades/{codigo_ibge}")
def remover_cidade(request,codigo_ibge: int):
    cidade =  get_object_or_404(Cidade, codigo_ibge=codigo_ibge)
    cidade.delete()
    return{"sucesso": True, "mensagem": "Cidade removida com sucesso"}
