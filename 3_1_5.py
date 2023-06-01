'''

'''

from datetime import date

def get_min_max(dates):
    
    if dates:
        return min(dates), max(dates)
    else:
        return '()'