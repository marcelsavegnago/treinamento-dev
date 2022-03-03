# Copyright 2018 ACSONE SA/NV
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo.addons.base_rest.controllers import main


class EscodooRestPublicApiController(main.RestController):
    _root_path = "/escodoo_rest_api/public/"
    _collection_name = "escodoo.rest.public.services"
    _default_auth = "public"


class EscodooRestPrivateApiController(main.RestController):
    _root_path = "/escodoo_rest_api/private/"
    _collection_name = "escodoo.rest.private.services"
    _default_auth = "user"


class EscodooRestNewApiController(main.RestController):
    _root_path = "/escodoo_rest_api/new_api/"
    _collection_name = "escodoo.rest.new_api.services"
    _default_auth = "public"


class EscodooRestJwtApiController(main.RestController):
    # JWT Demo Controller, to be used with auth_jwt_demo
    # https://github.com/OCA/server-auth/tree/14.0/auth_jwt_demo
    _root_path = "/escodoo_rest_api/jwt/"
    _collection_name = "escodoo.rest.jwt.services"
    _default_auth = "jwt_demo_keycloak"
    _component_context_provider = "auth_jwt_component_context_provider"
    _default_cors = "*"
