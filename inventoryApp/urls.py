from django.urls import path
from . import views

urlpatterns = [
   
    ##Product Releted Path
    path('api/products', views.product_list, name='product-list'),
    path('api/products/delete/<int:pk>', views.delete_product, name='delete-product'),
    path('api/products/update/<int:pk>', views.update_product, name='update-product'),
    
    #Users Releted Path
    path('api/users', views.user_list, name = 'user_list'),
    path('api/users/<int:pk>', views.user_list, name = 'user_list'),
    path('api/users/delete/<int:pk>', views.delete_user, name='delete-user'),
    path('api/users/update/<int:pk>', views.update_user, name='update-user'),
     
     
    #path for delete invoice data
    path('api/invoices', views.invoice_list, name='invoice_list'),
    path('api/invoices/<int:pk>', views.invoice_list, name='invoice_list'),
    path('api/delete/invoicedata/<int:pk>', views.delete_invoice, name='delete_invoice'),
    #path for update invoice data
    path('api/invoices/update/<int:pk>', views.update_invoice, name='update-invoice'),
]