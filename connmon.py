#!/usr/bin/python3

import psutil

def get_listening():
    conns = psutil.net_connections(kind='inet')
    print("Listening Ports")
    print("Proto\tLocal Address\tPort\tStatus\tPID")
    for conn in conns:
        if conn.status == psutil.CONN_LISTEN:
            print(f"{conn.family}\t{conn.laddr[0]}\t{conn.laddr[1]}\t{conn.status}\t{conn.pid}")
    

def main():
    get_listening()
    

if __name__ == '__main__':
    main()