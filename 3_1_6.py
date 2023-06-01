'''
Реализуйте функцию get_date_range(), которая принимает два аргумента в следующем порядке:

start — начальная дата, тип date
end — конечная дата, тип date
Функция get_date_range() должна возвращать список, состоящий из дат (тип date) от start до end включительно. Если start > end, функция должна вернуть пустой список.
'''

from datetime import date

def get_date_range(start, end):

    return list(map(lambda x: date.fromordinal(x), range(start.toordinal(), end.toordinal() + 1)))