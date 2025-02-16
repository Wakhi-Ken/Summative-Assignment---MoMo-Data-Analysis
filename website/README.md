HOW TO RUN MoMo Account Analysis

1. Ensure that Flask is installed
  [pip install Flask]
2. Run main.py
3. Open this link in your browser: (http://127.0.0.1:5000/)


The API was made using Flask because:
- Easier to call functions from backend 
- Provides a seamless integration between the backend and frontend

How It Works
- Transactions are called from databases using the backend
- When needed, this info is pulled by Javascript code and formats it to be displayed concisely.

Problems Encountered while coding/creating the backend API and HTML/CSS
- Linking api to the javascripts in order to execute the defined functions within main.py
- Sorting the webpage files according to the Flask's requirements
- Correctly calling table names from databases, and keeping a consistent naming standard
- Creating a consistent UX to make webpage appealing
- Creating sorting function for the transaction lists