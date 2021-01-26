#Here is an archive of other code related to the topic that we can use later

def fn1():
    import time
    import cv2
    #pip install mss
    import mss
    import numpy

    with mss.mss() as sct:
        # Part of the screen to capture
        monitor = {"top": 40, "left": 0, "width": 800, "height": 640}
        
        #fourcc = cv2.VideoWriter_fourcc(*'XVID')
        #out = cv2.VideoWriter('output2021.avi', fourcc, 20.0, (800,640))

        while "Screen capturing":
            last_time = time.time()
            # Get raw pixels from the screen, save it to a Numpy array
            img = numpy.array(sct.grab(monitor))
            ##################out.write(img)
            # Display the picture
            #cv2.imshow("OpenCV/Numpy normal", img)

            # Display the picture in grayscale
            image=cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
            cv2.imshow('OpenCV/Numpy grayscale',img)

            print("fps: {}".format(1 / (time.time() - last_time)))
  
            # Press "q" to quit
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break
    ######out.release()


    
def fn2():
    import numpy as np
    import cv2

    cap = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            frame = cv2.flip(frame,0)


            out.write(frame)

            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    
    cap.release()

    out.release()

    cv2.destroyAllWindows()

def fn3():
    # capture.py
    import numpy as np
    import cv2

    # Capture video from camera
    # cap = cv2.VideoCapture(0)

    # Capture video from file
    cap = cv2.VideoCapture('BlueUmbrella.webm')

    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()

    cv2.destroyAllWindows()
