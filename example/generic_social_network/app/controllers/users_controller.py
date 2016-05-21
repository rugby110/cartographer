#!flask/bin/python
from flask import Blueprint
from generic_social_network.app import db
from generic_social_network.app.controllers.flask_jsonapi_router import FlaskJSONAPIRouter
from generic_social_network.app.models.query_builders.users_dbm import UsersDBM
from generic_social_network.app.resources.user_resource import UserResource

users_blueprint = Blueprint('users_blueprint', __name__)
users_dbm = UsersDBM(db)


class UserRouter(FlaskJSONAPIRouter):
    RESOURCE = UserResource

    def create_model(self, table_data, inbound_request=None, inbound_session=None):
        return users_dbm.create_from_json(table_data)

    def update_model(self, table_data, inbound_request=None, inbound_session=None):
        return users_dbm.update_from_json(table_data)

    def delete_model(self, model_id, inbound_request=None, inbound_session=None):
        return users_dbm.delete_by_id(model_id)

    def list_models(self, inbound_request=None, inbound_session=None):
        return users_dbm.all


UserRouter.register_router(users_blueprint)
