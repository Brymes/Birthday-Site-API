import graphene
from graphene_django.types import DjangoObjectType

from wishes.models import Wishes

class WishType(DjangoObjectType):

    class Meta:
        model = Wishes
        fields = "__all__"


class CreateWishResponse(graphene.Scalar):

    @staticmethod
    def serialize(args_list):
        if args_list:
            response = {}

            response["message"] = "Wish Submitted Successfully"
            return response
