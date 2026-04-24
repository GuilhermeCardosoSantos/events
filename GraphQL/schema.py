import strawberry

@strawberry.type
class Message:
    id: int
    content: str


@strawberry.type
class Query:

    @strawberry.field
    def hello(self) -> str:
        return "GraphQL funcionando"


schema = strawberry.Schema(query=Query)