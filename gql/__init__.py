import graphene

from .query import Query
from .mutation import AddWish

WISH_QUERY = Query


class Mutation(graphene.ObjectType):
    add_wish = AddWish.Field()