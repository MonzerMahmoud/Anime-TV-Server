BASE_URL = 'https://animetak.vip/'
WATCH_URL = BASE_URL + 'watch_episodes/'

def getDBZURL(episode):
    return WATCH_URL + '%D8%A7%D9%86%D9%85%D9%8A-dragon-ball-z-%D8%A7%D9%84%D8%AD%D9%84%D9%82%D8%A9-{}-%D9%85%D8%AA%D8%B1%D8%AC%D9%85%D8%A9-%D8%A7%D9%88%D9%86-%D9%84%D8%A7%D9%8A%D9%86.html'.format(episode)

def get_black_clover_url(episode):
    
    return WATCH_URL + 'hunter-x-hunter-%D8%A7%D9%84%D8%AD%D9%84%D9%82%D8%A9-{}-%D9%85%D8%AA%D8%B1%D8%AC%D9%85%D8%A9.html'.format(episode)