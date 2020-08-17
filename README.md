# GET MAXIMUM DAILY TONS BETWEEN TWO DATES FILTERED DURING TWO TIMES  

The ```get-data-new.py``` script connects to the SQL Historian, then for each tag in a list (configured in the script), it will retrieve the day and the maximum value for that day. The data is filtered between two time slots as well (i.e. between 2 AM and 5:30 AM).  

## Context  

I got a request from an Engineer whom wanted for the last 3 months the daily total values for the production belts on his shaft.  
He wanted to compare it with the report being send out.  
This kind of request is a regular request.  
My SQL skills is not the best and it proved too time consuming to get it all with SQL.  
I used a combination of SQL, Python, Pandas and Numpy to get the data extracted with a very short script.  

## Requirements  

1. Windows based computer with access and Windows authentication to the Historian.  
2. Python 3.8 or later installed.  
3. Pandas Python package installed. ```pip install pandas```  
4. Numpy Python package installed. ```pip install numpy```  
5. Pyodbc Python package installed. ```pip install pyodbc```  
6. The script: ```get-data-new.py```  

> Please note that the above were already installed on the GR on Gold side.  

## Execution  

1. Edit script for Historian Server Name, tagnames, dates and times.  
2. run script from the command prompt from the directory on a PC which can access the Historian by means of Windows Authentication. ```>py .\get-data-new.py```  
3. The script will create a csv file for each tagname with the date and the value for the day.  

## Licensing  

Please note that all Sibanye Stillwater data is protected. Rights to data is reserved. Please familiarize yourself with company policy regarding the company data.  

Except for Sibanye Stillwater specific data, the script can be re-used in any legal way.  

end.  
