# import base64
# import requests
# from .models import CarritoItem, Orden, Cliente
# #Crea una constante
# PAYPAL_CLIENT_ID="AfwFUHPafT-vOj_SoJWkKyp1_HxL9xLNbOqPE4h6u0el0pPihazwu2bmN2MrG6-qGikEU7bVXJCR-YOp"
# PAYPAL_CLIENT_SECRET="EGbzhHjrlADRFK-sanKKzXm7IY41Rxv0SaGG5lP21AM_YocBgk40qW1Md2pbOyiv2e_ULDdyFckeVW9C"
# #sandbox pruebas
# BASE_URL="https://api-m.sandbox.paypal.com"
# def generateAccessToken():
#     if not PAYPAL_CLIENT_ID or not PAYPAL_CLIENT_SECRET:
#         raise ValueError("no hay credenciales")
#     auth = f"{PAYPAL_CLIENT_ID}:{PAYPAL_CLIENT_SECRET}"
#     auth = base64.b64encode(auth.encode()).decode('utf-8')
    
#     response = requests.post(
#         "https://api-m.sandbox.paypal.com/v1/oauth2/token",
#         data={"grant_type": "client_credentials"},
#         headers={"Authorization": f"Basic {auth}"}
#     )

#     data = response.json()
#     return data['access_token']

# def create_order(carrito_items):
#     try:
#         carrito_items = CarritoItem.objects.all()

#         # Crear una nueva orden
       
#         total = sum(item.total for item in carrito_items)
#         access_token = generateAccessToken()
#         total=total/18
        
#         url = "https://api-m.sandbox.paypal.com/v2/checkout/orders"
#         payload = {
#             "intent": "CAPTURE",
#             "purchase_units": [
#                 {
#                     "amount": {
#                         "currency_code": "USD",
#                         "value": str(total)  # Convertir el total a cadena
#                     }
#                 }
#             ]
#         }
#         headers = {
#             "Content-Type": "application/json",
#             "Authorization": f"Bearer {access_token}",
#         }
#         response = requests.post(url, headers=headers, json=payload)
#         print("Order response from PayPal:", response.json())
#         return response.json()
#     except Exception as error:
#         print("Error creating order:", error)

# def capture_order(orderID):
#     print("Capturing PayPal order ID:", orderID)
#     try:
#         access_token = generateAccessToken()
#         url = f"https://api-m.sandbox.paypal.com/v2/checkout/orders/{orderID}/capture"
#         headers = {
#             "Content-Type": "application/json",
#             "Authorization": f"Bearer {access_token}",
#         }
#         response = requests.post(url, headers=headers)
#         print("Capture response from PayPal:", response.json())
#         return response.json()
#     except Exception as error:
#         print("Error capturing order:", error)