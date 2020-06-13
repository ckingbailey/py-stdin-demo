import sys
import json

def read_json_file(filepath:str):
    return json.loads(open(filepath).read())

def handle_json(file_list:list):
    for filename in file_list:
        prompt = f'Is this the file you wanted: {filename}? [y/n] '
        res = input(prompt)
        while res not in [ 'y', 'n' ]:
            res = input(f'Please enter y or n. {prompt}')
        msg = 'we\'ll handle that' if 'y' == res else 'we\'ll skip this one'
        print(f'Thanks, {msg}')

def main():
    try:
        json_file = read_json_file(sys.argv[1])
        handle_json(json_file['files'])
    except OSError:
        print('Could not open file')

if __name__ == '__main__':
    main()