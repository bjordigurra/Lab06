from database.Sale_DAO import SaleDAO
from database.Product_DAO import ProductDAO
from database.Retailer_DAO import RetailerDAO
class Model:
    def __init__(self):
        pass

    def get_anni(self):
        return SaleDAO.get_anni()

    def get_brands(self):
        return ProductDAO.get_brands()

    def get_retailers(self):
        return RetailerDAO.get_retailers()

    def get_top_vendite(self, anno, brand, retailer):
        return SaleDAO.get_top_vendite(anno, brand, retailer)

    def get_statistiche(self, anno, brand, retailer):
        return SaleDAO.get_statistiche(anno, brand, retailer)