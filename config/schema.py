import graphene

import gql

class Query(gql.WISH_QUERY,graphene.ObjectType):
    pass


class Mutation(gql.Mutation,graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)