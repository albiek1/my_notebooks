import argparse
import csv

def print_file_content(file):
    with open(file) as file_object:
        print(file_object.read())

def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as file_object:
        for i in lst:
            file_object.write(i+'\n')

def read_csv(input_file):
    with open(input_file) as file_object:
        result = []
        reader = csv.reader(file_object)
        header_row = next(reader)
        my_comp = [result.insert(reader.line_num, row[0]) for row in reader]
        return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='program that does stuff with files')
    parser.add_argument('path', help='file path')
    parser.add_argument('--file', '--file_name', help='file_name to write to')

    args = parser.parse_args()
    if args.file == None:
        print_file_content(args.path))
    else:
        write_list_to_file(args.file, read_csv(args.path))