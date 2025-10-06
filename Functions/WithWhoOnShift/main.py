from Functions.parsing_xlsx import xslx_to_pandas
from Functions.WithWhoOnShift.combining import (get_month_dict)

schedule = xslx_to_pandas()
name = "Aleksander Vizvary"

get_month_dict(schedule, name)

