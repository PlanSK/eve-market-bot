import json

from eve_market_bot.settings import DB_LIB_DIR


def get_model_data_from_json_file(file_name: str) -> list|dict:
    path_to_file = DB_LIB_DIR.joinpath('fixtures', file_name)
    with path_to_file.open() as json_file:
        return json.load(json_file)
