Aim - To create an automation that scraps LinkedIn profiles of a given list of companies.

Requirements - 

A google service account. By default the service credentials used are in the "creds.json" file owned by "https://github.com/shiv4m-k". 
Although, any other Google service account may also be used, given that the "creds.json" file of that account is provided and that the google
sheet has given access to that service account.

Input to the script - 

The script takes input from a google sheet named "Scrap Companies LinkedIn URL" with the Tab name - "Missing LinkedIn Automation", propreitery under Default.
Although, input sheet can be changed by changing the name of the sheet in the "constants.py" file. The Sheet name and tab name provided in this sheet are then
used by the script to generate output.

The script finds all the names of the companies in this sheet and performs a google search to find their LinkedIn profile.

How to run - The script works like any other python script. Use the command below to run the script in your bash/command prompt.

Command - python main.py

Output - 

1) The script writes the LinkedIn profile's web link to the Sheet provided in the sheet named "Scrap Companies LinkedIn URL" with the Tab name - "Missing LinkedIn Automation".
2) The script also prints the links it finds, in the bash/command prompt.
