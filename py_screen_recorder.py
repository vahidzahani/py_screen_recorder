def main():
    #pip install mss
  
    import cv2
    import numpy 
    import os
    import pyautogui
    import mss
    import time

    w_w,h_h = pyautogui.size()
    t=(round(time.time()))
    output = str(t)+"_video.avi"
    print("Frame Rate ? :")
    frm_rate=int(input())
    print("resolution > Width : "+str(w_w)+" - Height : "+str(h_h))
    print("file name > "+ output)
    print("[ RECORDING ... ] (close this window to stop)")

    with mss.mss() as sct:
        #img = pyautogui.screenshot()

        monitor = {"top": 0, "left": 0, "width": w_w, "height": h_h}
        img = numpy.array(sct.grab(monitor))
        #img = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
        #get info from img
        height, width, channels = img.shape
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(output, fourcc, frm_rate, (width, height))

        while(True):
            try:
                #img = pyautogui.screenshot()
                img = numpy.array(sct.grab(monitor))
                image = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
                image = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
                #image = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
                out.write(image)
                StopIteration(0.5)
            except KeyboardInterrupt:
                break

    out.release()
    cv2.destroyAllWindows()

main()#run my function main
