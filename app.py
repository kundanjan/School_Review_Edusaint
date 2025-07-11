#!/usr/bin/env python3
"""
School Review Flask Application
Created for Edusaint Web Development Internship
"""

from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Database configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'database': os.getenv('DB_NAME', 'school_reviews'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_unicode_ci'
}

class DatabaseManager:
    """Handles all database operations with proper error handling"""
    
    @staticmethod
    def get_connection():
        """Create and return a database connection"""
        try:
            connection = mysql.connector.connect(**DB_CONFIG)
            if connection.is_connected():
                return connection
        except Error as e:
            logger.error(f"Database connection error: {e}")
            return None
    
    @staticmethod
    def execute_query(query, params=None, fetch=False):
        """Execute a database query with error handling"""
        connection = None
        cursor = None
        try:
            connection = DatabaseManager.get_connection()
            if not connection:
                return None
            
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, params or ())
            
            if fetch:
                result = cursor.fetchall()
                return result
            else:
                connection.commit()
                return cursor.rowcount
                
        except Error as e:
            logger.error(f"Database query error: {e}")
            if connection:
                connection.rollback()
            return None
        finally:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()

class ReviewValidator:
    """Validates review form data"""
    
    @staticmethod
    def validate_review(data):
        """Validate review form data"""
        errors = []
        
        # School name validation
        if not data.get('school_name', '').strip():
            errors.append("School name is required")
        elif len(data['school_name'].strip()) > 100:
            errors.append("School name must be less than 100 characters")
        
        # Reviewer name validation
        if not data.get('reviewer_name', '').strip():
            errors.append("Reviewer name is required")
        elif len(data['reviewer_name'].strip()) > 100:
            errors.append("Reviewer name must be less than 100 characters")
        
        # Rating validation
        try:
            rating = int(data.get('rating', 0))
            if rating < 1 or rating > 5:
                errors.append("Rating must be between 1 and 5")
        except (ValueError, TypeError):
            errors.append("Rating must be a valid number")
        
        # Comment validation
        if not data.get('comment', '').strip():
            errors.append("Comment is required")
        elif len(data['comment'].strip()) > 1000:
            errors.append("Comment must be less than 1000 characters")
        
        return errors

# Routes
@app.route('/')
def index():
    """Home page - redirect to add review"""
    return redirect(url_for('add_review'))

@app.route('/add-review', methods=['GET', 'POST'])
def add_review():
    """Handle adding new reviews"""
    if request.method == 'POST':
        # Get form data
        form_data = {
            'school_name': request.form.get('school_name', '').strip(),
            'reviewer_name': request.form.get('reviewer_name', '').strip(),
            'rating': request.form.get('rating', ''),
            'comment': request.form.get('comment', '').strip()
        }
        
        # Validate form data
        errors = ReviewValidator.validate_review(form_data)
        
        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('add_review.html', form_data=form_data)
        
        # Insert into database
        insert_query = """
            INSERT INTO reviews (school_name, reviewer_name, rating, comment)
            VALUES (%s, %s, %s, %s)
        """
        
        result = DatabaseManager.execute_query(
            insert_query,
            (form_data['school_name'], form_data['reviewer_name'], 
             int(form_data['rating']), form_data['comment'])
        )
        
        if result:
            flash('Review added successfully!', 'success')
            return redirect(url_for('reviews'))
        else:
            flash('Error adding review. Please try again.', 'error')
    
    return render_template('add_review.html')

@app.route('/reviews')
def reviews():
    """Display all reviews"""
    query = """
        SELECT id, school_name, reviewer_name, rating, comment, 
               DATE_FORMAT(created_at, '%Y-%m-%d %H:%i') as created_at
        FROM reviews 
        ORDER BY id DESC
    """
    
    reviews_data = DatabaseManager.execute_query(query, fetch=True)
    
    if reviews_data is None:
        flash('Error loading reviews. Please try again.', 'error')
        reviews_data = []
    
    return render_template('reviews.html', reviews=reviews_data)

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Check database connection on startup
    test_connection = DatabaseManager.get_connection()
    if test_connection:
        logger.info("Database connection successful")
        test_connection.close()
    else:
        logger.error("Failed to connect to database")
    
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)