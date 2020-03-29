# SP-API
Requirements: 
    Docker and Docker Compose for the database utility
    Python3.6
    CMake if you want to run and test it easier
        sudo apt install cmake
    Create a new python environment and install the requirements.txt from sp_py package
    To do the above and use SQLAlchemy from python you might need this:
        sudo apt install libpq-dev python3-dev
    If the above is not enough to install the requirements.txt:
        sudo apt install build-essential

The way to use this:
    If you have CMake:
       1. make build  --- to create the database container with docker
       2. make test  --- to run the automated unit tests with python
       3. bash run_process.sh  --- to actually get the data and upload it in the database (to be run after make build)
    If you do not have CMake:
       1. docker-compose up -d 
       2. pytest --ignore=sp_db_data_volume
       3. bash run_process.sh
      
    Regardless of whether you have CMake:
       4. docker exec -it sp_db_c1 sh  --- to get inside the containe
       5. psql sp postgres   --- to connect to the database called sp with the username called postgres
       6. select * from sp_schema.company;
       7. select * from sp_schema.registered_address;
       8. select * from sp_schema.source;



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
