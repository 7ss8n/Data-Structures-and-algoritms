class time:
    """create time instance with hour, minutes, seconds"""
    def __init__(self,hours,minutes,seconds):
        self.hour=hours
        self.minute=minutes
        self.second=seconds


class Time_ADT:
    """ Time ADT to represent the time of day"""
    def __init__(self,hours,minutes,seconds):
        self.__hours=hours
        self.__minutes=minutes
        self.__seconds=seconds
    def hour(self):
        """returns the hours"""
        return self.__hours
    def minutes(self):
        """returns the minutes"""
        return self.__minutes
    def seconds(self):
        """returns the seconds"""
        return self.__seconds
    def numSeconds(self,*otherTime):
        """returns the number of seconds of the time, use 3 elements as input"""
        #oTime=otherTime
        assert len(otherTime)<4,"More elements than needed"
        #print(list(otherTime))
        __hour,__min,__sec=otherTime
        #print("%02d:%02d:%02d"%(__hour,__min,__sec))
        return abs(((self.__hours*3600)+(self.__minutes*60)+self.__seconds)- \
            ((__hour*3600)+(__min*60)+__sec))
    def isAM(self):
        """return if"""
        if(self.__hours<12):
            return True
        if(self.__hours>=12):
            return False
    def isPM(self):
        if(self.__hours>=12):
            return True
        else:
            return False
    def comparable(self,*otherTime):
        assert len(otherTime)<4,"more elements than needed"
        __hour,__min,__sec=otherTime
        sec_dif=self.numSeconds(__hour,__min,__sec)
        m,s=divmod(sec_dif,60)
        h,m=divmod(m,60)
        return (h,m,s)
    def __str__(self):
        if self.isAM:
            return("%02d:%02d:%02d AM"%(self.__hours,self.__minutes,self.__seconds))
        if self.isPM:
            return("%02d:%02d:%02d PM"%(self.__hours-12,self.__minutes,self.__seconds))





nuevo=Time_ADT(12,35,3)
print(nuevo.numSeconds(23,4,5))
print(nuevo.isAM())
print("%02d hours %02d minutes %02d seconds"%(nuevo.comparable(13,0,4)))
print(nuevo)
    

