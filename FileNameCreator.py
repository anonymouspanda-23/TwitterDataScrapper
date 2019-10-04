import datetime


def create_file_name(twitter_username, language):
    twitter_username.replace(' ', '_')
    current_time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    filename = 'downloaded_data/' + twitter_username + '_' + current_time + '_' + language + '.csv.'
    return str(filename)
