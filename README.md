# Zendesk Ticket Viewer

Created by: Tom Keenan

Submission for: **2022 Zendesk Internship Coding Challenge**



## Dependencies
Python 3.8.0

requirements.txt

## Run project
Download or clone this repository then run below command from project folder. Make sure user_info.json file is included in project folder with your Zendesk authentication credientials.

    python3 src/main.py

## Run tests
Run the below command from project folder.

    python3 ZccTests.py

 
## Project Structure

My goal when designing this project was to focus on simplicity. The user interface is minimal and clean. The project has minimal dependencies.

**TicketHandler** :

 - Handles all api calls for the project
 - Reads from json file to authenticate requests
 - Retreives pages of tickets which can be scrolled through
 - Retreives single tickets using their unique **ticket_id**

**UI**:

 - Runs command line user interface for the project
 - Instructs user how to navigate the ticket viewer
 - Displays ticket information received from TicketHandler
 - Catches and displays appropriate error messages from user or TicketHandler
 
 **main**:
 
 - Runs the project

**ZccTests**:

 - Runs tests on all methods in TicketHandler
 - UI class has been tested manually

