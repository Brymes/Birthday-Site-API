from graphene_django.types import DjangoObjectType

from wishes.models import Wishes

class WishType(DjangoObjectType):

    class Meta:
        model = Wishes
        fields = "__all__"