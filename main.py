from cal_functions import main_func

event_name = "Praca"
employee_name = input("Wpisz się (tak jak w grafiku): ")
# employee_name = "Aleksander Vizvary"
file_name = "TuGrafik/test_sch.xlsx"
main = main_func(employee_name, file_name, event_name)
if not main:
    while not main:
        main = main_func(employee_name, file_name, event_name)