import GetOldTweets3 as TwitterCrawler
from file_writer import save_to_csv
from convert import convert_for_csv


def get_tweets(args):
    print('\n')

    # require user to search by either username or query
    if args.username == '' and args.query == '':
        print('Either username or query has to be defined!')
    else:
        print('Username: ' + args.username)
        print('Query: ' + args.query)
        print('Language: ' + args.lang)
        print('Max Tweets: ' + str(args.num_tweets))

        # if search by query
        if args.username == '':
            tweet_criteria = TwitterCrawler.manager.TweetCriteria().setQuerySearch(args.query).setLang(args.lang).setMaxTweets(args.num_tweets)

        # else if search by username
        elif args.query == '':
            tweet_criteria = TwitterCrawler.manager.TweetCriteria().setUsername(args.username).setLang(args.lang).setMaxTweets(args.num_tweets)

        # else if search by query and username
        else:
            tweet_criteria = TwitterCrawler.manager.TweetCriteria().setUsername(args.username).setQuerySearch(args.query).setLang(args.lang).setMaxTweets(args.num_tweets)

        # crawl data
        tweet = TwitterCrawler.manager.TweetManager.getTweets(tweet_criteria)
        print('Number of tweets and comments retrieved: ' + str(tweet.__len__()))

        # remove urls and other formatting
        tweet = convert_for_csv(tweet)

        # save results from query to csv file
        save_to_csv(tweet, args.username, args.query, args.lang)
