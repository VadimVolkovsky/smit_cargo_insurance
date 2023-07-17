import os

from dotenv import load_dotenv

load_dotenv('.env')

DATABASE_CONFIG = {
    "connections": {"default": os.environ['DATABASE_URL']},
    "apps": {
        "models": {
            "models": ["app.models.insurance", "aerich.models"],
            "default_connection": "default",
        },
    },
}
