"""Author: Jacky Ho

   Date: October 20, 2016
   
   Description: Determines the resultant velocity of the boat"""



#input
def main():
    '''Prompts user to enter the velocity of the boat and current'''  
    
    boat_speed = input ("Please enter the speed of the boat (km/h): ")
    
    current_speed = input ("Please enter the velocity of the current (m/s): ")
    
    boat_speed2 = float (boat_speed) * 1000/3600  #Converts km/h to m/s
    
    print  #Blank line
    
    resultant_velocity (boat_speed2, current_speed)    
    
    
#processing
def resultant_velocity (boat_speed, current_speed):
    
    '''Calculates the resultant velocity of the boat'''
     
    print "Calculating the resultant velocity..."
    
    # VR**2 = (VB **2 + VC**2)**0.5 equation for pythagorean theorem
    
    resultant_velocity = (boat_speed**2 + current_speed**2) **0.5 
    
    display_results(boat_speed, current_speed, resultant_velocity)
    
#output
def display_results (boat_speed, current_speed, resultant_velocity):
    
    """Displays results"""
    
    print "If the boat velocity is %.1f m/s" % boat_speed
    
    print "and the velocity of the current is %.1f m/s" % current_speed
    
    print "then the resultant velocity is %.1f m/s" % resultant_velocity
    
main()  #calls function