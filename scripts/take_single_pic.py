from picamera import PiCamera

camera = PiCamera()

media_path = '/home/pi/glorious-sunrise/media'

camera.capture('{}/image.jpg'.format(media_path))
