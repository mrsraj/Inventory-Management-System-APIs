1. # Install Python
    Install python-3.7.2 and python-pip. Follow the steps from the below reference document based on your Operating System. Reference:
    https://docs.python-guide.org/starting/installation/

2. # Install MySQL  Beacause I have used Mysql Database to store data.
   Install mysql-8.0.15. Follow the steps form the below reference document based on your Operating System. Reference:
   https://dev.mysql.com/doc/refman/5.5/en/

4. # Setup virtual environment:
   with the help of below command
   py -m venv <name>

5. # Install Django
   Command: py -m pip install django
   Set up it.

6. # Install mysqlclient:
   Command: pip install mysqlclient

7. # Install Djangorestframework:
   Command: pip install djangorestframework

   After all process you have to run this command : py manage.py runserver without it you can't use APIs.
  
Here, I have created some APIs for simple inventory management System. In this project has 4 model(means Database table) like Product, Stock, User and Invoice.
Every model has specific data.

# Product Releted APIs:
APis to show all product :loacalhost/api/products
APIs for delete specific product: loacalhost/api/products/delete/<int:pk>
APIs for Update specific product: loacalhost/api/products/update/<int:pk>

# Users Releted APIs
   APIs for user : localhost/api/users
   APIs for specific user : localhost/api/users/<int:pk>
   APIs for delete user : localhost/api/user/delete/<int:pk>
   APIs for update user : localhost/api/user/update/<int:pk>

# Invoice Releted APIs:
   APIs for invoice all data : api/invoices
   APIs for invoice specific data : api/invoices/<int:pk>
   APIs for invoice delete data : api/invoicedata/delete/<int:pk>
   APIs for invoice update data : api/invoicedata/update/<int:pk>
          
 
   

   
 
