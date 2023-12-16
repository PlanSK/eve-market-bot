from typing import TypeVar
from peewee import SqliteDatabase, IntegrityError, Model

from eve_market_bot.db_lib.models import User, Category, Group, Item, BaseItem
from eve_market_bot.db_lib.common import get_model_data_from_json_file
from eve_market_bot.settings import DATABASE_FILE
from eve_market_bot.settings import logger


BaseItemType = TypeVar('BaseItemType', bound=BaseItem)

DB_MODELS_LIST = [User, Category, Group, Item]
MODEL_FIXTURES = (
    (Category, 'categories.json'),
    (Group, 'groups.json'),
    (Item, 'items.json')
)


class DataBase:
    def __init__(self, db_file: str):
        self._db = SqliteDatabase(db_file)
        self._db.bind(DB_MODELS_LIST)
        self.prepare_db()

    def is_db_tables_exists(self) -> bool:
        return all([table.table_exists() for table in DB_MODELS_LIST])

    def _load_models(self, model_instance: type[BaseItemType],
                     json_file_name: str):
        logger.info(f'Importing {json_file_name} into db.')
        model_data = get_model_data_from_json_file(json_file_name)
        models_list = [model_instance(**model) for model in model_data]
        try:
            with self._db.atomic():
                model_instance.bulk_create(models_list, batch_size=500)
        except IntegrityError:
            logger.warning(f'{json_file_name} is already imported.')
        else:
            logger.info(
                f'{json_file_name} were successfully imported.'
            )

    def prepare_db(self) -> None:
        if not self.is_db_tables_exists():
            with self._db.connection_context():
                self._db.create_tables(DB_MODELS_LIST)
                for model_instance, json_file_name  in MODEL_FIXTURES:
                    self._load_models(model_instance, json_file_name)

    def add_user(self, id: int, first_name: str | None, last_name: str | None) -> bool:
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


db_instance = DataBase(DATABASE_FILE)
