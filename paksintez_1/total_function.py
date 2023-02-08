from pymavlink import mavutil 
import time 
import datetime
import serial
print('Hello World') 

import sys
import numpy as np
import cv2
import pyyolo


i = 0

dets = 0
sys.path.insert(1, '../darknet')

def get_detections():
    global dets
    detector = pyyolo.YOLO("./cfg/yolov4-csp.cfg",
                           "./yolov4-csp.weights",
                           "./cfg/coco.data",
                           detection_threshold = 0.25,  #default = 0.5
                           hier_threshold = 0.5,    #default = 0.5
                           nms_threshold = 0.7) #defalut = 0.45

    # cap = cv2.VideoCapture(0)

    # cap = cv2.VideoCapture('rtsp://admin:VIMvideo12345678@192.168.31.114/Streaming/Channels/101')
    cap = cv2.VideoCapture('output.mp4')


    while True:
        ret, frame = cap.read()
        dets = detector.detect(frame, rgb=False)
       
        
        
        for i, det in enumerate(dets):
            
            a = (f'Detection: {i}, {det}')
            print(a)
            print(type)

            xmin, ymin, xmax, ymax = det.to_xyxy()
            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 0, 255),2)
            write_log(a)

        cv2.imshow('cvwindow', frame)
        

        if cv2.waitKey(1) == 27:
            break
        

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



def write_log(a):
    
    
    time_stamp = get_time_stamp().__str__()
    current_time = get_current_time().__str__()
    alt = get_alt_int().__str__()
    lat = get_lat_int().__str__()
    lon = get_lon_int().__str__()
    timestr = time.strftime("%H%M%S-%D%M%Y") + ".txt"

    log = open("timestr10.txt", 'a+')
    print ('a =', a)
    print ('type a =', type(a))

    log.write("=======================================================\nОбъект:%s\nВремя: %s\nШирота: %s\nДолгота: %s\nВысота: %s\nВремя с начала старта: %s \n" %(a, current_time, lon, lat, alt, time_stamp))
    log.close()                        
    
    

if __name__ == '__main__':

    try:
        start_connection()
        print('Connection established')
    except:
        print('No connection established')

    get_detections()

    
    
    