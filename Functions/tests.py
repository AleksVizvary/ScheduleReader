from traceback import print_tb

from parsing_xlsx import extract_days_data, xslx_to_pandas
from parsing_xlsx import merge_info
from final_combining import save_file

schedule = xslx_to_pandas()
name = "Marcin Chełpa"
# extract_days_data("Aleksander Vizvary", test=True)

employee_dict, info_dict = extract_days_data(name)
if not employee_dict:
    print("No employee data")

print(merge_info(employee_dict, info_dict))
