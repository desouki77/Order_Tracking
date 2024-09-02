import pandas as pd
from .models import Order

file_path = '/home/doss/Desktop/Django/order_tracking/orders.xlsx'

def load_orders_from_excel(file_path):
    df = pd.read_excel(file_path)
    for _, row in df.iterrows():
        Order.objects.create(
            orderId=row['orderId'],
            orderNmae=row['orderName'],
            username=row['username'],
            status=row['status']
        )
