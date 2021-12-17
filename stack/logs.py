LOGLEVEL = os.environ.get('LOGLEVEL', 'info').upper()

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            # exact format is not important, this is the minimum information
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
        'django.server': DEFAULT_LOGGING['formatters']['django.server'],
    },
    'handlers': {
        # console logs to stderr
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        # Add Handler for Sentry for `warning` and above
        'file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_FILE_NAME,
            'maxBytes': 1024 * 1024 * 10,  # 10MB
            'backupCount': 10,
            'formatter': 'default',
        },
        'django.server': DEFAULT_LOGGING['handlers']['django.server'],
    },
    'loggers': {
        # default for all undefined Python modules
        '': {
            'level': LOGLEVEL,
            'handlers': ['console', 'file'],
            'propagate': True
        },
        # Default runserver request logging
        'django.server': DEFAULT_LOGGING['loggers']['django.server'],
    },
})




LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'formatters': {
      'simple': {
            'format': '%(asctime)s %(levelname)s %(name)s %(lineno)d %(message)s %(module)s %(filename)s %(funcName)s ',
            'format': '%(asctime)s %(levelname)s %(lineno)d %(module)s %(filename)s %(funcName)s %(name)s %(message)s '
        },
  },
  'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'logstash': {
            'level': 'DEBUG',
            'class': 'logstash.TCPLogstashHandler',
            'host': 'localhost',
            'port': 5959, # Default value: 5959
            'version': 1, # Version of logstash event schema. Default value: 0 (for backward compatibility of the library)
            'message_type': 'ELK_DEMO_Application Staging Server',  # 'type' field in logstash message. Default value: 'logstash'.
            'fqdn': True, # Fully qualified domain name. Default value: false.
             'tags': ['ELK_DEMO_Application Staging Server'], # list of tags. Default: None.
        },
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/home/fero/workspace/elk_demo/stack/logs/file.log',
            'maxBytes': 1024*1024*15,  # 15MB
            'backupCount': 10,
            'formatter': 'simple',

        },
        
        
  },
  'loggers': {
        'stack': {
            'handlers': ['logstash','log_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        # 'django': {
        #     'handlers': ['console','log_file', 'logstash'],
        #     'propagate': True,
        #     'level': 'WARNING',
        # },
        
    }
}