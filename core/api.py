from ninja import Router
from .models import Territorio
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