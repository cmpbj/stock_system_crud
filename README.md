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

### Usage

#### Prerequisites
Ensure you have Docker and Docker Compose installed on your system. If not, follow the installation instructions for your operating system on the [Docker website](https://www.docker.com/).

#### Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/cmpbj/stock_system_crud.git
   cd stock-management
   ```

2. **Build and Start the Services**
   Use the `docker-compose` command to build and start all the services defined in the `docker-compose.yml` file:
   ```bash
   docker-compose up
   ```
   This will:
   - Set up a PostgreSQL database with the specified user, password, and database name.
   - Build and run the backend service, exposing it on port `8000`.
   - Build and run the frontend service, exposing it on port `8501`.

3. **Access the Services**
   - **Backend**: Open your browser or use a tool like `curl` to access the backend API at [http://localhost:8000](http://localhost:8000).
   - **Frontend**: Open your browser and navigate to [http://localhost:8501](http://localhost:8501) to access the frontend application.

4. **Stopping the Services**
   To stop the running containers, press `Ctrl+C` in the terminal where the services are running, then use:
   ```bash
   docker-compose down
   ```
   This will stop and remove all containers, networks, and volumes created by `docker-compose`.

#### Additional Notes
- **Persistent Data**: The PostgreSQL database data is stored in a Docker volume named `postgres_data`. This ensures data persistence across container restarts.
- **Modifying Code**: Since the `backend` and `frontend` services mount the local directories (`./backend` and `./frontend`), any changes you make to the code will be reflected immediately in the running containers (hot-reloading is enabled).
- **Logs**: To view logs for a specific service, use:
  ```bash
  docker-compose logs <service_name>
  ```
  Replace `<service_name>` with `backend`, `frontend`, or `postgres`.

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
