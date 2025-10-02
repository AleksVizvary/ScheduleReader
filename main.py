import pars_functions
from cal_functions import main_func

event_name = "Praca"
employee_name = input("Wpisz się (tak jak w grafiku): ")

start = False
while not start:
    if employee_name not in pars_functions.xslx_to_pandas().values:
        employee_name = input("Wpisz się kurwa poprawnie: ")
    else:
        start = True

else:
    main_func(employee_name, event_name)

main = main_func(employee_name, event_name)
