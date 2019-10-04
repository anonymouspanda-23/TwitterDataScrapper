import csv
from file_name_creator import create_file_name


def save_to_csv(tweet, username, query, language):
    # if crawler returns at least 1 tweet
    if tweet.__len__() > 0:

        # create file name
        filename = create_file_name(username, query, language)

        # open and write file
        with open(filename, mode='w+', newline='', encoding='utf-16') as data_file:
            data_writer = csv.writer(data_file, delimiter=',', quotechar='"')

            for i in range(tweet.__len__()):
                data_writer.writerow(tweet[i])

            # close file after writing
            data_file.close()
