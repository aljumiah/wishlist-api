from rest_framework import serializers
from items.models import Item, FavoriteItem
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id' , 'first_name','last_name']


class ItemFavoriteSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = FavoriteItem
        fields = '__all__'


class ItemListSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name = 'api-detail',
        lookup_field = 'id',
        lookup_url_kwarg = 'item_id'
    )

    added_by= UserSerializer()
    fav_count = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ['id','name', 'description', 'detail' , 'added_by', 'fav_count']
    
    def get_fav_count(self,obj):
        return obj.favorite_items.count()

class ItemDetailSerializer(serializers.ModelSerializer):
    favorite_items = ItemFavoriteSerializer(many=True)
    class Meta:
        model = Item 
        fields = '__all__'


