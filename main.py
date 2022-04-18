import speedtest
from threading import Thread
import csv
import datetime
from mover import move

f = open('all.csv', 'a', newline='')
writer = csv.writer(f)

f1 = open('off-to-on.csv', 'a', newline='')
writer1 = csv.writer(f1)


def open_files():
    global f, writer, f1, writer1
    f = open('all.csv', 'a', newline='')
    writer = csv.writer(f)
    f1 = open('off-to-on.csv', 'a', newline='')
    writer1 = csv.writer(f1)


def close_files():
    global f, f1
    f.close()
    f1.close()


def pause():
    Ping.paused = True
    wait_for_ping()
    print('Info: Process was paused')


def resume():
    Ping.paused = False
    print('Info: Process was resumed')


def wait_for_ping():
    print('Info: Waiting for Ping to finish actions')
    while Ping.in_action:
        pass


debug = False
path = '/Users/Jacob/Desktop/Coding/Python/WiFi-Logger/'


class PingThread(Thread):
    def __init__(self):
        super(PingThread, self).__init__()
        self.running = True
        self.paused = False
        self.last = None
        self.in_action = False

    def run(self):
        while self.running:
            while not self.paused:
                self.in_action = True
                try:
                    wifi = speedtest.Speedtest()
                    if self.last is not None and not self.last and wifi:
                        writer1.writerow(['Restored_at', datetime.datetime.now()])
                        if debug:
                            print('Debug: Added Restored-line')
                    self.last = True
                    row = [f'UP:{wifi.upload()}', f'DOWN:{wifi.download()}', f'DATE:{datetime.datetime.now()}']
                    writer.writerow(row)
                    if debug:
                        print('Debug: Added line to all-file')
                except Exception as e:
                    if self.last:
                        writer1.writerow(['Broke_at', datetime.datetime.now()])
                        if debug:
                            print('Debug: Added Broken-line')
                    self.last = False
                finally:
                    pass
                self.in_action = False


Ping = PingThread()
Ping.start()
while True:
    inp = input()
    match inp.lower():
        case 'pause':
            pause()
        case 'resume':
            resume()
        case 'status':
            print(Ping.last)
        case 'enable debug':
            debug = True
            print('Info: Debug is on')
        case 'disable debug':
            debug = False
            print('Info: Debug is off')
        case 'save':
            pause()
            close_files()
            move('all.csv')
            move('off-to-on.csv')
            open_files()
            resume()
        case 'exit':
            Ping.running = False
            pause()
            f.close()
            f1.close()
            break
