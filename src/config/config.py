from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnection:

    def __init__(self) -> None:
        self.__connection_string = 'mysql=pymysql://root:Neosaldina@2021@mysqldb/sys_test'
        self.session = None

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        sessionmaker = sessionmaker
        self.session = sessionmaker(bind=engine)
        return self
    
    def __exit__(self, exc.type, exc.val, exc.tb):
        self.session.close()