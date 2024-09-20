from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinValueValidator
from django_cpf_cnpj.fields import CPFField, CNPJField

CULTURAS_CHOICES = [
    ('soja', 'Soja'),
    ('milho', 'Milho'),
    ('algodao', 'Algodão'),
    ('cafe', 'Café'),
    ('cana_acucar', 'Cana de Açúcar')
]


class ProdutorRural(models.Model):
    cpf = CPFField(null=True, blank=True)
    cnpj = CNPJField(null=True, blank=True)
    nome_produtor = models.CharField(max_length=255)
    nome_fazenda = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    area_total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])
    area_agricultavel = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])
    area_vegetacao = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])
    culturas_plantadas = models.ManyToManyField('Cultura', related_name='fazendas')

    def clean(self):
        if (self.area_agricultavel + self.area_vegetacao) > self.area_total:
            raise ValidationError('A soma da área agricultável e vegetação não pode ser maior que a área total.')

    def __str__(self):
        return f'{self.nome_produtor} - {self.nome_fazenda}'


class Cultura(models.Model):
    nome = models.CharField(max_length=50, choices=CULTURAS_CHOICES)

    def __str__(self):
        return self.nome
