import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

DATABASE_URL = "postgres://hujzeszkvgdmxj:9ac73148bd771a121bb65ccab533bdcd71a5b2b1a9bb3d9b07363c0ea55729db@ec2-52-45-83-163.compute-1.amazonaws.com:5432/d8r947fdjqauqs"

engine = _sql.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()
