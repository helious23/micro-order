from rest_framework import viewsets, status
from rest_framework.response import Response
from . import models, serializers, producer


class ShopViewSet(viewsets.ViewSet):
    def list(self, request):  # GET /api/shop
        shops = models.Shop.objects.all()
        serializer = serializers.ShopSerializer(shops, many=True)
        producer.publish()
        return Response(serializer.data)

    def create(self, request):  # POST /api/shop
        serializer = serializers.ShopSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # validation
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrive(self, request, pk=None):  # GET /api/shop/<str:idx>
        shop = models.Shop.objects.get(pk=pk)
        serializer = serializers.ShopSerializer(shop)
        return Response(serializer.data)

    def update(self, request, pk=None):  # PUT /api/shop/<str:idx>
        shop = models.Shop.objects.get(pk=pk)
        serializer = serializers.ShopSerializer(
            instance=shop, data=request.data
        )  # 해당 shop을 instance 로 받아온 다음 data 를 request.data 로 바꿈
        serializer.is_valid(raise_exception=True)  # validation
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):  # DELETE /api/shop/<str:idx>
        shop = models.Shop.objects.get(pk=pk)
        shop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderViewSet(viewsets.ViewSet):
    def list(self, request):  # GET /api/order
        orders = models.Order.objects.all()
        serializer = serializers.OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def create(self, request):  # POST /api/order
        serializer = serializers.OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrive(self, request, pk=None):  # GET /api/order/<str:idx>
        order = models.Order.objects.get(pk=pk)
        serializer = serializers.OrderSerializer(order)
        return Response(serializer.data)

    def update(self, request, pk=None):  # PUT /api/order/<str:idx>
        order = models.Order.objects.get(pk=pk)
        serializer = serializers.OrderSerializer(instance=order, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):  # DELETE /api/order/<str:idx>
        order = models.Order.objects.get(pk=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
