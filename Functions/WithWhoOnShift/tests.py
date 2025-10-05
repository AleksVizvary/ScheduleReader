import pandas as pd, datetime, math, re


from adding_info import iter_, get_names
from Functions.parsing_xlsx import xslx_to_pandas
from adding_info import find_existing_days


nan = math.nan
# date_range = pd.DataFrame({'Unnamed: 0': [nan, 'Name', 'Małorzata Janowska', 'Marcin Chełpa', 'Aleksander Vizvary', 'Anna Majewska', 'Paulina Gawęda', 'Malwina Walus', 'Dorota Hazik', 'Dariusz Dutkiewicz', nan, nan, nan, 'Total Paid'], 'Unnamed: 1': [nan, 'Shift', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 0], 'Unnamed: 2': [nan, 'Hrs', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan], 'Unnamed: 3': [nan, 'Shift', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 0], 'Unnamed: 4': [nan, 'Hrs', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan], 'Unnamed: 5': [datetime.datetime(2025, 10, 1, 0, 0), 'Shift', '09-17', '14-22', 'zl', '08-16', '08-16', 'u', nan, '14-22', nan, nan, nan, 56], 'Unnamed: 6': [nan, 'Hrs', 8, 8, 8, 8, 8, 8, nan, 8, nan, nan, nan, nan], 'Unnamed: 7': [datetime.datetime(2025, 10, 2, 0, 0), 'Shift', '08-16', nan, 'zl', '14-22', '08-16', 'u', '16-22', nan, nan, nan, nan, 46], 'Unnamed: 8': [nan, 'Hrs', 8, nan, 8, 8, 8, 8, 6, nan, nan, nan, nan, nan], 'Unnamed: 9': [datetime.datetime(2025, 10, 3, 0, 0), 'shift', '08-16', '14-22', 'zl', '08-16', nan, 'u', '16-22', nan, nan, nan, nan, 46], 'Unnamed: 10': [nan, 'Hrs', 8, 8, 8, 8, nan, 8, 6, nan, nan, nan, nan, nan], 'Unnamed: 11': [datetime.datetime(2025, 10, 4, 0, 0), 'Shift', nan, '08-16', 'zl', '08-16', nan, nan, '14-22', '16-22', nan, nan, nan, 38], 'Unnamed: 12': [nan, 'Hrs', nan, 8, 8, 8, nan, nan, 8, 6, nan, nan, nan, nan], 'Unnamed: 13': [datetime.datetime(2025, 10, 5, 0, 0), 'Shift', nan, nan, 'zl', nan, nan, nan, nan, nan, nan, nan, nan, 0], 'Unnamed: 14': [nan, 'Hrs', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan], 'Unnamed: 15': [nan, 'Total Hours', 24, 24, 32, 32, 16, 24, 20, 14, 0, 0, 0, 186], 'Unnamed: 16': [nan, 'Total Month ', 184, 184, 138, 184, 184, 184, 92, 92, 0, 0, 0, nan], 'Unnamed: 17': [nan, 'Max', 184, 184, 138, 184, 184, 184, 92, 92, nan, nan, nan, 1242], 'Unnamed: 18': [nan, 'overtime', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, nan, nan]})
# iter_(schedule)



## TESTING find_crue FUNCTION:
schedule = xslx_to_pandas()
name = "Aleksander Vizvary"

iter_(schedule, name)


