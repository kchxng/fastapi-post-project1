from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .configs import settings

# ----------------------------------------------------------------
# SQLLite3 connection configuration
# ----------------------------------------------------------------
# SQLALCHEMY_DATABASE_URL= "sqlite:///./cmstock.db"
# engine=create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_sam_thread":False})

# ----------------------------------------------------------------
# MySQL Connection configuration
# ----------------------------------------------------------------
# SQLALCHEMY_DATABASE_URL= "mysql+pymysql://root@localhost:3306/fastapi_stock_db?charset=utf8mb4"
# engine=create_engine(SQLALCHEMY_DATABASE_URL)

# ----------------------------------------------------------------
# PostgreSQL connection configuration
# ----------------------------------------------------------------
# SQLALCHEMY_DATABASE_URL= "postgresql+psycopg2://postgres:password@localhost:5433/fastapi_stock_db"
ATABASE_URL= settings.database_url
engine=create_engine(ATABASE_URL)

SessionLocal=sessionmaker(autocommit=False, autoFlush=False, bind=engine)

Base= declarative_base()