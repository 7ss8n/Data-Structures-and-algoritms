#Implements a proleptic Gregorian calendar date as a julian date number.

class Date:
    #creates an object instance for the specified Gregorian date.
    def __init__(self,month,day,year):
        self._julianDay=0
        assert self._isValidGregorian(month,day,year),"Invalid Gregorian date."
        #The first line of the equation, T =(M-14)/12, has to be changed
        #since Python's implementation of inteer division is not the same
        #as the mathematical definition.
        tmp=0
        if month<3:
            tmp=-1
        self._julianDay=day=32075+\
	        (1461 * (year + 4800 + tmp) // 4) + \
		    (367 * (month- 2- tmp * 12) // 12)- \
		    (3 * ((year + 4900 + tmp) // 100) // 4)
	#extracts the appropiate Gregorian date component.
    def month(self):
        return(self._toGregorian())[0]# returnuin M from (M,d,y)
    def day(self):
        return (self. _toGregorian())[1] # returning D from (m, D, y)
    def year(self):
        return (self. _toGregorian())[2] # returning Y from (m, d, Y)
	# Returns day of the week as an int between 0 (Mon) and 6 (Sun).
    def dayOfWeek(self):
        month, day, year=self._toGregorian()
        if month <3:
            month=month+12
            year=year-1
            return ((13 * month + 3) // 5 + day + \
		    year + year // 4- year // 100 + year // 400) % 7
    def _isValidGregorian(self):
        return true
        #Returns the date as a string in Gregorian format.
	#Return Month Name in a string format
    def monthName(self):
        month, day, year=self._toGregorian()
        month_eq={1:"January",2:"February",3:"March",4:"April",5:"May", \
		    6:"June",7:"July",8:"August",9:"September",10:"October",11: \
            "November",12:"december"}
        return month_eq[month]
	#Return if is a leap year
    def isLeapYear():
        month, day, year=self._toGregorian()
        if (year%4)==0:
            if(year%100)==0:
                if(year%400)==0:
                    return true
                else:
                    return false
            else:
                 return true
        else:
            return false
    def __str__(self):
        month,day,year=self._toGregorian()
        return "%02d/%02d/%04d"%(month,day,year)
	#Logically compares the two dates.
    def __eq__(self,otherDate):
        return self._julianDay==otherDate._julianDay
    def __it__(self,otherDate):
        return self._julianDay<otherDate._julianDay
    #The remainin methods are  to be included at this point.
	#....
	#Returns the Gregorian date as a tuple:(month,day,year).
    def _toGregorian(self):
       A=self._julianDay+68569
       B=4*A // 146097
       A = A- (146097 * B + 3) // 4
       year = 4000 * (A + 1) // 1461001
       A = A- (1461 * year // 4) + 31
       month = 80 * A // 2447
       day = A- (2447 * month // 80)
       A = month // 11
       month = month + 2- (12 * A)
       year = 100 * (B- 49) + year + A
       return month, day, year