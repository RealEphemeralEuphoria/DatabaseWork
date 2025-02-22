# My Project

## Table of Contents
- [Introduction](#introduction)
- [What is SQL, and what does it do?](#what-is-sql-and-what-does-it-do)
- [Why SQL Matters](#why-sql-matters)
- [Usage](#usage)
- [SQL Examples](#sql-examples)
- [License](#license)

---

## Introduction
This project is designed to **self teach SQL, SQLite, and Markdown**. It includes properly formatted SQL code blocks that work cleanly in **VS Code and GitHub**.

---

## What is SQL, and what does it do?
This project is how I will **self-teach the concept of DBMS(s?) as well as key SQL methods.**  
SQL (**Structured Query Language**) is a programming language used to **manage and manipulate relational databases**.  
It allows users to **store, retrieve, update, and delete** data in a structured way.

Below are some examples.

---

## Why SQL Matters
SQL is **the backbone of business logic, integrations, and programmatic functionality**. It powers **applications, automates workflows, and drives business intelligence**. Here's how:

### **1. SQL Reflects Business Logic**
SQL enforces the rules businesses rely on. A company selling products online needs to store **customer details, orders, and inventory**.

```sql
-- Stores customer information
CREATE TABLE customers (
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL, 
    email TEXT UNIQUE
);

-- Stores orders linked to customers
CREATE TABLE orders (
    id INTEGER PRIMARY KEY, 
    customer_id INTEGER, 
    order_date DATE,
    total_price DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
```

📌 **Why this matters:**  
- Prevents **duplicate emails** with a `UNIQUE` constraint.  
- Ensures **orders are linked to real customers**.  
- Enables **sales tracking and customer analytics**.

---

### **2. SQL Powers Business Data Storage**
A **relational database** consists of **structured tables** that track key business components.

| **Business Function** | **Table Name** | **What It Tracks** |
|----------------------|--------------|----------------|
| **Users & Accounts** | `users` | Name, email, login credentials |
| **Products & Inventory** | `products` | Stock levels, pricing, descriptions |
| **Transactions** | `payments` | Purchase history, refund tracking |
| **Support Tickets** | `support_tickets` | Issue details, resolution time |
| **Employees** | `employees` | Salaries, roles, performance reviews |

📌 **Why this matters:**  
- Keeps **data structured, consistent, and scalable**.  
- **Indexes improve search speed** for faster queries.  

---

### **3. SQL Enables Integrations**
Most businesses rely on multiple software platforms that **need to exchange data**. SQL helps connect these systems.

#### **Example: Syncing an Online Store with a Shipping System**
1️⃣ **Customer places an order** → Stored in the `orders` table.  
2️⃣ **Warehouse needs order details** → A SQL query fetches new orders.  
3️⃣ **Shipping system sends tracking info** → SQL updates the `orders` table.

```sql
-- Mark order as shipped and add tracking info
UPDATE orders 
SET status = 'Shipped', tracking_number = '1Z999AA10123456784' 
WHERE id = 123;
```

📌 **Why this matters:**  
- Prevents **duplicate or lost orders**.  
- Enables **real-time order tracking**.  

---

### **4. SQL in Applications**
SQL is used **programmatically** in applications to fetch and manipulate data in real time.

#### **Example: A Python Web App Fetching User Data**
```python
import sqlite3

conn = sqlite3.connect('store.db')
cursor = conn.cursor()

user_email = 'euphoria@example.com'
cursor.execute("SELECT * FROM users WHERE email = ?", (user_email,))
user_data = cursor.fetchone()

print(user_data)  # Outputs: (1, 'Euphoria', 'euphoria@example.com')
```

📌 **Why this matters:**  
- **Personalized user experiences** → Fetches recommendations & past orders.  
- **Security** → Uses **parameterized queries** to prevent SQL injection.  

---

### **5. SQL in Business Analytics**
SQL powers **business dashboards and decision-making tools**.

#### **Example: Monthly Sales Reports**
```sql
SELECT strftime('%Y-%m', order_date) AS month, 
       SUM(total_price) AS total_revenue
FROM orders
GROUP BY month
ORDER BY month DESC;
```

📌 **Why this matters:**  
- Helps **identify sales trends** (peak seasons).  
- Supports **budget allocation and pricing strategies**.  

---

### **6. SQL is Everywhere**
| **SQL Concept** | **Business Impact** | **Example** |
|---------------|----------------|----------|
| **Tables & Relationships** | Store structured data efficiently | Users, orders, inventory |
| **Joins & Queries** | Connect business insights across tables | Sales trends, user retention |
| **Indexes & Performance** | Speed up searches | Fast customer lookups |
| **ETL & Data Integration** | Sync data between different platforms | E-commerce → Shipping APIs |
| **Automation & Triggers** | Auto-update records | Mark orders as "Shipped" |
| **Security & Access Control** | Protect sensitive data | Role-based permissions |

📌 **SQL is the foundation of modern business intelligence, automation, and integrations.**

---

## SQL Examples

### Insert Data
```sql
-- Adds a new user to the table
INSERT INTO users (id, name, age) 
VALUES (1, 'Euphoria', 30);
```

### Select Data
```sql
-- Retrieves all users older than 21
SELECT * 
FROM users 
WHERE age > 21;
```

### Update Data
```sql
-- Updates Euphoria's age in the database
UPDATE users 
SET age = 31 
WHERE name = 'Euphoria';
```

### Delete Data
```sql
-- Removes a user from the table based on ID
DELETE FROM users
WHERE id = 1;
```

### Create Table
```sql
-- Creates a table to store user information
CREATE TABLE users (
    id INTEGER PRIMARY KEY, -- Unique user ID
    name TEXT NOT NULL, -- User's name (required)
    age INTEGER -- User's age
);
```

### Drop Table
```sql
-- Deletes the users table if it exists
DROP TABLE IF EXISTS users;
```

### Case Statement Example
```sql
-- Categorizes users based on their age group
SELECT name,  
    CASE  
        WHEN age < 18 THEN 'Minor'  -- Under 18
        WHEN age >= 18 AND age < 65 THEN 'Adult'  -- Between 18 and 64
        ELSE 'Senior'  -- 65 and older
    END AS age_group 
FROM users;
```

---