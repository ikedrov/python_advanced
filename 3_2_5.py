'''
Напишите программу, которая принимает на вход две даты и выводит ту, что меньше.

Формат входных данных
На вход программе подаются две корректные даты в ISO формате (YYYY-MM-DD), каждая на отдельной строке.

Формат выходных данных
Программа должна выбрать из двух введенных дат меньшую и вывести ее в формате DD-MM (YYYY).
'''

from datetime import date

date1 = date.fromisoformat(input())
date2 = date.fromisoformat(input())
min_date = min(date1, date2)
print(min_date.strftime('%d-%m (%Y)'))