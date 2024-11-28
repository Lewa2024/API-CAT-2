# API-CAT-2
Question 1 Explanation

---Explanation of Relationships:---

Customer: Represents a person placing orders, identified by a name and email. Order: Represents an order placed by a customer. It includes: customer: A ForeignKey linking an order to a customer. on_delete=models.CASCADE: Ensures that if a customer is deleted, their orders are deleted as well. related_name='orders': Allows reverse access from Customer to their orders via customer.orders. order_date: Automatically records the date when the order was created. total_amount: Stores the monetary value of the order.

-- steps explanation-- Model Creation (models.py): Defines the structure and relationships of data in the database.

Migration Generation (makemigrations): Converts the Python model definitions into migration files (blueprints for the database).

Migration Application (migrate): Executes the migration files to create the actual database schema (tables, fields, relationships).

Admin Registration (admin.py): Makes the models manageable via Django's built-in admin interface, simplifying testing and debugging.

Test in Admin Panel: Verifies that relationships work as expected (e.g., orders correctly associate with customers).

This structure ensures scalable, maintainable, and intuitive management of customers and their orders in an e-commerce system. Each part of the code is designed to handle specific requirements
