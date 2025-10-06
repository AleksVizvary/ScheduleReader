from Functions.setting_calendar import add_days_to_cal
from Functions.parsing_xlsx import xslx_to_pandas, extract_days_data, merge_info
import os
from icalendar import Calendar
from pathlib import Path


def save_file(employee_name, event_name, adress):

    employee_dict, info_dict = extract_days_data(employee_name)
    if not employee_dict:
        return False

    complete_info = merge_info(employee_dict, info_dict)

    cal = add_days_to_cal(complete_info, event_name, adress)

    directory = Path.cwd() / 'MyCalendar'
    try:
        directory.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        pass

    print("To gotowy plik masz w folderze MyCalendar")

    f = open(os.path.join(directory, 'my_grafik.ics'), 'wb')
    f.write(cal.to_ical())
    f.close()

    e = open('MyCalendar/my_grafik.ics', 'rb')
    ecal = Calendar.from_ical(e.read())
    e.close()

    return True

def start(event_name, adress, test=False, test_name=None):
    if test:
        employee_name = test_name
    else:
        employee_name = input("Wpisz się (tak jak w grafiku): ")

    try:
        data = xslx_to_pandas()
    except FileNotFoundError:
        print("Nie dałeś grafiku, jełopie\nDodaj i zacznij od nowa")
        quit()

    while employee_name not in data.values:
        employee_name = input("Wpisz się kurwa poprawnie: ")

    save_file(employee_name, event_name, adress)
    return True
