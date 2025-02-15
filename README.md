# Complete System for Gym Management

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0.1-green)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3.34.0-yellowgreen)](https://www.sqlite.org/index.html)

## ✨ Main Features
- Customer registration with personal and payment information
- Subscription plan management (monthly/annual)
- Generation of unique hash for secure customer identification
- Interface for payment processing
- Thread-safe connection to SQLite database

## 🛠️ Technologies Used
- **Backend**: Flask, SQLite3
- **Frontend**: HTML5, CSS3, Jinja2
- **Segurança**: SHA-256 para hashing, chave secreta dinâmica
- **Gerenciamento de Dados**: SQLAlchemy-like raw queries

## ⚙️ Installation
1. **Prerequisites**:
   - Python 3.10+
   - pip
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```
2. **Run**:
   ```bash
   python app.py
   ```
   Acess: http://localhost:5000

## 🗂 Project Structure
```
.
├── templates/
│   ├── home/             # Home pages
│   ├── clients/          # Customer interface
│   └── manager/          # Admin dashboard
├── static/               # CSS, JS, and images
├── app.py                # Main application
├── db.py                 # Database configurations
└── requirements.txt      # Dependencies

```

## 📌 Main Routes
| Route                | Method | Description                    |
|---------------------|--------|------------------------------------|
| `/new_client/<plan>`| GET    | Customer Registration Form |


## 🔒 Security Considerations
- SHA-256 hash generation for customer identification
- Thread-safe connection to the database
- Basic form validation
- Dynamically generated secret key

## 🚀 Future Improvements
- [ ] Implement JWT authentication
- [ ] Add email notification system
- [ ] Create an admin dashboard
- [ ] Add unit tests with pytest
- [ ] Add a customer area
- [ ] Implement AI for personalized training plans

## 📄 Licença
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
