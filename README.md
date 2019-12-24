# 52957---Data-Representation
Repository containing my solutions to lab exercises and my project for module 52957.


Name:                Aidan O'Connor
GMIT student number: G00364756
Created:             30/09/2019
Due date:            TBC

## Contents
1. week01-xml
2. week02-javascript
3. week03-webScraping
4. week04-json_ajax_rest
5. week05-ajax_rest
6. week08-Project
7. .gitignore
8. LICENSE
9. README.md

### week01-xml: 
Lab 1 - Create HTML page and xml file
File names:-
* carviewer.html
* library.xml

### week02-javascript
Lab 2 - Use of javascript to add functionality to the webpage made in the lab in week 1.

### week03-webScraping
Lab 3 - Webscraping labs completed.

### week04-json_ajax_rest
Lab 4 - JSON and AJAX (with jQuery)completed.

### week05-ajax_rest
Labs 5.1, 5.2 and 5.3 completed.

### week06-ajax_rest
not finished

### week08-Project
Shop website created. RESTful API implimented, however the AJAX query to the shopDAO results in the connection to the server being dropped for the "Update" buttons. I cannot currently figure out why this is the case.

1. To run the project you must first create the database on your mySQL. 
To do this run the createDatabase.py python file.
2. Next is to insert a table into the database that has been created, to do this run the createTable.py python file.
3. Then it is necessary to insert data into the table, to do this run the insertIntoShop.py python file.

4. Once these 3 python files ahve been ran, a database with a table called shop with 3 rows of data should have been created on your mySQL.

5. Next thing to do is to create a virtual environment that has the python packages in requirements.txt installed.

6. Set the FLASK_APP to server1.py

7. Run the flask server.

8. Open shopviewer on the local host.

9. The project is then available to view and play arounf with.

Hope this step by step guide makes sense.