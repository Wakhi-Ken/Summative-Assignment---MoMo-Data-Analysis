<h1>Fullstack SMS Data Processing Application</h1>
Assignment Overview

Here is the Link of Documentation : 

This project focuses on creating and implementing a comprehensive full-stack application designed to handle SMS data in XML format. The system will clean, categorize, and store the data in a relational database, while also providing a user-friendly front-end for analysis and visualization.

The dataset consists of around 1600 SMS messages from MTN MoMo, a mobile payment service provider in Rwanda. The primary objective is to extract valuable insights from the data and display them on an interactive dashboard for easy exploration.

Learning Objectives
By completing this assignment, you will:

Apply data cleaning and categorization techniques to extract insights from raw data.
Design and implement a relational database schema for structured data storage.
Develop a backend to handle database operations and integrate it with a frontend application.
Build an interactive and user-friendly dashboard using HTML, CSS, and JavaScript.
Demonstrate end-to-end problem-solving skills in fullstack application development.
Deliverables
Python/JS Scripts: For data cleaning, processing, and populating the database.
Database Schema: Relational database design for SMS data storage.
Frontend Interface: A dashboard to visualize and interact with the data.
Documentation: A report explaining the approach, design decisions, and functionality of the application.

Assignment Tasks

1. Data Cleaning and Processing (Backend)
Data Extraction
Parse the provided XML file using JavaScript or Python libraries (e.g., xml.etree.ElementTree, lxml, BeautifulSoup).
Extract and categorize SMS messages into the following types:
Incoming Money
Payments to Code Holders
Transfers to Mobile Numbers
Bank Deposits
Airtime Bill Payments
Cash Power Bill Payments
Transactions Initiated by Third Parties
Withdrawal from Agents
Bank Transfers
Internet and Voice Bundle Purchases
Other

2. Database Design and Implementation
Relational Database
Design a schema that captures all relevant fields for each transaction type.
Use SQLite, MySQL, or PostgreSQL for database implementation.
Data Insertion
Develop a script to insert the cleaned and categorized data into the database.
Ensure data integrity and handle duplicates or conflicting entries.

3. Frontend Dashboard Development
Dashboard Requirements
Build an interactive dashboard using HTML, CSS, and JavaScript.

Implement the following features:

Search and Filter: Enable users to search and filter transactions by type, date, or amount.
Visualizations: Use charts (e.g., bar charts, pie charts) to display:
Total transaction volume by type.
Monthly summaries of transactions.
Distribution of payments and deposits.
Additional relevant visualizations.
Details View: Show detailed information for selected transactions.
API Integration (Optional for Bonus Marks)
Develop a simple backend API using Python (Flask/FastAPI) or NodeJS to fetch data from the database for the frontend.

Getting Started

Prerequisites

Ensure you have the following installed:

Python (if using a Python backend)
Node.js (if using a JavaScript backend)
Database System (SQLite/MySQL/PostgreSQL)
Frontend Tools (HTML, CSS, JavaScript, Chart.js for visualizations)
Setup Instructions

1. Clone the repository:
    git clone 
    cd fullstack-sms-apppip install -r requirements.txt  # For Python backend
npm install  # For Node.js backend
2. Install dependencies:
    
3. Set up the database schema:
    python setup_database.py  # Python script to create tables
4. Run data processing:
    python process_sms.py  # Parses XML and inserts into DB
5. Start the backend server:
    python app.py  # Flask API
6. Start the frontend:
    open index.html  # Or use a local server

