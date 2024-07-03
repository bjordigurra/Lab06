from database.DB_connect import DBConnect
from model.Retailer import Retailer

class RetailerDAO:

    @staticmethod
    def get_retailers():
        cnx = DBConnect.get_connection()

        if cnx is None:
            print("Nessuna connessione")
            return None
        result = []
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT *
                FROM go_retailers"""
        cursor.execute(query)
        for row in cursor:
            result.append(Retailer(row["Retailer_code"], row["Retailer_name"], row["Type"], row["Country"]))

        cursor.close()
        cnx.close()
        return result
