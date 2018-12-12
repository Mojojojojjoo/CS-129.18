# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 21:04:52 2018

@author: Gwapito
"""
import cv2

def decom(fname):
    fn = fname.split('.')[0]
    i=0
    cap = cv2.VideoCapture(fn+'.mp4')
    last = 5# int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    while(cap.isOpened()) and i<last:
        ret, frame = cap.read()        
        if ret==True:
            frame = cv2.resize(frame, None, fx=0.75, fy=0.75)
            cv2.imwrite(fn+"{0:0>5}".format(i)+'.jpg',frame)    
            i=i+1
            
    print (i)
    cap.release()
    cv2.destroyAllWindows()
    
decom("1.mkv")