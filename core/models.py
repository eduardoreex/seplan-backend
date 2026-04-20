from django.db import models

class Territorio(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome


class Cidade(models.Model):
    codigo_ibge = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    
    territorio = models.ForeignKey(Territorio, on_delete=models.CASCADE, related_name='cidades')

    def __str__(self):
        return f"{self.codigo_ibge} - {self.nome}"