

from icalendar import Calendar, Event, vCalAddress, vText
import re, datetime

def add_event(start, end, event_name, description, adress):

    event = Event()
    if if_G(description, start, end):
        description = "ZMIANA Z G\n" +"\n" + description

    event.add('summary', event_name)
    event.add('dtstart', start)
    event.add('dtend', end)

    event.add('description', description)

    event['location'] = vText(adress)

    return event

def add_days_to_cal(dates_dict, event_name, adress):
    cal = Calendar()

    cal.add('prodid', '-//My calendar product//example.com//')
    cal.add('version', '2.0')


    for date in dates_dict:
        day_data = dates_dict[date]
        start = day_data["dtstart"]
        end = day_data["dtend"]
        description = day_data["description"]
        event = add_event(start, end, event_name, description, adress)
        cal.add_component(event)

    return cal

def if_G(description, my_start, my_end):
    date = my_start.date()
    if description.find("Małgorzata"):
        pa = re.compile(r'Ma[ł]g?orzata\s*:\s*(\d{2}\s*-\s*\d{2})')
        try:
            match = pa.search(description)
            time = match.group(1)

        except AttributeError:
            time = None

        if time:
            g_start = datetime.time(int(time.split("-")[0]))
            g_end = datetime.time(int(time.split("-")[1]))

            g_start = datetime.datetime.combine(date, g_start)
            g_end = datetime.datetime.combine(date, g_end)

            if g_start == my_start or g_end == my_end:

                return True

    return False
