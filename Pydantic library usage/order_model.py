from pydantic import BaseModel, conint, confloat

class ProductOrder(BaseModel):
    product_name: str
    quantity: conint(gt=0)  # Positive integers only
    unit_price: confloat(gt=0.0)  # Positive floats only

    def total_cost(self) -> float:
        """Calculate total cost of the order."""
        return self.quantity * self.unit_price
