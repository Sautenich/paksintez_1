"""Entry point for paksintez_1."""

#from .cli import main  # pragma: no cover

import mavlink_listener
import sys
import numpy as np
import cv2
from threading import Thread
import mavlink_listener

#sys.path.insert(0, '../darknet')
import pyyolo
#import darknet_video
# from darknet import sample_detection
from darknet.sample_detection import get_detections
# from darknet.sample_detection import dets

t1 = Thread(target=get_detections)
t2 = Thread(target=mavlink_listener)


if __name__ == "__main__":  # pragma: no cover
    #darknet_video(cfg/coco.data cfg/yolov4-csp.cfg yolov4-csp.weights -ext_output videoplayback.mp4)
    #main()
    
    #detections = get_detections()
    print('detections')
    t1.start()
    dets = t1.dets
    print(dets)
    t2.start()
    # t1.join()
    #t2.join()
    #print('det')

