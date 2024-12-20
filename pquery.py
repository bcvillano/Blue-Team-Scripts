#!/usr/bin/python3

import psutil
import argparse
import socket



def arg_setup():
    msg = "Command line tool for querying information about processes"
    parser = argparse.ArgumentParser(description = msg)
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument('id', help="pid of process to look up", type=int) #required argument
    return parser.parse_args()

def get_process_info(pid):
    process = psutil.Process(pid)
    cmdline = process.cmdline()
    cmdline_str = ""
    for arg in cmdline:
        cmdline_str += arg + " "
    print(f"Process ID: {pid}")
    print(f"Process Name: {process.name()}")
    print(f"Process User: {process.username()}")
    print(f"Process Path: {process.exe()}")
    print(f"Process Command: {cmdline_str}")
    print(f"Process Status: {process.status()}")
    print(f"Process Parent ID: {process.ppid()}")
    print(f"Process Parent Name: {psutil.Process(process.ppid()).name()}")



def verbose(pid):
    files = psutil.Process(pid).open_files()
    conns = psutil.net_connections(kind='inet')
    print(f"Process Open Files: ", end="")
    for file in files:
        print(file.path, end=", ")
    print(f"\nProcess Connections:")
    for conn in conns:
        if conn.pid == pid:
            conn_type = "TCP" if conn.type == socket.SOCK_STREAM else "UDP" if conn.type == socket.SOCK_DGRAM else "UNKNOWN"
            print(f"\tConnection Type: {conn_type}")
            try:
                if isinstance(conn.laddr, tuple):
                    print(f"\tLocal Address: {conn.laddr[0]}:{conn.laddr[1]}")
                if isinstance(conn.raddr, tuple):
                    print(f"\tRemote Address: {conn.raddr[0]}:{conn.raddr[1]}")
            except:
                pass #skips unprintable information
            print(f"\tStatus: {conn.status}\n")


def main():
    args = arg_setup()
    get_process_info(args.id)
    if args.verbose:
        verbose(args.id)


if __name__ == '__main__':
    main()