import graphene

from gql.types import WishType
from wishes.models import Wishes


class Query(graphene.ObjectType):

    allWishes = graphene.Field(WishType, name="allWishes")

    def resolve_allWishes(root, info):
        return Wishes.objects.all()
