from django.shortcuts import render

from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book, Author, Customer, Order
from .serializers import BookSerializer, AuthorSerializer, CustomerSerializer, OrderSerializer
from .utility import CustomLoggingMixin, CustomerPagination, CustomNotFoundException

class AuthorViewSet(CustomLoggingMixin, viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['email', 'username']
    ordering_fields = ['created_at']
    filterset_fields = ['username', 'is_active']
    pagination_class = CustomerPagination
    # override default auth and perms
    # authentication_classes = []
    # permission_classes = []
    # throttle_classes = []

    def list(self, request, *args, **kwargs):
        self.log_request(request)
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_object(self):
        try:
            return super().get_object()
        except Author.DoesNotExist:
            raise CustomNotFoundException()

    def retrieve(self, request, *args, **kwargs):
        self.log_request(request)
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        self.log_request(request)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.log_request(request)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.log_request(request)
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        author = serializer.save()
        logger.info(f"Author '{author.username}' created with ID {author.id}")

    def perform_update(self, serializer):
        author = serializer.save()
        logger.info(f"Author '{author.username}' updated with ID {author.id}")

class BookViewSet(CustomLoggingMixin, viewsets.ModelViewSet):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'author__username']
    ordering_fields = ['created_at']
    filterset_fields = ['price', 'publication_date']
    pagination_class = CustomerPagination
    # throttle_classes = []
    # authentication_classes = []
    # permission_classes = []

    @action(detail=False, methods=['get'], url_path='search')
    def search(self, request):
        self.log_request(request)
        query = request.query_params.get('q', '')
        books = self.queryset.filter(title__icontains=query)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        self.log_request(request)
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_object(self):
        try:
            return super().get_object()
        except Book.DoesNotExist:
            raise CustomNotFoundException()

    def retrieve(self, request, *args, **kwargs):
        self.log_request(request)
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        self.log_request(request)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.log_request(request)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.log_request(request)
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        book = serializer.save()
        logger.info(f"Book '{book.title}' created with ID {book.id}")

    def perform_update(self, serializer):
        book = serializer.save()
        logger.info(f"Book '{book.title}' updated with ID {book.id}")

class CustomerViewSet(CustomLoggingMixin, viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # override default auth and perms
    # authentication_classes = []
    # permission_classes = []
    # throttle_classes = []
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['email', 'username']
    ordering_fields = ['created_at']
    filterset_fields = ['username', 'is_active']
    pagination_class = CustomerPagination

    def list(self, request, *args, **kwargs):
        self.log_request(request)
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_object(self):
        try:
            return super().get_object()
        except Customer.DoesNotExist:
            raise CustomNotFoundException()

    def retrieve(self, request, *args, **kwargs):
        self.log_request(request)
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        self.log_request(request)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.log_request(request)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.log_request(request)
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        customer = serializer.save()
        logger.info(f"Customer '{customer.username}' created with ID {customer.id}")

    def perform_update(self, serializer):
        customer = serializer.save()
        logger.info(f"Customer '{customer.username}' updated with ID {customer.id}")

class OrderViewSet(CustomLoggingMixin, viewsets.ModelViewSet):
    queryset = Order.objects.select_related('customer').prefetch_related('books').all()
    serializer_class = OrderSerializer
    # override default auth and perms
    # authentication_classes = []
    # permission_classes = []
    # throttle_classes = []
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['customer', 'total_amount']
    ordering_fields = ['created_at']
    filterset_fields = ['total_amount']
    pagination_class = CustomerPagination

    def create(self, request, *args, **kwargs):
        data = request.data
        customer_id = data.get('customer')
        book_ids = list(data.get('books', []))
        customer = Customer.objects.get(id=customer_id)
        total_amount = 0

        for book_id in book_ids:
            book = Book.objects.get(id=book_id)
            if book.stock < 1:
                return Response({"error": f"Book '{book.title}' is out of stock."}, status=status.HTTP_400_BAD_REQUEST)
            total_amount += book.price
            book.stock -= 1
            book.save()

        # Apply discount for first-time users
        if customer.is_first_time_user():
            discount_type = settings.DISCOUNT_TYPE
            discount_value = settings.DISCOUNT_VALUE

            if discount_type == 'flat':
                total_amount -= discount_value
            elif discount_type == 'percentage':
                total_amount *= (1 - discount_value / 100)

        order = Order.objects.create(customer=customer, total_amount=total_amount)
        order.books.set(book_ids)
        order.save()
        
        # log request
        self.log_request(request)
        # delete old cached data 
        # cache.delete('Order_list')
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        self.log_request(request)
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_object(self):
        try:
            return super().get_object()
        except Order.DoesNotExist:
            raise CustomNotFoundException()

    def retrieve(self, request, *args, **kwargs):
        self.log_request(request)
        return super().retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        self.log_request(request)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.log_request(request)
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        order = serializer.save()
        logger.info(f"Order '{order.title}' created with ID {order.id}")

    def perform_update(self, serializer):
        order = serializer.save()
        logger.info(f"Order '{order.title}' updated with ID {order.id}")