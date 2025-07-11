-- Database Schema for School Reviews Application
-- Created for Edusaint Web Development Internship

-- Create database
CREATE DATABASE IF NOT EXISTS school_reviews;
USE school_reviews;

-- Create reviews table
CREATE TABLE IF NOT EXISTS reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    school_name VARCHAR(100) NOT NULL,
    reviewer_name VARCHAR(100) NOT NULL,
    rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5),
    comment TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create index for better performance
CREATE INDEX idx_school_name ON reviews(school_name);
CREATE INDEX idx_rating ON reviews(rating);
CREATE INDEX idx_created_at ON reviews(created_at);

-- Insert sample data for testing
INSERT INTO reviews (school_name, reviewer_name, rating, comment) VALUES 
('Springfield Elementary', 'John Smith', 4, 'Great school with excellent teachers. My child loves going there every day.'),
('Oakwood High School', 'Sarah Johnson', 5, 'Outstanding academic programs and extracurricular activities. Highly recommend!'),
('Riverside Middle School', 'Mike Davis', 3, 'Average school. Could improve on communication with parents.'),
('Greenfield Academy', 'Emily Wilson', 5, 'Exceptional faculty and beautiful campus. Best decision for my child education.'),
('Westside Primary', 'David Brown', 4, 'Good school with caring teachers. Small class sizes which is great.');

-- Show table structure
DESCRIBE reviews;

-- Show sample data
SELECT * FROM reviews ORDER BY created_at DESC; 