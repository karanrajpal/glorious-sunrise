from picamera import PiCamera
from os import system
from time import sleep

camera = PiCamera()

media_path = '/home/pi/glorious-sunrise/media'
NUMBER_OF_PICS = 10
CLICK_GAP_S = 3

shortlisted_exposure_modes = ['spotlight']
for awb_string in PiCamera.AWB_MODES:
    for exposure_string in shortlisted_exposure_modes:
        sleep(CLICK_GAP_S)
        camera.exposure_mode = exposure_string
        camera.awb_mode = awb_string
        image_name = '{}/experimental_image_{}_{}.jpg'.format(media_path, exposure_string, awb_string)
        camera.capture(image_name)
        print('Done taking picture {}'.format(image_name))

print('Done taking pics')
