from django.http import response
import graphene
from gql.types import CreateWishResponse

from wishes.models import Wishes


class AddWish(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)
        message = graphene.String(required=True)

    add_wish_resp = graphene.Field(CreateWishResponse)

    @classmethod
    def mutate(cls, root, infom, name, message):

        wish = Wishes(
            name=name,
            message=message
        )

        wish.save()

        return cls(add_wish_resp="True")

