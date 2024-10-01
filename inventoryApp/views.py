from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from .models import Invoice, User,Product,Stock
from .serializers import InvoiceSerializer, UserSerializer, ProductSerializer


#Auth
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    
@api_view(['DELETE'])
def delete_product(request, pk):
    try:
        # Try to get the product by primary key (id)
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        # If the product does not exist, return a 404 response
        return Response({'error': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)

    # If the product exists, delete it
    product.delete()

    # Return a 204 No Content status to indicate successful deletion
    return Response({'message': 'Product deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def update_product(request, pk):
    try:
        # Try to get the product by primary key (id)
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        # If the product does not exist, return a 404 response
        return Response({'error': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)

    # Use the serializer to validate and update the product
    serializer = ProductSerializer(product, data=request.data, partial=True)  # partial=True allows partial updates
    if serializer.is_valid():
        serializer.save()  # Save the updated product
        return Response(serializer.data, status=status.HTTP_200_OK)  # Return the updated product data
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors
    
    
    
##user releted functions:
    
@api_view(['GET'])
def user_list(request, pk=None):
    # Fetch a specific member if pk is provided
    if pk:
        try:
            rec = User.objects.get(pk=pk)
            serializer = UserSerializer(rec)
            return JsonResponse({"data": serializer.data}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return JsonResponse({'error': 'users not found'}, status=status.HTTP_404_NOT_FOUND)

    # Fetch all members if pk is not provided
    else:
        users = User.objects.all()
        if users.exists():
            serializer = UserSerializer(users, many=True)
            return JsonResponse({"data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error': 'No users found'}, status=status.HTTP_404_NOT_FOUND)
        
        
@api_view(['DELETE'])
def delete_user(request, pk):
    try:
        # Try to get the user by primary key (id)
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        # If the user does not exist, return a 404 response
        return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    # If the user exists, delete it
    user.delete()

    # Return a 204 No Content status to indicate successful deletion
    return Response({'message': 'User deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def update_user(request, pk):
    try:
        # Try to get the user by primary key (id)
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        # If the user does not exist, return a 404 response
        return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    # Use the serializer to validate and update the user
    serializer = UserSerializer(user, data=request.data, partial=True)  # partial=True allows partial updates
    if serializer.is_valid():
        serializer.save()  # Save the updated user
        return Response(serializer.data, status=status.HTTP_200_OK)  # Return the updated user data
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors

    



##Invoice releted functions:

@api_view(['GET'])
def invoice_list(request, pk=None):
    if pk:
        invoicedata = Invoice.objects.get(pk=pk)
        serializer = InvoiceSerializer(invoicedata)
        return JsonResponse({"invoicedata": serializer.data}, status=status.HTTP_200_OK)
    else:
        invoicedata = Invoice.objects.all()
        if invoicedata.exists():
            serializer = InvoiceSerializer(invoicedata, many=True )
            return JsonResponse({"invoicedata": serializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error': 'No invoicedata found'}, status=status.HTTP_404_NOT_FOUND)
        
   
@api_view(['DELETE'])
def delete_invoice(request, pk):
    try:
        # Try to get the invoice by primary key (id)
        invoice = Invoice.objects.get(pk=pk)
    except Invoice.DoesNotExist:
        # If the invoice does not exist, return a 404 response
        return Response({'error': 'Invoice not found.'}, status=status.HTTP_404_NOT_FOUND)

    # If the invoice exists, delete it
    invoice.delete()

    # Return a 204 No Content status to indicate successful deletion
    return Response({'message': 'Invoice deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def update_invoice(request, pk):
    try:
        # Try to get the invoice by primary key (id)
        invoice = Invoice.objects.get(pk=pk)
    except Invoice.DoesNotExist:
        # If the invoice does not exist, return a 404 response
        return Response({'error': 'Invoice not found.'}, status=status.HTTP_404_NOT_FOUND)

    # Use the serializer to validate and update the invoice
    serializer = InvoiceSerializer(invoice, data=request.data, partial=True)  # partial=True allows partial updates
    if serializer.is_valid():
        serializer.save()  # Save the updated invoice
        return Response(serializer.data, status=status.HTTP_200_OK)  # Return the updated invoice data
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors


