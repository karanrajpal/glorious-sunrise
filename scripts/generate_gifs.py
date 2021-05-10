system('convert -delay {} -loop 0 {}/image*.jpg {}'.format(args.gif_image_delay, media_path, output_file_path))
system('gifsicle -O3 --scale 0.8 {} -o {}'.format(output_file_path, output_file_path))