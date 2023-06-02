'''
Тимур считает дату «интересной», если её год совпадает с годом его рождения, а сумма номера месяца и номера дня равна его возрасту. Год рождения Тимура —
1992
1992, возраст —
29
29 лет.

Реализуйте функцию print_good_dates(), которая принимает один аргумент:

dates — список дат (тип date)
Функция должна выводить «интересные» даты в порядке возрастания, каждую на отдельной строке, в формате  month_name DD, YYYY, где month_name — полное название месяца на английском.

Примечание 1. Если в функцию передается пустой список или список без интересных дат, функция ничего не должна выводить.
'''

from datetime import date
def print_good_dates(dates):

    good_dates = list()
    for date in dates:
        if int(date.year) == 1992 and int(date.day) + int(date.month) == 29:
            good_dates.append(date)

    for d in sorted(good_dates):
        print(d.strftime('%B %d, %Y'))