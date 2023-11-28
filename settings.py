from loguru import logger
import os


TOKEN=os.environ.get('TOKEN')

logger.add('debug.log',
           format='{time} {level} {message}',
           level='DEBUG',
           rotation='10 KB'
)
