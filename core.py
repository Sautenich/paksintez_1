"""Entry point for paksintez_1."""

#from .cli import main  # pragma: no cover
import pyyolo
#import mavlink_listener
import sys
import numpy as np
import cv2


darknet_path = './darknet' 
datacfg = 'cfg/coco.data' 
cfgfile = 'cfg/tiny-yolo.cfg' 
weightfile = '../tiny-yolo.weights' 
filename = darknet_path + '/data/dog.jpg' 
thresh = 0.45 
hier_thresh = 0.5
#BS
# sys.path.insert(1, '../darknet/')

# #import darknet_video


# if __name__ == "__main__":  # pragma: no cover
    #darknet_video(cfg/coco.data cfg/yolov4-csp.cfg yolov4-csp.weights -ext_output videoplayback.mp4)
    #main()

    #print(hi)


    # cap = cv2.VideoCapture('../darknet/videoplayback.mp4')
    # meta_filepath = "../darknet/cfg/coco.data"
    # cfg_filepath = "../darknet/cfg/yolov4-csp.cfg"
    # weights_filepath = "../darknet/yolov4-csp.weights"


    # meta = pyyolo.load_meta(meta_filepath)
    # net = pyyolo.load_net(cfg_filepath, weights_filepath, False)

    # while(cap.isOpened()):
    #     ret, frame = cap.read()
    #     if not ret:
    #         break

    #     yolo_img = pyyolo.array_to_image(frame)
    #     res = pyyolo.detect(net, meta, yolo_img)

    #     for r in res:
    #         cv2.rectangle(frame, r.bbox.get_point(pyyolo.BBox.Location.TOP_LEFT, is_int=True),
    #                     r.bbox.get_point(pyyolo.BBox.Location.BOTTOM_RIGHT, is_int=True), (0, 255, 0), 2)


    #     cv2.imshow('frame', frame)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break

    # cap.release()
    # cv2.destroyAllWindows()