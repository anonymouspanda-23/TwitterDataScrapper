import datetime


def create_file_name(twitter_username, query, language):
    # get current datetime
    current_time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

    # if user searches by username
    if query == '':
        twitter_username = twitter_username.replace(' ', '_')
        filename = 'downloaded_data/' + twitter_username + '_' + current_time + '_' + language + '.csv.'

    # else if user searches by query
    elif twitter_username == '':
        query = query.replace(' ', '_')
        filename = 'downloaded_data/' + query + '_' + current_time + '_' + language + '.csv.'

    # else if user searches by both username and query
    else:
        query.replace(' ', '_')
        twitter_username.replace(' ', '_')
        filename = 'downloaded_data/' + twitter_username + '_' + query + '_' + current_time + '_' + language + '.csv.'

    return str(filename)
