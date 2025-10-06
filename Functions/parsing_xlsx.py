import datetime
import pandas as pd
import os
import pathlib
from Functions.WithWhoOnShift.combining import get_month_dict
from Functions.WithWhoOnShift.classes import Cell


pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)


def xslx_to_pandas():
    base = pathlib.Path(pathlib.Path(__file__).parent.parent.resolve())
    filename = "grafik.xlsx"
    try:
        file_path = os.path.join(base, filename)
    except Exception as e:
        print(e)
    else:
        return pd.read_excel(file_path, index_col=False).dropna(how="all").dropna(axis=1, how="all")

def find_employee_data(pandas_file, employee_name):

    rows = []
    for idx, row in pandas_file.iterrows():
        for col in pandas_file.columns:

            cell = pandas_file.loc[idx, col]

            if isinstance(cell, datetime.datetime) or cell == employee_name:
                rows.append(idx)
                break

    df = pandas_file.loc[rows]
    return df

def format_to_ical(hours, date):
    try:
        start_hour, end_hour = hours.split('-')
    except Exception:
        return  None

    start = datetime.datetime.combine(date, datetime.time(int(start_hour)))
    end = datetime.datetime.combine(date, datetime.time(int(end_hour)))

    return {"dtstart": start, "dtend": end}

def extract_days_data(employee_name, pandas_schedule=None, test=False):

    if pandas_schedule is None:
        pandas_schedule = xslx_to_pandas()
    else:
        pass

    employee_df = find_employee_data(pandas_schedule, employee_name)
    employee_df.reset_index(drop=True, inplace=True)

    dates_dict = {}
    for idx, row in employee_df.iterrows():
        for col in employee_df.columns:
            cell = Cell(employee_df.loc[idx , col])
            if cell.isDate():
                date = cell.toDate()
                try:
                    hours = employee_df.loc[idx + 1, col]
                except Exception:
                    continue

                start_end = format_to_ical(hours, date)
                if start_end is not None:
                    dates_dict[date] = start_end

    mattering_dates = list(dates_dict.keys())
    shift_info = get_month_dict(mattering_dates, pandas_schedule, employee_name, test)

    return dates_dict, shift_info

def merge_info(employee_dict, info_dict):
    complete_info = {}
    for date in employee_dict:
        complete_info[date] = employee_dict[date], info_dict[date]

    calendar_info = {}

    for day in complete_info:
        info_type = complete_info[day]

        crue_on_shift = info_type[1]
        my_shift = f"{employee_dict[day]["dtstart"].time().hour}-{employee_dict[day]["dtend"].time().hour}"
        crue_on_shift["Ja"] = {day: my_shift}
        info = []

        for person in crue_on_shift:
            persons_status = f"{person.split()[0]}: {crue_on_shift[person][day]}"
            info.append(persons_status)
        start, end = info_type[0]['dtstart'], info_type[0]['dtend']
        day_info = {'dtstart': start, 'dtend': end, "description": "\n".join(info)}
        calendar_info[day] = day_info

    return calendar_info
