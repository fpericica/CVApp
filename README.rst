CVApp
=====

CVApp is a Flask application that provides a RESTful API to access candidate information.

Routes
------

The following routes are available in the CVApp:

- Home:
  - URL: /
  - Method: GET
  - Description: Retrieves the home page of the application.

- Get All Candidates:
  - URL: /candidates
  - Method: GET
  - Description: Retrieves a list of all candidates.

- Get Candidate by UUID:
  - URL: /candidates/<string:uuid>
  - Method: GET
  - Description: Retrieves a candidate based on the specified UUID.

- Get Candidate Section:
  - URL: /candidates/<string:uuid>/<string:section>
  - Method: GET
  - Description: Retrieves a specific section of a candidate's information.

Accessing Data
--------------

- Clone the repository to your local machine.
- Ensure you have Python and Flask installed, according to the requirements file.
- Open your terminal or command prompt;
- Navigate to the root directory of your Flask application;
- Set the FLASK_APP environment variable to "server.py" by running the following command in the terminal (Windows Powershell):
     ```
     $env:FLASK_APP = "server.py"
     ```


The data in the CVApp can be accessed through the following ways:

1. JSON REST API:
   - Start the Flask app by running the following command:
     ```
     flask run
     ```
   - The app will start running on the local development server. You can now access the API endpoints using an API testing tool like Postman.
   - Test the following API endpoints with different scenarios and cases:
     - GET /
     - GET /candidates
     - GET /candidates/<uuid>
     - GET /candidates/<uuid>/<section>
   - Replace <uuid> with the actual UUID of a candidate and <section> with the desired section of candidate information (e.g., personal, experience, education).
   - Observe the JSON responses returned by the API, which provide candidate information in the requested format.

2. Flask CLI Command:
   - In the terminal, you can run the following Flask CLI command to print the data to the console:
     ```
     flask print-data
     ```
   - This command will execute the code to fetch and print the data from the CandidatesModel class (the entire list with the candidates).
   - You should see the data displayed in the console output, providing an overview of the candidates' information.
   - This command is useful for quickly viewing the data without making API requests.
