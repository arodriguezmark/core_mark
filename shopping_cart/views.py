from django.core.serializers import serialize
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from shopping_cart.models import ShoppingCart, Item
from shopping_cart.serializers import ShoppingCartSerializer, ShowShoppingCartSerializer


# from shopping_cart.serializers import ShoppingCartSerializer


class ShoppingCartDetail(APIView):
    """
    View to create, update or delete a ShoppingCart object.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = ShoppingCartSerializer
    renderer_classes = [JSONRenderer]

    def post(self, request, *args, **kwargs):
        customer_id = self.request.query_params.get('customer_id', None)
        if customer_id:
            try:
                shopping_cart = ShoppingCart.objects.get(customer_id=customer_id)
            except ShoppingCart.DoesNotExist:
                return Response({'message': 'Customer does not have a shopping cart'},
                                status=status.HTTP_400_BAD_REQUEST)
            shopping_cart_items = shopping_cart.items.all()
            items = request.data['items']
            serializer = ShowShoppingCartSerializer(shopping_cart)

            for item in items:
                try:
                    if shopping_cart_items.count() == 0:
                        raise KeyError
                    for shopping_cart_item in shopping_cart_items:
                        if shopping_cart_item.id == item['id']:
                            if item['quantity'] == 0:
                                shopping_cart_item.delete()
                                continue
                            if item['quantity'] != shopping_cart_item.quantity:
                                shopping_cart_item.quantity = item['quantity']
                                shopping_cart.item.total_price = item['quantity'] * item['price']
                                shopping_cart_item.save()
                        else:
                            continue

                except KeyError:
                    new_item = Item.objects.create(
                        price=item['price'],
                        quantity=item['quantity'],
                        total_price=item['price'] * item['quantity']
                    )
                    shopping_cart.items.add(new_item)
                    continue

            return Response(serializer.data, status=status.HTTP_200_OK)

        serializer = ShoppingCartSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        customer_id = self.request.query_params.get('customer_id', None)

        if customer_id:
            try:
                shopping_cart = ShoppingCart.objects.get(customer_id=customer_id)
                shopping_cart.delete()
                return Response({'message': 'Shopping cart delete successfully'}, status=status.HTTP_200_OK)
            except ShoppingCart.DoesNotExist:
                return Response({'message': 'Customer does not have a shopping cart'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': "'customer_id' cannot be null"}, status=status.HTTP_400_BAD_REQUEST)
