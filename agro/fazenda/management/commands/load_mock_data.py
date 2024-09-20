from decimal import Decimal
import random
from django.core.management.base import BaseCommand
from faker import Faker
from fazenda.models import ProdutorRural, Cultura


class Command(BaseCommand):
    help = 'Gera dados mockados para ProdutorRural e Cultura'

    def handle(self, *args, **kwargs):
        fake = Faker('pt_BR')

        # Cria culturas (se não existirem)
        culturas = ['soja', 'milho', 'algodao', 'cafe', 'cana_acucar']
        for cultura in culturas:
            Cultura.objects.get_or_create(nome=cultura)

        # Gera produtores rurais mockados
        for _ in range(10):
            cpf = fake.cpf() if random.choice([True, False]) else None
            cnpj = fake.cnpj() if not cpf else None
            nome_produtor = fake.name()
            nome_fazenda = fake.company()
            cidade = fake.city()
            estado = fake.state_abbr()
            area_total = fake.pydecimal(left_digits=3, right_digits=2, positive=True)
            area_agricultavel = area_total * Decimal(random.uniform(0.5, 0.9))
            area_vegetacao = area_total - area_agricultavel

            produtor = ProdutorRural.objects.create(
                cpf=cpf,
                cnpj=cnpj,
                nome_produtor=nome_produtor,
                nome_fazenda=nome_fazenda,
                cidade=cidade,
                estado=estado,
                area_total=area_total,
                area_agricultavel=area_agricultavel,
                area_vegetacao=area_vegetacao
            )

            # Adiciona culturas aleatórias
            culturas_selecionadas = Cultura.objects.order_by('?')[:random.randint(1, 3)]
            produtor.culturas_plantadas.add(*culturas_selecionadas)

        self.stdout.write(self.style.SUCCESS('Dados mockados carregados com sucesso!'))
