from picamera import PiCamera
from time import sleep

camera = PiCamera()

media_path = '/home/pi/glorious-sunrise/media'

# camera.exposure_mode = 'spotlight'

for i in range(1, 10):
    print('Taking picture numer {}'.format(i))
    camera.capture('{0}/image{1:04d}.jpg'.format(media_path, i))
    sleep(5)
