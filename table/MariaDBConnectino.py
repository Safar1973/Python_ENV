import MariaDBConnection

class MariaDBConnection:
    def __init__(self, host, user, password, database, port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.connection = None
        self.error = None
        try:
            self.connection = mariadb.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
        except MariaDBConnection .Error as e:
            self.error = str(e)
            
            def isconnected(self):
                return self.connection is not None and self.error is None
            
            def getConnection(self):
                if self.isconnected():
                    return self.connection
                  else:
                      return None
