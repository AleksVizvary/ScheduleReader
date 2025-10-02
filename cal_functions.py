import pars_functions
from pars_functions import extract_days_data
from icalendar import Calendar, Event, vCalAddress, vText
from pathlib import Path
import os

def add_event(start, end, event_name):
    event = Event()
    event.add('summary', event_name)
    event.add('dtstart', start)
    event.add('dtend', end)

    organizer = vCalAddress('MAILTO:ckj.krakow.krakowska@ck.com')
    event.add('organizer', organizer)

    event['location'] = vText('Cracow, Poland, Pawia 5, 31-154')

    return event

def add_days_to_cal(dates_dict, event_name):
    cal = Calendar()

    cal.add('prodid', '-//My calendar product//example.com//')
    cal.add('version', '2.0')

    for date in dates_dict:
        day_data = dates_dict[date]
        start = day_data["dtstart"]
        end = day_data["dtend"]
        event = add_event(start, end, event_name)
        cal.add_component(event)

    return cal

def main_func(employee_name, event_name):

    dates_dict = extract_days_data(employee_name)
    if not dates_dict:
        return False

    cal = add_days_to_cal(dates_dict, event_name)

    directory = Path.cwd() / 'MyCalendar'
    try:
        directory.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        print("Folder already exists")
    else:
        print("Folder was created")

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
            if employee_name not in pars_functions.xslx_to_pandas().values:
                employee_name = input("Wpisz się kurwa poprawnie: ")

        except FileNotFoundError:
            print("Nie dałeś grafiku, jełopie")
            print("Dodaj i zacznij od nowa")
            quit()

        else:
            start = True

    else:
        main_func(employee_name, event_name)

    return True