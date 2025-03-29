# im-backend Project

## Overview
This project is a backend application built using Python and Flask. It serves as a foundation for developing web applications with a structured approach, separating concerns into different modules.

## Project Structure
```
im-backend
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── controllers
│   │   └── __init__.py
│   ├── models
│   │   └── __init__.py
│   ├── routes
│   │   └── __init__.py
│   └── utils
│       └── __init__.py
├── requirements.txt
├── .env
└── README.md
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd im-backend
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

5. **Set up environment variables**:
   Create a `.env` file in the root directory and add your configuration variables.

## Usage

To run the application, execute the following command:
```
python app/main.py
```

The application will start on the default Flask port (5000). You can access it at `http://localhost:5000`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.