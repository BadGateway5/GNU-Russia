from psycopg_pool import ConnectionPool

pool = ConnectionPool(conninfo='dbname=test user=linus password=Habib2005.', min_size=4, max_size=10)