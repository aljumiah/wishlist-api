from django.shortcuts import render
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,RetrieveUpdateAPIView
from items.models import Item

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import AddedBy

from .serializers import ItemListSerializer,ItemDetailSerializer
from django.db.models import Count



# Create your views here.
class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    filter_backends = [SearchFilter,OrderingFilter,]
    search_fields = ['name','description',]
    permission_classes = [AllowAny,]
    
    
    
    #serializer.save(favorite_items=Item.Count())
class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
    permission_classes = [IsAuthenticated,AddedBy]
