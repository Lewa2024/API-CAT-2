from django.db import models

# Customer model
class Customer(models.Model):
    name = models.CharField(max_length=100)  # Customer's full name
    email = models.EmailField(unique=True)   # Unique email for the customer

    def __str__(self):
        return self.name

# Order model
class Order(models.Model):
    customer = models.ForeignKey(
        Customer, 
        on_delete=models.CASCADE,  # Delete orders if the customer is deleted
        related_name='orders'      # Allows reverse access from Customer
    )
    order_date = models.DateTimeField(auto_now_add=True)  # Automatically sets to now when created
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total cost of the order

    def __str__(self):
        return f"Order {self.id} - {self.customer.name}"

