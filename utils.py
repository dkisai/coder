import logging
from sqlalchemy import create_engine
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
import datetime



logging.basicConfig(
    filename='app.log',  # Nombre y ubicación del archivo de registro
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Crear un objeto de registro
logger = logging.getLogger(__name__)

host = 'data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com'
port = 5439
database = 'data-engineer-database'
user = 'diego_kisai_coderhouse'
password = ' '

db_engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

metadata = MetaData()

logs_table = Table(
    'logs',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('timestamp', DateTime),
    Column('level', String),
    Column('message', String)
)

def log_to_database(level, message):
    now = datetime.datetime.now()
    conn = db_engine.connect()
    conn.execute(logs_table.insert().values(timestamp=now, level=level, message=message))
    conn.close()