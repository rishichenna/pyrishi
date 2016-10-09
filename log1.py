#!/usr/bin/env python
import logging
logger = logging.getLogger()


if __name__ == '__main__':
	from argparse import ArgumentParser
	parser = ArgumentParser(description='My app which is mine', add_help=True, prog="MYPROG099", epilog='MyNameIsRishi')
	parser.add_argument('-ll', '--loglevel',
		type=str,
		choices=['DEBUG','INFO','WARNING','ERROR','CRITICAL'],
		help='Set the logging level: %(prog)s')
	#print("parse_args:", parser.parse_args)
	args = parser.parse_args()
	parser.print_help()
	#print ("args:", args)
	logging.basicConfig(level=args.loglevel)

logger.debug('debug:This is for debugging. Very talkative!')
logger.info('info:This is for normal chatter')
logger.warning('Warning:s should almost always be seen.')
logger.error('error:You definitely want to see all errors!')
logger.critical('Last message before a program crash!')

'''
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Start reading database')
# read database here
records = {'john': 55, 'tom': 66}
logger.debug('Records: %s', records)
logger.info('Updating records ...')
# update records here
logger.info('Finish updating records')
'''
