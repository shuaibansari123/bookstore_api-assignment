**Django Bookstore API**
This is a Django-based RESTful API for a bookstore, featuring custom user authentication, advanced filtering, searching, pagination, and detailed logging. The application includes models for Author, Book, Customer, and Order, and is equipped with custom exception handling, caching, and Swagger API documentation.

**Features**
**Custom Authentication**: Utilizes a custom user model (Customer) with email-based authentication.
**Custom Managers**: Includes CustomerManager for user creation and management.
**Custom Mixins**: Provides CustomLoggingMixin for request logging and CustomerPagination for pagination.
**Custom Exception Handling**: Implements CustomNotFoundException for better error management.
**Advanced Filtering and Searching**: Employs DjangoFilterBackend, SearchFilter, and OrderingFilter.
**Indexing**: Optimized database queries with custom indexes.
**Pagination**: Implements custom pagination with CustomerPagination.
**Swagger API Documentation**: Automated API documentation using Swagger.
**Caching**: (Placeholder) Future plans to integrate caching for improved performance.
**Logging**: Detailed request and operation logging.


Endpoints

GET /swagger/: API Documentation (FIND ALL API ENDPOINTS HERE EASILY)

Authors
    GET /authors/: List all authors
    POST /authors/: Create a new author
    GET /authors/{id}/: Retrieve an author
    PUT /authors/{id}/: Update an author
    DELETE /authors/{id}/: Delete an author

Books
    GET /books/: List all books
    POST /books/: Create a new book
    GET /books/{id}/: Retrieve a book
    PUT /books/{id}/: Update a book
    DELETE /books/{id}/: Delete a book
    GET **/books/search/**: Search for books by title

Customers
    GET /customers/: List all customers
    POST /customers/: Create a new customer
    GET /customers/{id}/: Retrieve a customer
    PUT /customers/{id}/: Update a customer
    DELETE /customers/{id}/: Delete a customer

Orders
    GET /orders/: List all orders
    POST /orders/: Create a new order
    GET /orders/{id}/: Retrieve an order
    PUT /orders/{id}/: Update an order
    DELETE /orders/{id}/: Delete an order


Custom Components
    Custom User and Authentication Backend

User Model: Customer with email-based and username-based authentication.
    Manager: CustomerManager for user operations.

Custom Mixins
    CustomLoggingMixin: Logs requests and operations for debugging and monitoring.

Custom Pagination
    CustomerPagination: Custom pagination settings for API responses.

Custom Exception Handling
    CustomNotFoundException: Handles cases where an object is not found.

Logging
    Operation Logging: Logs actions on models (Author, Book, Customer, Order).

Caching (Future Enhancement)
    Plans to integrate caching to enhance performance and reduce database load.

Swagger API Documentation
    Endpoint: /swagger/ (Access Swagger UI for interactive API documentation.)

Installation
Clone the Repository
    git clone https://github.com/shuaibansari123/bookstore_api-assignment
    cd bookstore

Set Up Virtual Environment
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install Dependencies
    pip install -r requirements.txt

Apply Migrations
    python manage.py migrate

Run the Server
    python manage.py runserver

Access Swagger Documentation
Open http://localhost:8000/swagger/ in your browser.

Testing
Run tests with:
    python manage.py test

Run Docker-compose in detach mode
    docker-compose up --build -d

Custom Test Cases
    Unit Tests: Test individual model methods and views.
    Integration Tests: Test the interactions between different components.

Contribution
Feel free to open issues or submit pull requests if you want to contribute to this project.

License
This project is licensed under the MIT License - see the LICENSE file for details.




