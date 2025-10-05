from icalendar import Calendar, Event, vCalAddress, vText

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
