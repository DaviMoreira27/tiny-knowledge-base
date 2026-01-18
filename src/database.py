import asyncpg
import dotenv
import os
import logging

logger = logging.getLogger(__name__)

dotenv.load_dotenv()

class DatabaseService:
    def __init__(self):
        self.database_user = os.environ['DB_USER']
        self.database_pass = os.environ['DB_PASS']
        self.database_host = os.environ['DB_HOST']
        self.database_port = os.environ['DB_PORT']
        self.database_name = os.environ['DB_NAME']

    async def db_connection(self):
        try:
            conn = await asyncpg.create_pool(
                user=self.database_user,
                database=self.database_name,
                password=self.database_pass,
                port=self.database_port,
                host=self.database_host,
                command_timeout=60
            )

            yield
            await conn.close()
        except (
            asyncpg.InvalidCatalogNameError,  # database does not exist
            asyncpg.InvalidAuthorizationSpecificationError,  # invalid user
            asyncpg.InvalidPasswordError,  # incorrect pass
            asyncpg.ConnectionDoesNotExistError,  # incorrect host or post
            asyncpg.CannotConnectNowError,  # server unavailable
            asyncpg.TooManyConnectionsError,  # max connections
        ) as e:
            logger.error(f"Error connecting with the database: {e}")
            raise Exception("Internal failure while connecting with the database") from e