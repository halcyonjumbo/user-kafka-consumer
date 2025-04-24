from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.database import DB_CONFIG


class RedshiftConnection:
    """Singleton class for Redshift connection using SQLAlchemy"""
    _instance = None
    _engine = None
    _Session = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(RedshiftConnection, cls).__new__(cls, *args, **kwargs)
            
            # Create connection string with Redshift-specific parameters
            connection_string = f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
            
            # Create engine with Redshift-specific configurations
            cls._engine = create_engine(
                connection_string,
                connect_args={
                    'options': f'-c search_path={DB_CONFIG["schema"]}',
                    'sslmode': 'require'  # Enable SSL for security
                },
                # Disable SQLAlchemy features that aren't supported by Redshift
                pool_pre_ping=True,
                pool_recycle=3600,
                # Disable standard_conforming_strings check
                connect_args={'options': '-c standard_conforming_strings=off'}
            )
            
            cls._Session = sessionmaker(bind=cls._engine)
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
