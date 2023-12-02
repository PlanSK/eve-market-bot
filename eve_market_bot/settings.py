from loguru import logger
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent
TOKEN=os.environ.get('TOKEN')
DATABASE_FILE='database.sqlite3'

logger.add('debug.log',
           format='{time} {level} {message}',
           level='DEBUG',
           rotation='10 KB'
)
