import sys
import argparse

def get_execution_args():
    filename = sys.argv[1]
    print(filename)

def get_file():
    return open(sys.argv[1])

def read_input(sys):
    return sys.stdin

def main():
    try:
        print(get_file().read())
    except Exception:
        print('Could not open file')

if __name__ == '__main__':
    main()