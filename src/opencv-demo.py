import cv2
import time

class CameraInst():
    def __init__(self):
        fps = 20.0
        resolution = (640, 480)
        w = 640
        h = 480

        self.cap = cv2.VideoCapture(0)
        print('Camera warming up')
        time.sleep(1)
        
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'H264') # could also use (*'XDIV')
        self.out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

    def captureVideo(self):
        self.ret, self.frame = self.cap.read()
        # Manipulate the image here
        self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', self.gray)

    def saveVideo(self):
        # Write frame
        self.out.write(self.frame)

    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()
        print('Camera disabled and all output windows closed...')


def main():
    cam1 = CameraInst()
    while(True):
        # Display the resulting frames
        cam1.captureVideo()
        cam1.saveVideo()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    #cleanUp()

if __name__ == '__main__':
    main()
