# API-CAT-2
Explanation of Relationships
A customer model indicates an individual who places orders through the e-commerce. It contains important fields such as name and email, which are sufficient enough to distinguish each customer. This model would, therefore, be a starting point on which data about customers will be managed.

Order model: this represents an order placed by one customer. It has a customer field, ForeignKey that links each order with a particular customer. The on_delete=models.CASCADE parameter ensures that if a customer is deleted, all of the orders associated with that customer are also removed from the database. This prevents data inconsistency. The related_name='orders' attribute allows reverse access so that obtaining all orders for a given customer is as easy as customer.orders. Other fields in the Order model are order_date, which is automatically set to the date the order was created, and total_amount, which will store the monetary value of the order.

Explanation of Steps
This system should first be implemented by creating the models in models.py. The structure of the data is defined, and a relationship between the Customer and Order models is established. It contains fields such as name, email, order_date, total_amount, and a ForeignKey relationship that will relate orders to customers.

With the models defined, the next step is migration generation using the command makemigrations. What this does is convert the Python model definitions into migration files; these are like blueprint instructions for creating tables and relationships in the database.

Next, with the creation of migrations, the application of the migrations using the migrate command is done. This applies the migration files to the database and creates the real schema, comprising tables, fields, and relationships as defined in the models.

In admin.py, the models have been registered to enable easy management of data. Customer and Order models can be accessed within Django's admin interface, where the developers and other users perform CRUD activities quite easily, thus simplifying their testing and debugging.

Finally, the admin panel was used to verify that the relations between models work as expected. As an example, after a customer was created, they could be linked with many orders, and vice-versa, deleting the customer removed their orders because of the on_delete=models.CASCADE behavior.


