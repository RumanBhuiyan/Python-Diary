import logging

# process : 02 (writing our log to a file)
# name , levelname, message are python known variables that are substituted 
logging.basicConfig(
    filename='file_logs.log',
    level=logging.DEBUG,
    filemode= 'w',
    format = '%(name)s - %(levelname)s - %(message)s'
)

logging.debug('DEBUG message')
logging.info('INFO message')
logging.warning('INFO message')
logging.error('INFO message')
logging.critical('INFO message')