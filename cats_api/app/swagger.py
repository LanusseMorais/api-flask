from flasgger import Swagger

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Cats API",
        "description": "API para obter informações sobre raças de gatos",
        "version": "1.0.0"
    },
    "basePath": "/api/v1"
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/"
}

swagger = Swagger(template=swagger_template, config=swagger_config)
