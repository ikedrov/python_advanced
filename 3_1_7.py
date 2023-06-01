'''
Реализуйте функцию saturdays_between_two_dates(), которая принимает два аргумента в следующем порядке:

start — начальная дата, тип date
end — конечная дата, тип date
Функция должна возвращать количество суббот между датами start и end включительно.
'''

from datetime import date

def saturdays_between_two_dates(start, end):

    count = 0
    start, end = min(start, end), max(start, end)
    dates = list(map(lambda x: date.fromordinal(x), range(start.toordinal(), end.toordinal() + 1)))
    for i in dates:
        if i.weekday() == 5:
            count += 1

    return count

date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)

print(saturdays_between_two_dates(date1, date2))