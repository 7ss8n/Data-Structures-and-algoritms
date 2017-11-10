class click_counter:
    #constructor of the click counter
    def __init__(self):
        self._count_display=0
        print ("The actual value is %03s"%(self._count_display))
    #Reset the actual value of the counter
    def reset(self):
        self._count_display=0
        print ("The actual value is %03s"%(self._count_display))
    #Increase in 1 the actual value
    def increase_counter(self):
        self._count_display=self._count_display+1
        print ("The actual value is %03s"%(self._count_display))
    #return the actual value of display
    def display(self):
        print ("The actual value is %03s"%(self._count_display))
new_clock=click_counter()
new_clock.increase_counter()
new_clock.increase_counter()
new_clock.increase_counter()
new_clock.increase_counter()
new_clock.reset()
new_clock.display()
new_clock.increase_counter()
new_clock.increase_counter()
new_clock.display()
