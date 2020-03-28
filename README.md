# SP-API
sp
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
