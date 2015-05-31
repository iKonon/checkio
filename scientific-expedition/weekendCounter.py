'''
Sofia has given you a schedule and two dates and told you she needs help planning her weekends. 
She has asked you to count each day of rest (Saturday and Sunday) starting from the initial date to final date. 
You should count the initial and final dates if they fall on a Saturday or Sunday.

The dates are given as datetime.date. The result is an integer.

Input: Start and end date as datetime.date.
Output: The quantity of the rest days as an integer.

How it is used: Now is a good time to learn how to work with dates. 
These ideas here often come up in calendar apps, customer relation management software, 
automated messaging schedulers among many other things.
Precondition: start_date < end_date.
'''
from datetime import date, timedelta

def checkio(from_date, to_date):
    # count the days of rest 
    daygenerator = (from_date + timedelta(x) for x in range((to_date - from_date).days + 1))
    return sum(1 for day in daygenerator if day.weekday() in (5,6))

def checkioFromVeky(d1, d2):
    w1, w2 = d1.weekday(), d2.weekday()
    count = (d2 - d1).days // 7 * 2
    while True:
        count += w2 > 4
        if w1 == w2: return count
        w2 = (w2 - 1) % 7

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"