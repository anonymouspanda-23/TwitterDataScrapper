import re
import csv


def read_file(filename, file_dir, is_external_file):
    if filename == '':
        print('File Name cannot be empty!')
        return 0
    else:
        if re.match('.+(\\.csv)$', filename):
            filename = file_dir + filename
            if is_external_file:
                with open(filename, encoding='utf-8') as csv_file:
                    reader = csv.DictReader(csv_file, delimiter=',')
                    print('Titles: \n')
                    i = 1
                    for row in reader:
                        titles = row['recordTitle']
                        print('Title ' + str(i) + ': ' + titles)
                        i = i + 1
            else:
                with open(filename, encoding='utf-16') as csv_file:
                    reader = csv.reader(csv_file, delimiter=',')
                    print('Articles: \n')
                    i = 1
                    for row in reader:
                        for column in row:
                            print('Article ' + str(i) + ': ' + column)
                            i = i + 1
        else:
            print('Program unable to read file formats other than csv!')
