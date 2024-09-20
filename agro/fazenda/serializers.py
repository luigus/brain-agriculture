from rest_framework import serializers
from .models import ProdutorRural, Cultura


class CulturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultura
        fields = ['nome']


class ProdutorRuralSerializer(serializers.ModelSerializer):
    culturas_plantadas = CulturaSerializer(many=True)

    class Meta:
        model = ProdutorRural
        fields = [
            'cpf', 'cnpj', 'nome_produtor', 'nome_fazenda', 'cidade',
            'estado', 'area_total', 'area_agricultavel', 'area_vegetacao', 'culturas_plantadas'
        ]

    def validate(self, data):
        if data['area_agricultavel'] + data['area_vegetacao'] > data['area_total']:
            raise serializers.ValidationError(
                "A soma da área agricultável e vegetação não pode ser maior que a área total."
            )
        return data
