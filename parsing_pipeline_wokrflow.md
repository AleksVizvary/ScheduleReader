## PIPELINES WORKFLOW:

### 1. Opening and reading .xlsx file:

-   **coverting to pandas**

### 2. Parsing pandas file:

-   **cleaning empty rows and columns**
-   **selecting rows with:**
    -   employee hours
    -   dates

### 3. Parsing new pandas file:

-   **selecting cells containg dates**
-   **selecting cells containg working hours**

### 4. Parsing cells containg dates and working hours:

dates: `datetime.datetime(date_cell).date()`

hours: `datetime.strptime(hour_cell, '%H:%M').time()`

start_time = combine(date, hour)

### 5. Combining date with time and adding to a dict:

-   returning a dict containg date as a key, datetime.datetime as a valaue

`dict = {datetime.datetime(date_cell):`  
`{'dtstart': datetime.datetime(start_time),`  
`'dtend': datetime.datetime(end_time)}}`