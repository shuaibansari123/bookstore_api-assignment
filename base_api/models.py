from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings 

class BaseModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CustomerManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Customer(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomerManager()

    def is_first_time_user(self):
        # using reverse-relation , if user has placed any order before, it return false
        return not self.order_set.exists()

    class Meta:
        indexes = [
            models.Index(fields=['email']),  
        ]

class Author(Customer):
    '''
    we can use OneToOneField relation instead of inheritance'''
    class Meta:
        indexes = [
            #models.Index(fields=['email']),  
            # can use unique_together , order_by  , UniqueConstraintCheckS etc.
        ]

class Book(BaseModelMixin):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publication_date = models.DateField()
    stock = models.PositiveIntegerField()

    class Meta:
        indexes = [
            # can modify this as per requirements and needs
            models.Index(fields=['title']),  # Index for faster title searches
            models.Index(fields=['author']),  # Index for foreign key lookups
            models.Index(fields=['price']),  # Index for filtering by price
        ]

class Order(BaseModelMixin):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    indexes = [
            # models.Index(fields=['customer']),  
            # because of fk field automatically create index behind the scene we dont need to create seperate
            models.Index(fields=['total_amount']),  # Index for amount-based queries
        ]
    