import os
from argparse import ArgumentParser

from twitter_crawler import get_tweets

project_dir = os.path.dirname(os.path.abspath(__file__))


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--num-tweets', type=int, default=10)
    parser.add_argument('--username', type=str, default='')
    parser.add_argument('--query', type=str, default='')
    parser.add_argument('--lang', type=str, default='en')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    get_tweets(args)
    print('Retrieval Complete!')

#  currently works with, english, chinese and arabic
