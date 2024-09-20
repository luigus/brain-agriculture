from rest_framework import viewsets
from rest_framework.response import Response
from .models import ProdutorRural
from .serializers import ProdutorRuralSerializer
from django.db.models import Sum


class ProdutorRuralViewSet(viewsets.ModelViewSet):
    queryset = ProdutorRural.objects.all()
    serializer_class = ProdutorRuralSerializer


class DashboardViewSet(viewsets.ViewSet):
    def list(self, request):
        total_fazendas = ProdutorRural.objects.count()
        total_hectares = ProdutorRural.objects.aggregate(Sum('area_total'))['area_total__sum']
        dados_por_estado = ProdutorRural.objects.values('estado').annotate(total_area=Sum('area_total'))
        dados_por_cultura = ProdutorRural.objects.values('culturas_plantadas__nome').annotate(total_area=Sum('area_total'))
        dados_por_uso_solo = ProdutorRural.objects.aggregate(
            agricultavel=Sum('area_agricultavel'),
            vegetacao=Sum('area_vegetacao')
        )

        return Response({
            'total_fazendas': total_fazendas,
            'total_hectares': total_hectares,
            'dados_por_estado': dados_por_estado,
            'dados_por_cultura': dados_por_cultura,
            'dados_por_uso_solo': dados_por_uso_solo,
        })
