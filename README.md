Vocab Randomizer Flask Application
This is a simple Flask application that allows users to randomize vocabulary terms from a CSV file. The app uses SQLite as the backend database, and users can upload a CSV file containing vocabulary data (English and Thai words), view random vocabulary terms, and edit them.

Features
Random Vocabulary Generator: Displays a random English vocabulary term along with its Thai translation.
Vocabulary List: Shows all vocabulary terms in alphabetical order.
CSV Upload: Allows users to upload a CSV file that replaces the current vocabulary database.
Edit Vocabulary: Edit existing vocabulary entries.
Technologies Used
Flask: A lightweight Python web framework.
SQLAlchemy: A SQL toolkit for Python, used to interact with the SQLite database.
SQLite: A lightweight database used to store vocabulary data.
Pandas: Used to handle the CSV file and insert its contents into the SQLite database.
Installation
1. Clone the Repository
Clone this repository to your local machine using the following command:

bash
คัดลอกโค้ด
git clone https://github.com/yourusername/vocab-randomizer.git
cd vocab-randomizer
2. Install Dependencies
Ensure you have Python 3.x installed. Install the necessary Python packages by running:

bash
คัดลอกโค้ด
pip install -r requirements.txt
The requirements.txt file should contain:

txt
คัดลอกโค้ด
Flask
Flask-SQLAlchemy
pandas
If you don't have a requirements.txt file, you can generate one with:

bash
คัดลอกโค้ด
pip freeze > requirements.txt
3. Prepare the Database
Before running the application, make sure to prepare the SQLite database by running the following:

bash
คัดลอกโค้ด
python app.py
This will create the necessary tables in the SQLite database.

Usage
Run the Application
To run the application in debug mode, use the following command:

bash
คัดลอกโค้ด
python app.py
By default, Flask will run the app on http://127.0.0.1:5000/. Open this URL in your browser to start using the application.

CSV File Upload
The application allows users to upload a CSV file containing vocabulary data:

The CSV file should have two columns: English and Thai.
When you upload a new CSV file, the vocabulary database will be replaced with the new content.
Routes
/: Displays a random vocabulary term and its translation.
/list/: Displays a list of all vocabulary terms in alphabetical order. You can also upload a new CSV file here.
/edit/<int:index>: Allows you to edit an existing vocabulary entry.
Editing Vocabulary
You can edit vocabulary terms by accessing the /edit/<index> route, where <index> is the ID of the vocabulary entry. After editing, the changes will be saved to the database.

Code Explanation
CSV File Handling: The csvreplacedb() function loads a CSV file into a pandas DataFrame and writes it to the SQLite database, replacing any existing data in the vocab table.

Database Model: The vocab model defines the structure of the vocabulary table, with columns for index, English, and Thai. It uses SQLAlchemy's ORM to interact with the database.

Flask Routes:

The root route (/) fetches a random vocabulary term from the database and renders it on the homepage.
The /list/ route lists all vocabulary terms in alphabetical order and allows users to upload a new CSV file to replace the existing vocabulary data.
The /edit/<int:index> route allows users to edit a specific vocabulary entry.
Directory Structure
graphql
คัดลอกโค้ด
vocab-randomizer/
│
├── app.py             # Main Flask application
├── Dict.csv           # Sample vocabulary CSV file
├── database.db        # SQLite database file
├── requirements.txt   # Python dependencies
└── templates/         # HTML templates
    ├── index.html
    ├── list.html
    └── edit.html
Contributing
Feel free to fork this repository and submit pull requests if you'd like to contribute improvements or fixes. If you encounter any issues, please open an issue ticket.
