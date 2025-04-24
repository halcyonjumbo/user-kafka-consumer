from requests import Session
from sqlalchemy import MetaData, create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from config.database import DB_CONFIG


class RedshiftConnection:
    """Singleton class for Redshift connection using SQLAlchemy"""
    _instance = None
    _engine = None
    _Session = None
    _metadata = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(RedshiftConnection, cls).__new__(cls, *args, **kwargs)
            


            # build the sqlalchemy URL
            url = URL.create(
            drivername='redshift+redshift_connector', # indicate redshift_connector driver and dialect will be used
            host=DB_CONFIG['host'], # Amazon Redshift host
            port=DB_CONFIG['port'], # Amazon Redshift port
            database=DB_CONFIG['database'], # Amazon Redshift database
            username=DB_CONFIG['user'], # Amazon Redshift username
            password=DB_CONFIG['password'], # Amazon Redshift password
            )

            cls._engine = create_engine(url)
                        
            cls._Session = sessionmaker(bind=cls._engine)
            cls._metadata = MetaData(bind=cls._Session().bind)

        return cls._instance

    @classmethod
    def get_session(cls):
        """Get a new SQLAlchemy session"""
        if cls._Session is None:
            cls._instance = RedshiftConnection()
        return cls._Session()

    @classmethod
    def close_connection(cls):
        """Close the Redshift connection"""
        if cls._engine:
            cls._engine.dispose()
            cls._instance = None
            cls._engine = None
            cls._Session = None
            cls._metadata = None