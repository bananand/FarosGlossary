# FarosGlossary

FarosGlossary is a lightweight web application designed to enhance the experience of reading English novels. It allows users to quickly search, view, and manage vocabulary by providing both English definitions and Indonesian translations, helping readers understand complex terms without breaking their reading flow.
The project utilizes Python scripts for data processing and database operations, a Node.js backend server, and a lightweight web frontend interface.

Tech Stack & Dependencies

The project relies on two main runtime environments:

Python 3.10.6

Used for data ingestion, scraping/fetching definitions, and building/populating the SQLite database (*.db).

Node.js & npm

Powers the backend HTTP API server (server.js) to serve glossary data and handle requests from the frontend client.

HTML5, CSS3, & JavaScript (ES6+)

Provides the user-interface layout, styling, and interactive client-side logic.

📁 Repository Structure

FarosGlossary/
├── data/
│   └── sampel.csv          # Sample data file containing terms and definitions
├── scripts/
│   ├── build_db.py         # Script to initialize and construct database schema
│   ├── get_definitions.py  # Utility script for processing or fetching definitions
│   └── populate_db.py     # Script to populate the database from dataset files
├── src/
│   ├── backend/
│   │   └── server.js       # Node.js backend API server
│   └── frontend/
│       ├── index.html      # Main HTML structure for the web app
│       ├── script.js       # Frontend UI interaction and API fetch logic
│       └── style.css       # Application styling and layout
├── .gitignore              # Git ignore rules for node_modules, DBs, and Python cache
├── package.json            # Node.js dependencies and project scripts
└── README.md               # Project documentation


🚀 Getting Started

Follow the steps below to set up and run the application on your local machine.

Prerequisites

Ensure you have the following installed on your system:

Node.js (v14+ recommended)

Python 3.x

Installation & Setup

Clone the Repository

git clone <repository-url>
cd FarosGlossary


Install Node.js Dependencies

npm install


Build and Populate the Database
Run the Python scripts to build the database schema and load sample data:

# Initialize database
python scripts/build_db.py

# (Optional) Fetch additional definitions if needed
python scripts/get_definitions.py

# Populate the database with term data
python scripts/populate_db.py


Start the Backend Server
Start the Node.js server:

npm start
# or
node src/backend/server.js


Access the Application
Open your browser and navigate to the local server address (typically http://localhost:3000 or the port specified in server.js).

📝 Features

Term Search & Lookup: Quickly search through terms and view their corresponding definitions.

Automated Data Population: Easily seed and rebuild the database using Python utility scripts, no API injection is used so the glossary database is used offline.

Clean & Quick Frontend: Clean and accessible user interface built using vanilla HTML/CSS/JavaScript.
