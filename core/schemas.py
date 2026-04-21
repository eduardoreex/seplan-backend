from ninja import Schema

class TerritorioSchema(Schema):
    id: int = None
    nome: str
    
class CidadeIn(Schema):
    codigo_ibge: int
    nome: str
    territorio_id: int
    
class  CidadeOut(Schema):
    codigo_ibge:int
    nome:str
    territorio:TerritorioSchema