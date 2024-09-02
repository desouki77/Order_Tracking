from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order

class OrderTracking(APIView):
    def get(self, request):

        # Fetch all orders 
        orders = Order.objects.all()  
        
        # Manually serialize the orders into a list of dictionaries
        order_list = [
            {
                'orderId': order.orderId,
                'orderName': order.orderName,
                'username': order.username,
                'status': order.status
            }
            for order in orders
        ]
        
        return Response(order_list)
    
    def post(self, request):
        data = request.data  
        
        required_fields = ['orderID', 'orderName', 'username', 'status']
        for field in required_fields:
            if field not in data:
                return Response(
                    {'error': f'Missing field: {field}'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        
        # Create a new Order instance with the validated data
        order = Order(
            orderID=data['orderID'],
            orderName=data['orderName'],
            username=data['username'],
            status=data['status']
        )
        
        # Try to save the order to the database and handle any errors
        try:
            order.save()
            return Response(
                {
                    'orderId': order.orderId,
                    'orderName': order.orderName,
                    'username': order.username,
                    'status': order.status
                },
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
