from flask_restx import Api

from .cats import api as cats


api = Api(
    title="My Title",
    version="1.0",
    description="A description",
    # All API metadatas
)

api.add_namespace(cats)

# Another way of doing it:
# api.add_namespace(ns2, path='/prefix/of/ns2')
