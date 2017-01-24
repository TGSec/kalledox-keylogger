import argparse
import keyboard

parser = argparse.ArgumentParser()

parser.add_argument('-o', '--output', help='define the output keys file.', action='store_value')
parser.add_argument('-s', '--stdout', 'define the output keys as the console stdout (incompatible with -q and -v.', action='store_true')
parser.add_argument('-t', '--timeout', help='define the maximum time (in seconds) of keylogger execution.', action='store_true')
parser.add_argument('-q', '--quiet', help='make the keylogger don\'t print nothing at the stdout (incompatible with -v and -s).')
parser.add_argument('-v', '--verbose', help='make the keylogger print more information at the stdout (incompatible with -q and -s).')

args = parser.parse_args()
