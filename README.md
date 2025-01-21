# Stock Management System

This project is a **Stock Management System** that allows users to manage products in a stock inventory. The system consists of a backend API built with FastAPI and a frontend built using Streamlit.

## Features

### Backend (FastAPI)
- **Add Product**: Create a new product with details like name, description, price, category, and supplier email.
- **View Products**: Retrieve all products or a specific product by its ID.
- **Update Product**: Update details of an existing product.
- **Delete Product**: Remove a product from the inventory.
- **Error Handling**: Provides detailed error messages for invalid operations.

### Frontend (Streamlit)
- **Add Product**: A form to add a new product to the inventory.
- **View Products**: Displays all products in a tabular format with their details.
- **Search Product**: Retrieve details of a specific product by its ID.
- **Delete Product**: Remove a product from the inventory by its ID.
- **Update Product**: Update product details using a form.

## Requirements

### Backend
- Python 3.8+
- FastAPI
- SQLAlchemy
- Uvicorn
- A database (e.g., SQLite, PostgreSQL)

### Frontend
- Python 3.8+
- Streamlit
- Pandas
- Requests

## Installation

### Backend
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/stock-management.git
   cd stock-management/backend
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the backend server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend
1. Navigate to the frontend directory:
   ```bash
   cd ../frontend
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the frontend:
   ```bash
   streamlit run app.py
   ```

## Usage

### Backend
- The backend API will be available at `http://localhost:8000`.
- You can use the interactive Swagger UI documentation at `http://localhost:8000/docs`.

### Frontend
- The Streamlit frontend will be available at `http://localhost:8501`.
- Use the interface to perform the following actions:
  - Add a new product.
  - View all products.
  - Search for a specific product by its ID.
  - Delete a product by its ID.
  - Update product details.

## API Endpoints

### Base URL: `http://localhost:8000`

| Method | Endpoint                  | Description                   |
|--------|---------------------------|-------------------------------|
| GET    | `/`                       | Welcome message               |
| GET    | `/products/`              | Retrieve all products         |
| GET    | `/products/{product_id}`  | Retrieve a product by ID      |
| POST   | `/products/`              | Add a new product             |
| DELETE | `/products/{product_id}`  | Delete a product by ID        |
| PUT    | `/products/{product_id}`  | Update a product by ID        |
