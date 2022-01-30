import logging

# process : 01 (printing log to terminal)
# let's look at the default behaviours of logging module.logger default level is warning.
# logging has 5 levels : warning, error, critical logs are printed by default.
# debug and info are neglected but if we set level to logging.DEBUG then all levels 
# that are greater than or equal to that level will be printed

#logging.basicConfig(level=logging.DEBUG)
logging.debug('DEBUG message')
logging.info('INFO message')
logging.warning('INFO message')
logging.error('INFO message')
logging.critical('INFO message')

