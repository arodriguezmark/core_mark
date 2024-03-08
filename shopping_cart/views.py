from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from shopping_cart.models import ShoppingCart
from shopping_cart.serializers import ShoppingCartSerializer


class ShoppingCartDetail(APIView):
    """
    View to create a ShoppingCart object.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = ShoppingCartSerializer
    renderer_classes = [JSONRenderer]

    def post(self, request, *args, **kwargs):
        customer_id = self.request.query_params.get('customer_id', None)
        # if customer_id:
        #     try:
        #         cart = ShoppingCart.objects.get(customer_id=customer_id)
        #         serializer = ShoppingCartSerializer(cart, data=request.data)
        #         if serializer.is_valid():
        #             serializer.save()
        #             return Response(serializer.data, status=status.HTTP_200_OK)
        #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #     except ShoppingCart.DoesNotExist:
        #         return Response({"detail": "Shopping cart does not exist for this customer"},
        #                         status=status.HTTP_404_NOT_FOUND)
        #
        # else:
        serializer = ShoppingCartSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
