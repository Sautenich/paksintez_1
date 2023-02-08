"""
paksintez_1 base module.

This is the principal module of the paksintez_1 project.
here you put your main classes and objects.

Be creative! do whatever youa want!

If you want to replace this with a Flask application run:

    $ make init

and then choose `flask` as template.
"""

# example constant variable
NAME = "paksintez_1"

from pymavlink import mavutil 
import time 
import datetime
import serial
print('Hello World') 
i = 0

def start_connection():
# Start a connection listening to a UDP port 
    global the_connection
    the_connection = mavutil.mavlink_connection('/dev/ttyACM0') 
    #the_connection = mavutil.mavlink_connection('udpin:localhost:14550') 
    time.sleep(1) 
    # Wait for the first heartbeat  
    #   This sets the system and component ID of remote system for the link jetson.agx
    the_connection.wait_heartbeat() 
    print(the_connection.recv_match(blocking=True))
    print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_system)) 
    
    # Wait for the vehicle to send GPS_RAW_INT message 
    time.sleep(1) 
    return the_connection

def get_current_time():
    global current_time
    current_time = datetime.datetime.now() #time now on Computer
    print("The real time now is " + str(current_time))
    return current_time

def get_lon_int():
    lon =  the_connection.messages['GPS_RAW_INT'].lon #longtitude
    print("Longtitude is " + str(lon)) 
    return lon

def get_lat_int():
    lat = the_connection.messages['GPS_RAW_INT'].lat #latitude
    print("Latitude is " + str(lat))
    return lat

def get_alt_int():
    alt=the_connection.messages['GPS_RAW_INT'].alt #altitude
    print("Altitude is " + str(alt)) 
    return alt

def get_time_stamp():
    time_stamp=the_connection.time_since('GPS_RAW_INT') #time since the start of the connection
    print("Time since the start is " + str(time_stamp)) 
    return time_stamp



def write_log(current_time, lon, lat, alt, time_stamp):
    timestr = time.strftime("%H%M%S-%D%M%Y")
    log = open('timestr1.txt', 'a+')
    log.write("Время: %s\nШирота: %s\nДолгота: %s\nВысота: %s\nВремя с начала старта: %s \n" %(current_time, lon, lat, alt, time_stamp))
    log.close()                        

if __name__ == '__main__':

    try:
        start_connection()
        print('Connection established')
    except:
        print('No connection established')
    
    for i in range(0,100):
        # try:
        time_stamp = get_time_stamp().__str__()
        current_time = get_current_time().__str__()
        alt = get_alt_int().__str__()
        lat = get_lat_int().__str__()
        lon = get_lon_int().__str__()

        
        write_log(current_time, lon, lat, alt, time_stamp)

        # except:
        #     print('No GPS data received. Try to reconnect')
                                                              

    # while i<1000:
    #     i+=1
    #     try:  
    #         current_time = datetime.datetime.now()
    #         lon =  the_connection.messages['GPS_RAW_INT'].lon
    #         lat = the_connection.messages['GPS_RAW_INT'].lat
    #         altitude=the_connection.messages['GPS_RAW_INT'].alt  # Note, you can access message fields as attributes! 
    #         timestamp=the_connection.time_since('GPS_RAW_INT') 
    #         print("Altitude is " + str(altitude)) 
    #         print("Longtitude is " + str(lon)) 

    #         print("Latitude is " + str(lat))

    #         print("Time since the start is " + str(timestamp)) 
    #         print("The real time now is " + str(current_time))

    #         print(i)
    #     except: 
    #         print('No GPS_RAW_INT message received')
        