from rest_framework import viewsets
from .models import Menu, InfoCard
from .serializers import MenuSerializer, InfoCardSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all().order_by('-id')
    serializer_class = MenuSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class InfoCardViewSet(viewsets.ModelViewSet):
    queryset = InfoCard.objects.all().order_by('-id')
    serializer_class = InfoCardSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 