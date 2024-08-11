from django.test import TestCase

# Create your tests here.
from .models import Book, Author, Customer, Order

class BookTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(username="John Doe", email="john@example.com")
        self.book = Book.objects.create(title="Sample Book", author=self.author, price=10.00, publication_date="2023-01-01", stock=100)

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Sample Book")
        self.assertEqual(self.book.stock, 100)

class OrderTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create_user(email="customer@example.com", password="password")
        self.author = Author.objects.create(username="John Doe", email="john@example.com")
        self.book = Book.objects.create(title="Sample Book", author=self.author, price=10.00, publication_date="2023-01-01", stock=100)

    def test_order_creation_with_discount(self):
        order = Order.objects.create(customer=self.customer, total_amount=9.00)
        order.books.add(self.book)
        self.assertEqual(order.total_amount, 9.00)