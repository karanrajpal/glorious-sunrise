from picamera import PiCamera
from time import sleep

camera = PiCamera()

media_path = '/home/pi/glorious-sunrise/media'


for i in range(1, 10):
    sleep(5)
    camera.exposure_mode = 'spotlight'
    print('Taking picture numer {}'.format(i))
    camera.capture('{0}/image{1:04d}.jpg'.format(media_path, i))
