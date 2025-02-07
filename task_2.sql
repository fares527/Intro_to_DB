CRAETE DATABASE IF NOT EXISTS alx_book_store;
use alx_book_store;


CREATE TABLE Authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL,
)


CREATE TABLE Books (
    book_id INT  PRIMARY KEY,
    title VARCHAR(215) NOT NULL,
    author_id INT,
    price DOUBLE INT NOT NULL,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);


CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) UNIQUE NOT NULL,
    address TEXT,
);


CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
);

CREATE TABLE Order_Details (
    orderdetail_id INT PRIMARY KEY,
    order_id INT,
    book_id INT,
    quantity DOUBLE INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)

);
