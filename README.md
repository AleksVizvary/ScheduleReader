# ScheduleReader

I made this because manually copying my work schedule from Excel into a calendar was annoying.

The program reads an `.xlsx` work schedule, finds shifts for a selected person and generates an `.ics` calendar file ready to import.

## what it does

- reads Excel schedules with pandas
- finds shifts for selected employees
- creates calendar events with `icalendar`
- exports a ready `.ics` file
- works with the same schedule format I use at work

## setup

```bash
git clone https://github.com/AleksVizvary/ScheduleReader.git
cd ScheduleReader
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

The repository contains placeholder employee data. To use it with a real schedule, add your own names and `.xlsx` file locally.

## status

this is a real utility I made for myself and people I work with. I’m also working on a SwiftUI version of it in `ScheduleReader-App`.
