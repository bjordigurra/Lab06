from dataclasses import dataclass

from model.Product import Product
from model.Retailer import Retailer


@dataclass
class Sale:
    retailer_code: int
    product_number: int
    order_method_code: int
    date: str
    quantity: int
    unit_price: float
    unit_sale_price: float
    ricavo: float

    def __str__(self):
        return f"Data: {self.date}; Ricavo: {self.ricavo}; Retailer: {self.retailer_code}; Product: {self.product_number}"



