
from Functions.setting_calendar import add_days_to_cal
from Functions.parsing_xlsx import xslx_to_pandas, extract_days_data
import os
from icalendar import Calendar
from pathlib import Path


def main_func(employee_name, event_name):

    dates_dict = extract_days_data(employee_name)
    if not dates_dict:
        return False

    cal = add_days_to_cal(dates_dict, event_name)

    directory = Path.cwd() / 'MyCalendar'
    try:
        directory.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        pass
    finally:
        print("To gotowy plik masz w folderze MyCalendar")

    f = open(os.path.join(directory, 'my_grafik.ics'), 'wb')
    f.write(cal.to_ical())
    f.close()

    e = open('MyCalendar/my_grafik.ics', 'rb')
    ecal = Calendar.from_ical(e.read())
    e.close()

    return True

def start(employee_name, event_name):

    start = False
    while not start:
        try:
            if employee_name not in xslx_to_pandas().values:
                employee_name = input("Wpisz się kurwa poprawnie: ")

            else:
                start = True

        except FileNotFoundError:
            print("Nie dałeś grafiku, jełopie")
            print("Dodaj i zacznij od nowa")
            quit()


    else:
        main_func(employee_name, event_name)

    return True

