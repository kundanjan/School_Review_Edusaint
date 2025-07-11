# School Reviews Web Application

A Flask-based web application for submitting and viewing school reviews, built for the Edusaint Web Development Internship.

## 🎯 Features

- **Add Reviews**: Submit detailed reviews with school name, reviewer name, rating (1-5), and comments
- **View Reviews**: Browse all submitted reviews with search functionality
- **Clean UI**: Modern Bootstrap-based responsive design
- **Data Validation**: Comprehensive form validation and error handling
- **MySQL Integration**: Robust database operations with proper error handling
- **Search Functionality**: Real-time search through reviews
- **Statistics**: Dashboard showing total reviews, average rating, and schools reviewed

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Database**: MySQL
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 5.3
- **Icons**: Font Awesome 6.0
- **Database Driver**: mysql-connector-python
- **Configuration**: python-dotenv for environment variables

## 📁 Project Structure

```
school_review_app/
├── app.py                 # Main Flask application
├── templates/
│   ├── add_review.html    # Add review form
│   ├── reviews.html       # Display all reviews
│   ├── 404.html          # 404 error page
│   └── 500.html          # 500 error page
├── static/               # Static files (CSS, JS, images)
├── reviews.sql           # Database schema
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables
├── .gitignore           # Git ignore file
└── README.md            # This file
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- MySQL 8.0+
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd school_review_app
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Database Setup
1. Create MySQL database:
```sql
mysql -u root -p
source reviews.sql
```

2. Or manually create the database:
```sql
CREATE DATABASE school_reviews;
USE school_reviews;

CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    school_name VARCHAR(100) NOT NULL,
    reviewer_name VARCHAR(100) NOT NULL,
    rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5),
    comment TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

### Step 5: Configure Environment Variables
Create a `.env` file in the project root:
```env
DB_HOST=localhost
DB_NAME=school_reviews
DB_USER=root
DB_PASSWORD=your_mysql_password
SECRET_KEY=your-secret-key-change-this-in-production
```

### Step 6: Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 🔧 Configuration

### Database Configuration
The application uses environment variables for database configuration:
- `DB_HOST`: MySQL server host (default: localhost)
- `DB_NAME`: Database name (default: school_reviews)
- `DB_USER`: Database username (default: root)
- `DB_PASSWORD`: Database password
- `SECRET_KEY`: Flask secret key for sessions

### Remote Database Setup (Alternative)
You can use services like db4free.net for remote MySQL hosting:
```env
DB_HOST=db4free.net
DB_NAME=your_db_name
DB_USER=your_username
DB_PASSWORD=your_password
```

## 🎨 Key Features Explained

### 1. Code Structure & Clarity
- **Modular Design**: Separate classes for database operations and validation
- **Error Handling**: Comprehensive error handling with logging
- **Clean Code**: Well-documented, readable code with proper naming conventions
- **Configuration**: Environment-based configuration management

### 2. Flask + MySQL Integration
- **Database Manager Class**: Centralized database operations
- **Connection Pool**: Efficient database connection management
- **Transaction Safety**: Proper commit/rollback mechanisms
- **SQL Injection Prevention**: Parameterized queries

### 3. UI/UX Design
- **Modern Bootstrap Design**: Responsive, mobile-first design
- **Interactive Elements**: Star rating system, hover effects, animations
- **Search Functionality**: Real-time filtering of reviews
- **Visual Feedback**: Success/error messages, loading states
- **Accessibility**: Proper ARIA labels and semantic HTML

## 🔍 API Endpoints

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Redirect to add review page |
| `/add-review` | GET | Display add review form |
| `/add-review` | POST | Process form submission |
| `/reviews` | GET | Display all reviews |

## 🧪 Testing

### Manual Testing Checklist
- [ ] Form validation works correctly
- [ ] Database operations (insert/select) function properly
- [ ] Search functionality filters results accurately
- [ ] Responsive design works on different screen sizes
- [ ] Error handling displays appropriate messages
- [ ] Star rating system is interactive

### Sample Test Data
The `reviews.sql` file includes sample data for testing:
- 5 sample reviews
- Different ratings (3-5 stars)
- Various school types and comments

## 🔒 Security Features

- **Input Validation**: Server-side validation for all form inputs
- **SQL Injection Prevention**: Parameterized queries
- **XSS Protection**: Proper HTML escaping in templates
- **Environment Variables**: Sensitive data stored securely
- **Error Handling**: Graceful error handling without exposing system info

## 🎯 Performance Optimizations

- **Database Indexes**: Optimized queries with proper indexing
- **Connection Management**: Efficient database connection handling
- **Frontend Optimization**: Minified CSS/JS, optimized images
- **Caching**: Static file caching for better performance

## 📱 Responsive Design

The application is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile phones
- Different screen orientations

## 🚧 Future Enhancements

- User authentication and authorization
- Review editing and deletion
- Image uploads for schools
- Email notifications
- Advanced filtering and sorting
- Review moderation system
- REST API for mobile apps

## 📞 Support

For technical issues or questions:
1. Check the error logs in the console
2. Verify database connection settings
3. Ensure all dependencies are installed
4. Check Python and MySQL versions

## 📄 License

This project is created for educational purposes as part of the Edusaint Web Development Internship program.

---

**Created by**: [Your Name]  
**Date**: [Current Date]  
**Version**: 1.0.0