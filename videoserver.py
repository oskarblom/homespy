from gevent import monkey; monkey.patch_all()

import gevent
from gevent.fileobject import FileObject
from gevent.server import StreamServer

import sys




def hi():
    while True:
        sys.stderr.write("hi")
        gevent.sleep(3)

if __name__ == "__main__":
    sys.stdin = FileObject(sys.stdin)
    task = gevent.spawn(hi)

    for line in sys.stdin.readlines():
        print line
