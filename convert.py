import re


def convert_for_csv(retrieved_list):
    temp = []  # temporary list for storing results
    tweets = []  # list for storing formatted results

    for i in range(retrieved_list.__len__()):
        # get required data from results
        tweet_text = retrieved_list[i].text
        current_tweet_date = retrieved_list[i].formatted_date
        previous_tweet_date = retrieved_list[i - 1].formatted_date
        current_thread_id = retrieved_list[i].convo_id
        previous_thread_id = retrieved_list[i - 1].convo_id
        current_author_id = retrieved_list[i].author_id
        previous_author_id = retrieved_list[i - 1].author_id

        #  regex to remove standard urls
        tweet_text = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', tweet_text)

        #  code to remove twitter image urls
        temp_list = tweet_text.split('pic.')
        for words in temp_list:
            if words.__contains__('twitter.com'):
                temp_list.remove(words)

        #  code to rejoin tweet without urls
        tweet_text = ''.join(temp_list)

        #  code to join tweet if user uses comment to continue tweet
        if current_thread_id == previous_thread_id and current_author_id == previous_author_id:
            if current_tweet_date > previous_tweet_date:  # if older tweet has later date than newer tweet
                tweet_text = temp[i - 1] + tweet_text
                temp.pop[i - 1]
                temp.insert(i - 1, tweet_text)
                tweet_text = ''
            else:  # if older tweet has older date than newer tweet
                tweet_text = tweet_text + temp[i - 1]
                temp.pop(i - 1)
                temp.insert(i - 1, '')

        # store tweets into temporary list for formatting if required
        temp.append(tweet_text)

    # remove empty indexes and store into tweets list
    for i in range(temp.__len__()):
        if temp[i] != '':
            tweets.append([temp[i]])

    return tweets
