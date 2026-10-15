# FarosGlossary

> **FarosGlossary** is a web application designed to enhance your reading experience when reading English novels. It allows you to quickly search, view, and manage vocabulary terms, providing both **English definitions** and **Indonesian translations** so you can look up unfamiliar words without breaking your reading flow.

---

## Features

- **Quick Vocabulary Lookup**: Search English terms to instantly view detailed English definitions alongside Indonesian translations.
- **Novel Reading Companion**: Designed specifically to help readers understand context and complex terminology seamlessly while reading literature.
- **Offline-Capable Database**: Powered by a local SQLite database for instant query response times without relying on live API calls during reading sessions.
- **Automated Data Pipeline**: Python utility scripts streamline database schema initialization, definition fetching, and bulk dataset population.
- **Minimal & Distraction-Free UI**: Clean, responsive user interface built using vanilla HTML, CSS, and JavaScript.

---

## 🛠️ Tech Stack & Dependencies

- **Backend / API**: Node.js & npm (HTTP API server)
- **Database & Data Processing**: Python 3.x, SQLite3
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Data Source**: CSV dataset containing English terms, definitions, and Indonesian translations

---

## 📁 Repository Structure

```text
FarosGlossary/
├── data/
│   └── sampel.csv          # Dataset containing terms, English definitions & Indonesian translations
├── scripts/
│   ├── build_db.py         # Initializes and constructs SQLite database schema
│   ├── get_definitions.py  # Utility script for fetching/processing definitions
│   └── populate_db.py     # Seeds the database with dataset records
├── src/
│   ├── backend/
│   │   └── server.js       # Node.js backend server handling API requests
│   └── frontend/
│       ├── index.html      # Application layout
│       ├── script.js       # Search interaction & backend API fetch logic
│       └── style.css       # Clean, distraction-free styling
├── .gitignore              # Git ignore rules for node_modules, DB files, and cache
├── package.json            # Node.js dependencies and script shortcuts
└── README.md               # Documentation file
```

---

## Getting Started

Follow the steps below to set up and run FarosGlossary on your local machine.

### Prerequisites

Make sure you have the following installed on your system:
- **Node.js** (v14 or higher)
- **Python** (3.8 or higher)

---

### Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/FarosGlossary.git
   cd FarosGlossary
   ```

2. **Install Node.js Dependencies**
   ```bash
   npm install
   ```

3. **Build and Populate the Database**
   Run the Python scripts in sequence to initialize the database structure and load the vocabulary data:

   ```bash
   # Initialize SQLite database schema
   python scripts/build_db.py

   # (Optional) Fetch additional definitions or translations
   python scripts/get_definitions.py

   # Populate database with term data
   python scripts/populate_db.py
   ```

4. **Start the Backend Server**
   ```bash
   npm start
   # or
   node src/backend/server.js
   ```

5. **Access the Application**
   Open your browser and navigate to `http://localhost:3000` (or the port specified in `server.js`).
