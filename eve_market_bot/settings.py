from loguru import logger
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent
DB_LIB_DIR = BASE_DIR.joinpath('db_lib')
LOG_DIR = BASE_DIR.joinpath('logs')
TOKEN=os.environ.get('TOKEN')
DATABASE_FILE='database.sqlite3'


LOG_DIR.mkdir(parents=True, exist_ok=True)
logger.add(LOG_DIR.joinpath('debug.log'),
           format='{time} {level} {message}',
           level='DEBUG',
           rotation='10 KB'
)
