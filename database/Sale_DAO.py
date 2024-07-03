from database.DB_connect import DBConnect
from model.Sale import Sale

class SaleDAO:

    @staticmethod
    def get_anni():
        cnx = DBConnect.get_connection()

        if cnx is None:
            print("Nessuna connessione")
            return None
        result = []
        cursor = cnx.cursor()
        query = """SELECT DISTINCT YEAR(Date)
                FROM go_daily_sales"""
        cursor.execute(query)

        for row in cursor:
            result.append(row[0])
            # print(row)

        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_top_vendite(anno, brand, retailer):
        cnx = DBConnect.get_connection()
        """ # non più necessario
        if anno == "null":
            anno = None

        if brand == "null":
            brand = None

        if retailer == "null":
            retailer = None
        """
        if cnx is None:
            print("Nessuna connessione")
            return None
        result = []
        cursor = cnx.cursor(dictionary=True)
        query = """select *
                from go_daily_sales gds , go_products gp 
                where gds.Product_number = gp.Product_number and year(gds.Date) = coalesce (%s, year(gds.Date)) 
                and gp.Product_brand = coalesce (%s, gp.Product_brand) 
                and gds.Retailer_code = coalesce (%s, gds.Retailer_code)
        """
        cursor.execute(query, [anno, brand, retailer])
        # year(gds.Date) = coalesce (%s, year(gds.Date))

        for row in cursor:
            #print("ciao")
            #print(row)
            result.append(Sale(row["Retailer_code"], row["Product_number"],
                               row["Order_method_code"], row["Date"], row["Quantity"],
                               row["Unit_price"], row["Unit_sale_price"],
                               row["Quantity"]*row["Unit_sale_price"]))

        cursor.close()
        cnx.close()
        #print(result)
        return result

    @staticmethod
    def get_statistiche(anno, brand, retailer):
        cnx = DBConnect.get_connection()
        """ # non più necessario
        if anno == "null":
            anno = None

        if brand == "null":
            brand = None

        if retailer == "null":
            retailer = None
        """
        if cnx is None:
            print("Nessuna connessione")
            return None
        cursor = cnx.cursor()
        query = """select count(distinct gds.Retailer_code), count(distinct gds.Product_number)
                        from go_daily_sales gds , go_products gp 
                        where gds.Product_number = gp.Product_number and year(gds.Date) = coalesce (%s, year(gds.Date)) 
                        and gp.Product_brand = coalesce (%s, gp.Product_brand) 
                        and gds.Retailer_code = coalesce (%s, gds.Retailer_code)
                """
        cursor.execute(query, [anno, brand, retailer])
        result = cursor.fetchone() # tupla con due numeri

        cursor.close()
        cnx.close()
        #print(result)
        return result


