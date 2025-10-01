import datetime
import pathlib
import pandas as pd

pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)


def xslx_to_pandas(file_name):
    try:
        file_path = pathlib.Path(__file__).parent.resolve()/file_name
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
    df.index = range(df.index.size)
    if employee_name not in df.values:
        print("Wprowadziłeś złą nazwę pracownika... ")
        print("Popraw to.")
        return False

    return df

def format_to_ical(hours, date):
    try:
        start_hour, end_hour = hours.split('-')
    except Exception:
        return  None

    start = datetime.datetime.combine(date, datetime.time(int(start_hour)))
    end = datetime.datetime.combine(date, datetime.time(int(end_hour)))

    return {"dtstart": start, "dtend": end}

def extract_days_data(employee_name, file_name):

    pandas_schedule = xslx_to_pandas(file_name)
    employee_df = find_employee_data(pandas_schedule, employee_name)
    if not employee_df:
        return False

    dates_dict = {}
    for idx, row in employee_df.iterrows():
        for col in employee_df.columns:
            cell = employee_df.loc[idx , col]
            if isinstance(cell, (datetime.datetime, datetime.date)):
                date = cell.date()
                try:
                    hours = employee_df.loc[idx + 1, col]
                except Exception:
                    continue

                start_end = format_to_ical(hours, date)
                if start_end is not None:
                    dates_dict[date] = start_end

    return dates_dict
