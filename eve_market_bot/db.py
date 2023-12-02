from peewee import SqliteDatabase, IntegrityError

from eve_market_bot.db_lib.models import User
from eve_market_bot.settings import DATABASE_FILE
from eve_market_bot.settings import logger


class DataBase:
    def __init__(self, db_file: str):
        self._db = SqliteDatabase(db_file)
        self._db.bind([User])

    def add_user(self, id: int, first_name: str, last_name: str = '') -> bool:
        try:
            User.create_table(safe=True)
            current_user = User.create(
                id=id,
                first_name=first_name,
                last_name=last_name
            )
            current_user.save()
        except IntegrityError as exception:
            logger.error(exception)
            return False
        else:
            return True
        finally:
            self._db.close()


db_instance = DataBase(DATABASE_FILE)
