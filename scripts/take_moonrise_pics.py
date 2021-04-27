from picamera import PiCamera
from time import sleep

camera = PiCamera()

media_path = '/home/pi/glorious-sunrise/media'


shortlisted_exposure_modes = ['off', 'auto', 'night', 'nightpreview', 'backlight', 'spotlight', 'sports', 'snow', 'beach', 'verylong', 'fixedfps', 'antishake', 'fireworks']
for i in range(1, 10):
    for exposure_string in shortlisted_exposure_modes:
        sleep(5)
        print(camera.digital_gain)
        print(camera.analog_gain)
        camera.exposure_mode = exposure_string
        camera.capture('{0}/image{1:04d}.jpg'.format(media_path, i))
        print('Taking picture numer {}'.format(i))
