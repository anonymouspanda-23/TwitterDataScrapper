from argparse import ArgumentParser
from twitter_crawler import get_tweets
from file_reader import read_file


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--num-tweets', type=int, default=10)
    parser.add_argument('--username', type=str, default='')
    parser.add_argument('--query', type=str, default='')
    parser.add_argument('--lang', type=str, default='en')
    parser.add_argument('--read-file', type=bool, default=False)
    parser.add_argument('--file-name', type=str, default='')
    parser.add_argument('--file-dir', type=str, default='imported_data/')
    parser.add_argument('--external-file', type=bool, default=False)

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    if args.read_file is True:
        read_file(args.file_name, args.file_dir, args.external_file)
    else:
        get_tweets(args)
    print('Retrieval Complete!')

#  currently works with, english, chinese and arabic
