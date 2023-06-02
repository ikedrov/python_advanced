'''
Во время визита очередного гостя сотрудникам отеля приходится проверять, доступна ли та или иная дата для бронирования номера.

Реализуйте функцию is_available_date(), которая принимает два аргумента в следующем порядке:

booked_dates — список строковых дат, недоступных для бронирования. Элементом списка является либо одиночная дата, либо период (две даты через дефис). Например:
['04.11.2021', '05.11.2021-09.11.2021']
date_for_booking — одиночная строковая дата или период (две даты через дефис), на которую гость желает забронировать номер. Например:
'01.11.2021' или '01.11.2021-04.11.2021'
Функция is_available_date() должна возвращать True, если дата или период date_for_booking полностью доступна для бронирования. В противном случае функция должна возвращать False.
'''

from datetime import datetime
import pandas as pd


def is_available_date(dates, booking):
    booked_dates = set()
    for date in dates:
        date_range = date.split("-")
        start_date = datetime.strptime(date_range[0], "%d.%m.%Y")
        end_date = start_date if len(date_range) == 1 else datetime.strptime(date_range[1], "%d.%m.%Y")
        booked_dates.update(
            pd.date_range(min(start_date, end_date), max(start_date, end_date)).strftime("%d.%m.%Y").to_list())

    booking_list = booking.split("-")
    start_date = datetime.strptime(booking_list[0], "%d.%m.%Y")
    end_date = start_date if len(booking_list) == 1 else datetime.strptime(booking_list[1], "%d.%m.%Y")
    check_in_dates = set(
        pd.date_range(min(start_date, end_date), max(start_date, end_date)).strftime("%d.%m.%Y").to_list())

    if booked_dates.intersection(check_in_dates):
        return False
    else:
        return True