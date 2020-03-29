Folder structure

The docker-compose.yml to start the database container. It has 2 volumes attached to it, the sp_db_init_volume and sp_db_data_volume. The first contains the initialization scripts and the schema and the second is the actual data folder.

The sp_file_db folder is the "file" database, containing the CSV required in the exercise. - The sp_py is the python package.

The sp_py/tests subfolder contains the tests and sp_py/sp_py contains a database toolbox, an api handler module, a file called pull that gets data from the api and then to the CSV and, finally, a file called push that pushes the csv file to the database.

The makefile which runs the container and the tests.

The run_process.sh which runs the python code.
##############################
Requirements
Docker and Docker Compose for the database utility

CMake if you want to run and test it easier
sudo apt install cmake

Create a new python environment and install the requirements.txt from sp_py package
To do the above and use SQLAlchemy from python you might need this:
sudo apt install libpq-dev python3-dev
If the above is not enough to install the requirements.txt:
sudo apt install build-essential
###############################
How to run the application
If you have CMake:

1. make build --- to create the database container with docker
2. make test --- to run the automated unit tests with python
3. bash run_process.sh --- to actually get the data and upload it in the database (to be run after make build)

If you do not have CMake:

1. docker-compose up -d
2. pytest --ignore=sp_db_data_volume
3. bash run_process.sh

Regardless of whether you have CMake:

4. docker exec -it sp_db_c1 sh --- to get inside the container
5. psql sp postgres --- to connect to the database called sp with the username called postgres
6. run select statements on the tables: sp_schema.company; sp_schema.registered_address; sp_schema.source

#####################################################################################
Query an api (http://api.opencorporates.com/documentation/API-Reference). You will need to:
• Query the api for a list of companies that have the word “smart” in their name
• Retrieve details about each of these companies including (but not limited to):
◦ Company ID
◦ Jurisdiction
◦ Incorporation date
◦ Dissolution date
◦ Company Type
◦ Registered Address
◦ Ultimate beneficiary owners
• Output the collected data to a CSV file
• Upload the CSV file to a database (any local database will be sufficient, e.g. SQLLite, MySQL, etc.)
Additional considerations
Please include consideration for the following:
• Automated unit tests
• Error handling if the API returns error codes
• Handling of API rate limiting
• How to handle API keys/secrets if the API were to require such things
• Consideration for how the code would perform with much higher volumes of data (e.g. 100,000 company records)
