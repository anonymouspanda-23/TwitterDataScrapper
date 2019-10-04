import csv
from FileNameCreator import create_file_name


def save_to_csv(tweet, username, language):
    if tweet.__len__() > 0:
        filename = create_file_name(username, language)
        with open(filename, mode='w+', newline='', encoding='utf-16') as data_file:
            data_writer = csv.writer(data_file, delimiter=',', quotechar='"')

            for i in range(tweet.__len__()):
                data_writer.writerow(tweet[i])

            data_file.close()
