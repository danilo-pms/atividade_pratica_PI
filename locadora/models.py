from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nome
        
class Filme(models.Model):
    titulo = models.CharField(max_length=150)
    valor = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo
    
class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    
    def __str__(self):
        return self.nome
    
class Locacao(models.Model):
    nome = models.CharField(max_length=150)
    data = models.DateField()
    filmes = models.ManyToManyField(Filme)
    clientes = models.ManyToManyField(Cliente)
    
    def filmes_str(self):
        return ', '.join([p.titulo for p in self.filmes.all()])
    
    def clientes_str(self):
        return ', '.join([p.nome for p in self.clientes.all()])