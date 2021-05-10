from picamera import PiCamera
import os
from os import system
from time import sleep
import argparse
from notifier import send_email

# Setup argument parsing and use defaults
parser = argparse.ArgumentParser()
parser.add_argument("--number_of_images", "-n", default=150, type=int)   # integer
parser.add_argument("--capture_interval", "-i", default=30, type=int)    # seconds
parser.add_argument("--gif_image_delay", "-g", default=10, type=int)    # milliseconds
parser.add_argument("--compress", "-c", default=False, type=bool)    # milliseconds
parser.add_argument("--output_file_name", "-o", default='animation', type=str)    # milliseconds
args = parser.parse_args()

media_path = '/home/pi/glorious-sunrise/media'
timestamp=system('date +%m_%d_%Y_%I_%M_%S')
output_file_name='animation_{}'.format(timestamp)
output_file_path = '{}/{}.gif'.format(media_path, output_file_name)

print('Clearing out previous media')
system('rm {}/*.jpg'.format(media_path))
system('mkdir -p {}'.format(media_path))

camera = PiCamera()
if (args.compress):
    camera.resolution = (640, 480)

camera.exposure_mode = 'spotlight'

for i in range(args.number_of_images):
    print('Taking picture numer {}'.format(i))
    camera.capture('{0}/image{1:04d}.jpg'.format(media_path, i))
    sleep(args.capture_interval)

print('Done taking pics. Generating GIF')
system('convert -delay {} -loop 0 {}/image*.jpg {}'.format(args.gif_image_delay, media_path, output_file_path))
system('gifsicle -O3 --scale 0.8 {} -o {}'.format(output_file_path, output_file_path))
print('done converting GIFs')
# send_email(
#     os.environ['SUNRISE_RECIPIENT'],
#     'It''s a glorious sunrise!',
#     'Check out this amazing animation of the sunrise that you missed while you were asleep',
#     [output_file_path]
# )
