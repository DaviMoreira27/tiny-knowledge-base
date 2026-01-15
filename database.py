import asyncpg
import dotenv
import os

dotenv.load_dotenv()

class DatabaseService:
    def __init__(self):
        self._database_string = os.environ["DB_STRING"]

    @property
    def database_string(self):
        return self._database_string

    async def db_connection(self):
        try:
            return await asyncpg.connect(self.database_string)
        except (
            asyncpg.InvalidCatalogNameError,  # database does not exist
            asyncpg.InvalidAuthorizationSpecificationError,  # invalid user
            asyncpg.InvalidPasswordError,  # incorrect pass
            asyncpg.ConnectionDoesNotExistError,  # incorrect host or post
            asyncpg.CannotConnectNowError,  # server unavailable
            asyncpg.TooManyConnectionsError,  # max connections
        ) as e:
            raise Exception("Falha interna ao conectar ao banco") from e