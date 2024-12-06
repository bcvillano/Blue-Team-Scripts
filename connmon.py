#!/usr/bin/python3

import psutil
import socket

#COLOR CODE CONTANTS
RED = "\033[91m"
RESET = "\033[0m"

def get_listening():
    conns = psutil.net_connections(kind='inet')
    print(f"{RED}Listening Ports{RESET}")
    print("Proto\tLocal Address\t\t Port\t  Status    PID")
    for conn in conns:
        if conn.status == psutil.CONN_LISTEN:
            proto = "TCP" if conn.type == socket.SOCK_STREAM else "UDP" if conn.type == socket.SOCK_DGRAM else "UNKNOWN"
            local_ip = conn.laddr.ip if conn.laddr else "*"
            local_port = conn.laddr.port if conn.laddr else "*"
            print(f"{proto:<8}{local_ip:<25}{local_port:<8} {conn.status:<10}{conn.pid:<10}")

def get_established():
    conns = psutil.net_connections(kind='inet')
    print(f"\n\n{RED}Established Connections{RESET}")
    print("Proto\tLocal Address\t\t Local Port\tRemote Address\tRemote Port\t Status        PID")
    for conn in conns:
        if conn.status == psutil.CONN_ESTABLISHED:
            proto = "TCP" if conn.type == socket.SOCK_STREAM else "UDP" if conn.type == socket.SOCK_DGRAM else "UNKNOWN"
            local_ip = conn.laddr.ip if conn.laddr else "*"
            local_port = conn.laddr.port if conn.laddr else "*"
            remote_ip = conn.raddr.ip if conn.raddr else "*"
            remote_port = conn.raddr.port if conn.raddr else "*"
            print(f"{proto:<8}{local_ip:<25}{local_port:<15}{remote_ip:<16}{remote_port:<17}{conn.status:<14}{conn.pid:<10}")
            
    

def main():
    get_listening()
    get_established()
    

if __name__ == '__main__':
    main()