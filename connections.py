import MySQLdb


def get_connection():
    # conn = MySQLdb.connect(host="localhost", user="root", passwd="password", port=3306, db="nsinteriors")
    conn = MySQLdb.connect(host="localhost", user="newroot", passwd="sh@d0w", port=3306, db="nsinteriors")
    cursor = conn.cursor()
    return cursor, conn
