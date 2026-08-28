from parsing_xlsx import *
from setting_calendar import *
from saving_file import *
from pathlib import Path
# from open_file import *

event_name = "Praca"
adress = "Kraków, Polska"

ROOT = Path(__file__).resolve().parent.parent

def main(i, path=None):
    with open(ROOT / "EmployeeNamesList.txt", "r") as file:
        employee_list = [p.split(';') for p in file][0]
    boss_name = employee_list[7]
    client = employee_list[i]

    miesiac = 'czerwiec'
    file_name = f"grafik_{miesiac}.xlsx"
    file_path = "DataHolder/" + file_name
    if not path:
        path = ROOT / file_path

    if not Path(path).exists():
        print(f"Brak pliku grafiku: {path}")
        return False

    schedule_xslx = pd.read_excel(path)
    schedule_list = parse_pandas_to_dict(schedule_xslx, employee_list)

    cal = add_days_to_cal(schedule_list, boss_name, client, adress, event_name)
    save_file(cal, client, miesiac)
    return True

if __name__ == "__main__":
    for i in range(7):
        if not main(i):
            break
