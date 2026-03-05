from datetime import datetime
def calculate(dob_string):
    birth_date = datetime.strptime(dob_string,"%Y/%m/%d")
    today = datetime.today()
    years  = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day
    if days < 0:
        months -=1
        days += (birth_date.replace(year=today.year,month=today.month)-birth_date.replace(year=today.year,month=today.month-1)).days
    if months < 0:
        years -=1
        months +=12
    return years,months,days