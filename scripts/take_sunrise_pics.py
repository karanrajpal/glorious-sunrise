from picamera import PiCamera
import os
from os import system
from time import sleep
import argparse
from notifier import send_email

# Setup argument parsing and use defaults
parser = argparse.ArgumentParser()
parser.add_argument("--number_of_images", "-n", default=10, type=int)   # integer
parser.add_argument("--capture_interval", "-i", default=5, type=int)    # seconds
parser.add_argument("--gif_image_delay", "-g", default=30, type=int)    # milliseconds
parser.add_argument("--compress", "-c", default=False, type=bool)    # milliseconds
args = parser.parse_args()

media_path = '/home/pi/glorious-sunrise/media'
print('Clearing out previous media')
system('rm -rf {}'.format(media_path))
system('mkdir {}'.format(media_path))

camera = PiCamera()
if (args.compress):
    camera.resolution = (720, 480)

for i in range(args.number_of_images):
    sleep(args.capture_interval)
    camera.capture('{0}/image{1:04d}.jpg'.format(media_path, i))
    print('Taking picture numer {}'.format(i))

print('Done taking pics. Generating GIF')
system('convert -delay {} -loop 0 {}/image*.jpg {}/animation.gif'.format(args.gif_image_delay, media_path, media_path))
print('done converting GIFs')
send_email(os.environ['SUNRISE_RECIPIENT'], 'It''s a glorious sunrise!', 'Check out this amazing animation of the sunrise that you missed while you were asleep', ['/home/pi/glorious-sunrise/media/animation.gif'])