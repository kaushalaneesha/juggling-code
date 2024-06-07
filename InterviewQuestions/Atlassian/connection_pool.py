# a connection pool is a cache of database connections maintained so that the connections can be reused when future requests to the database are required.[1] Connection pools are used to enhance the performance of executing commands on a database. 

class Connection:
    def __init__(self, url, user, password) -> None:
        self.url = url
        self.user = user
        self.password = password


class ConnectionPool:  
    max_conn = 5                                  # For a give  URL, user and password
    def __init__(self, url, user, password, max_connection = max_conn) -> None:
        self.avilableConnections = []*5
        self.usedConnections = []*5
        self.maxConnections = max_connection

        self.url = url
        self.user = user
        self.password = password

        # Initialise connection pool with all the 5 connections
        for i in range(self.maxConnections):
            self.avilableConnections.append(self.createConnection())

    # Private function to create a connection iternally
    def createConnection(self):
        return Connection(self.url, self.user, self.password)

    # Public function to get connection from the pool
    def getConnection(self):
        if len(self.avilableConnections) > 0:
            cc = self.avilableConnections.pop(0)
            self.usedConnections.append(cc)
            return cc
        else:
            print("No connection available! Already 5 connections in use")

    # Public function to return connection from the pool
    def releaseConnection(self, conn: Connection):
        try:
            self.usedConnections.remove(conn)
            self.avilableConnections.append(conn)
        except:        
            print("Connection doesn't exist can't remove {}".format(conn))

    def getFreeConnectionCount(self):
        return len(self.avilableConnections)


pool = ConnectionPool("jdbc:mysql://localhost/mydb", "testusr", "somepwd")
con1 = pool.getConnection()
con2 = pool.getConnection()
print(pool.getFreeConnectionCount())
con3 = pool.getConnection()
con4 = pool.getConnection()
con5 = pool.getConnection()
con6 = pool.getConnection()
print(pool.getFreeConnectionCount())
pool.releaseConnection(con1)
pool.releaseConnection(con2)
pool.releaseConnection(con4)
print(pool.getFreeConnectionCount())