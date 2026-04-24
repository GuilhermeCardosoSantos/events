from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

# GraphQL
from GraphQL import schema

# Routes
from routes.dummy import router as dummy_router
from routes.metrics import router as metrics_router


app = FastAPI()

app.include_router(dummy_router)
app.include_router(metrics_router)



graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")