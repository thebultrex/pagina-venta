from rest_framework import viewsets
from .models import TuModelo
from .serializers import TuModeloSerializer

class TuModeloViewSet(viewsets.ModelViewSet):
    queryset = TuModelo.objects.all()
    serializer_class = TuModeloSerializer



    from django.http import JsonResponse

def mi_vista(request):
    return JsonResponse({"mensaje": "Hola desde Django!"})