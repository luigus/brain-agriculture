# Generated by Django 5.1.1 on 2024-09-20 02:49

import django.core.validators
import django_cpf_cnpj.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cultura",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nome",
                    models.CharField(
                        choices=[
                            ("soja", "Soja"),
                            ("milho", "Milho"),
                            ("algodao", "Algodão"),
                            ("cafe", "Café"),
                            ("cana_acucar", "Cana de Açúcar"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProdutorRural",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cpf",
                    django_cpf_cnpj.fields.CPFField(
                        blank=True, max_length=14, null=True
                    ),
                ),
                (
                    "cnpj",
                    django_cpf_cnpj.fields.CNPJField(
                        blank=True, max_length=18, null=True
                    ),
                ),
                ("nome_produtor", models.CharField(max_length=255)),
                ("nome_fazenda", models.CharField(max_length=255)),
                ("cidade", models.CharField(max_length=100)),
                ("estado", models.CharField(max_length=2)),
                (
                    "area_total",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[django.core.validators.MinValueValidator(0.0)],
                    ),
                ),
                (
                    "area_agricultavel",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[django.core.validators.MinValueValidator(0.0)],
                    ),
                ),
                (
                    "area_vegetacao",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[django.core.validators.MinValueValidator(0.0)],
                    ),
                ),
                (
                    "culturas_plantadas",
                    models.ManyToManyField(
                        related_name="fazendas", to="fazenda.cultura"
                    ),
                ),
            ],
        ),
    ]
