from database.DB_connect import DBConnect
from model.Product import Product

class ProductDAO:

    @staticmethod
    def get_brands():
        cnx = DBConnect.get_connection()

        if cnx is None:
            print("Nessuna connessione")
            return None
        # result = []
        cursor = cnx.cursor()
        query = """SELECT DISTINCT Product_brand
                        FROM go_products"""
        cursor.execute(query)

        """
        for row in cursor:
            result.append(row[0])
            print(row)
        """
        result = cursor.fetchall()
        cursor.close()
        cnx.close()
        return result
