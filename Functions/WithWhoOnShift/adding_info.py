from Functions.WithWhoOnShift.adding_info_functions import find_date_range, find_existing_days
import re


class Cell:
    def __init__(self, content):
        self.content = content

    def isTime(self):
        time_form = re.compile(r'^\d{2}-\d{2}$')
        return isinstance(self.content, str) and bool(time_form.match(self.content))

    def isTrash(self):
        trash = {'u', 'Name', 'Total Hours', 'shift', 'Max', 'zl', 'Total Paid', 'Shift', 'Hrs', 'Total Month ', 'overtime'}
        return self.content in trash

    def isName(self, name):
        return self.content == name

    def __repr__(self):
        return str(self.content)

def get_persons_dict(row_idx, date_range, date):
    dates_dict = {}

    match = date_range.isin([date]).any(axis=0)
    column = date_range.columns[match]
    i = row_idx[0]
    j = column[0]

    hours = date_range.loc[i, j]
    time_form = re.compile(r'^\d{2}-\d{2}$')
    if isinstance(hours, str):
        if time_form.match(hours):
            dates_dict[date] = hours
        else:
            dates_dict[date] = "Wolne"
    else:
        dates_dict[date] = "Wolne"

    return dates_dict

def get_day_dict(names, date_range, date):
    peoples_dicts = {}
    for n in names:
        match = date_range.astype(str).isin([n]).any(axis=1)
        row = date_range.index[match]

        persons_dict = get_persons_dict(row, date_range, date)
        peoples_dicts[n] = persons_dict

    return peoples_dicts




def get_names(schedule, name):
    potential_names = []
    for i in schedule.index:
        for c in schedule.columns:
            cell = schedule.loc[i, c]
            if isinstance(cell, str):
                cell = Cell(cell)
                if not cell.isTime() and not cell.isTrash():
                    if not cell.isName(name):
                        potential_names.append(schedule.loc[i, c])
    return potential_names


def iter_(schedule, name):
    dates = find_existing_days(schedule)
    date = min(dates)
    date_range = find_date_range(date, schedule)
    days_in_range = find_existing_days(date_range)

    names = get_names(date_range, name)
    print("=====================")
    for d in dates:
        if d not in days_in_range:
            date_range = find_date_range(d, schedule)
            days_in_range = find_existing_days(date_range)

        peoples_dict = get_day_dict(names, date_range, d)

        ###
        print(f"{d.day}/{d.month}")
        print("=====================")
        for key in peoples_dict:
            print(key)
            print(peoples_dict[key][d])
            print("--------")
        print("=====================")
        ###
