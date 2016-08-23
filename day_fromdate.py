import datetime
from datetime import date
import calendar

weekday = {1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday', \
               5:'Friday',6:'Saturday',7:'Sunday'}




def dateFinder(year_inp, month_inp, date_inp):
    try:
        op = date.isoweekday(datetime.date(year_inp, month_inp, date_inp))
    except Exception as e:
        print('Sorry invalid inputs..?! \n kindly try again...',e)
    else:
        #print(op)
        return op
        #print(date_inp,'-',month_inp,'-',year_inp,'..week day is ..',weekday[op])


def first_lastday(year_inp, month_inp):
    first_day ,number_days = calendar.monthrange(year_inp, month_inp)
    print(first_day)
    print(date_inp,'-',month_inp,'-',year_inp,'..week day is ..', \
          weekday[dateFinder(year_inp, month_inp, date_inp)])
    print('First day of the month is ...',weekday[first_day+1])
    print('Last day of the month is ...',weekday[dateFinder(year_inp, month_inp,number_days)])
    print('Number of days in the month...',number_days)


def main():
    first_lastday(year_inp, month_inp)


date_inp= int(input('Enter the date..'))
month_inp = int(input('Enter the month..'))
year_inp = int(input('Enter the year..'))
    
main()
    

