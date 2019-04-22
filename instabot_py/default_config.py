LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        },
        "user": {
            "format": "%(login)s - %(asctime)s - %(levelname)s - %(message)s"
        }

    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        }
    },
    "loggers": {
        "InstaBot": {
            "level": "DEBUG",
            "handlers": [
                "console"
            ],
            "propagate": "no"
        }
    },
    "root": {
        "level": "INFO"
    }
}

DEFAULT_CONFIG = {
    "config": {
        "file": "instabot.config.yml"

    },
    "logging": LOGGING_CONFIG,
    "debug": 0,
    "database": {
        "type": "sqlite3",
        "directory": "."

    },
    'unfollow_selebgram': False,
    'user_blacklist': {},
    'unfollow_probably_fake': True,
    'log_mod': 0,
    'start_at_h': 0,
    'start_at_m': 0,
    'follow_time_enabled': True,
    'follow_time': 18000,
    'unfollow_break_min': 15,
    'max_like_for_one_tag': 5,
    'session_file': None,
    'unfollow_not_following': True,
    'unfollow_break_max': 30,
    'comments_per_day': 0,
    'user_min_follow': 0,
    'tag_blacklist': [],
    'unfollow_recent_feed': True,
    'unlike_per_day': 0,
    'end_at_m': 59,
    'end_at_h': 23,
    'user_max_follow': 0,
    'comment_list': [['this', 'the', 'your'], ['photo', 'picture', 'pic', 'shot', 'snapshot'],
                     ['is', 'looks', 'feels', 'is really'],
                     ['great', 'super', 'good', 'very good', 'good', 'wow', 'WOW', 'cool', 'GREAT', 'magnificent',
                      'magical', 'very cool', 'stylish', 'beautiful', 'so beautiful', 'so stylish', 'so professional',
                      'lovely', 'so lovely', 'very lovely', 'glorious', 'so glorious', 'very glorious', 'adorable',
                      'excellent', 'amazing'], ['.', '..', '...', '!', '!!', '!!!']], 'proxy': '',
    'unfollow_per_day': 0,
    'follow_per_day': 0,
    'unwanted_username_list': [],
    'unfollow_whitelist': [],
    'unfollow_inactive': True,
    'media_max_like': 150,
    'database_name': None,
    'media_min_like': 0,
    'time_till_unlike': 259200,
    'unfollow_everyone': False,
    'tag_list': ['cat', 'car', 'dog'],
    'like_per_day': 1000,
    'accept_language': "en-US,en;q=0.5",

    # If you have 3 400 error in row - looks like you banned.
    'error_400_to_ban': 3,
    # If InstaBot think you are banned - going to sleep.
    'ban_sleep_time': 3 * 60 * 60,
    'list_of_ua': [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FSL 7.0.6.01001)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FSL 7.0.7.01001)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FSL 7.0.5.01003)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0",
        "Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.2.8) Gecko/20100723 Ubuntu/10.04 (lucid) Firefox/3.6.8",
        "Mozilla/5.0 (Windows NT 5.1; rv:13.0) Gecko/20100101 Firefox/13.0.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:11.0) Gecko/20100101 Firefox/11.0",
        "Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.2.8) Gecko/20100723 Ubuntu/10.04 (lucid) Firefox/3.6.8",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.0.3705)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
        "Opera/9.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.01",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows NT 5.1; rv:5.0.1) Gecko/20100101 Firefox/5.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.02",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112 Safari/535.1",
        "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.0) Opera 7.02 Bork-edition [en]",
    ]

}
