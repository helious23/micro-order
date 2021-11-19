from rest_framework import viewsets


class ShopViewSet(viewsets.ViewSet):
    def list(self, request):  # GET /api/shop
        pass

    def create(self, requsest):  # POST /api/shop
        pass

    def retrive(self, request, pk=None):  # GET /api/shop/<str:idx>
        pass

    def update(self, request, pk=None):  # PUT /api/shop/<str:idx>
        pass

    def destroy(self, request, pk=None):  # DELETE /api/shop/<str:idx>
        pass


class OrderViewSet(viewsets.ViewSet):
    def list(self, request):  # GET /api/order
        pass

    def create(self, requsest):  # POST /api/order
        pass

    def retrive(self, request, pk=None):  # GET /api/order/<str:idx>
        pass

    def update(self, request, pk=None):  # PUT /api/order/<str:idx>
        pass

    def destroy(self, request, pk=None):  # DELETE /api/order/<str:idx>
        pass
