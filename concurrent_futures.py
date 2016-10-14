#!/usr/bin/env python

from concurrent.futures import ThreadPoolExecutor as Executor
import logging
logger = logging.getLogger()

#logger.debug('debug:This is for debugging. Very talkative!')
#logger.info('info:This is for normal chatter')
#logger.warning('Warning:s should almost always be seen.')
#logger.error('error:You definitely want to see all errors!')
#logger.critical('Last message before a program crash!')
#urls = """google twitter facebook youtube pinterest tumblr
#instagram reddit flickr meetup classmates microsoft apple
#linkedin xing renren disqus snapchat twoo whatsapp""".split()
if __name__ == '__main__':
        from argparse import ArgumentParser
        parser = ArgumentParser(description='MyApp', add_help=False, prog="concurrent.futures", epilog='MyNameIsRishi')
        parser.add_argument('-ll', '--loglevel',
                type=str,
                choices=['DEBUG','INFO','WARNING','ERROR','CRITICAL'],
                help='Set the logging level: %(prog)s')
        #print("parse_args:", parser.parse_args)
        args = parser.parse_args()
        #parser.print_help()
        #print ("args:", args)
        logging.basicConfig(level=args.loglevel)


urls = """google twitter121 facebook""".split()
def fetch(url):
	from urllib import request, error
	try:
		data = request.urlopen(url).read()
		return '{}: length {}'.format(url, len(data))
	except error.HTTPError as e:
		print(e.code)
		print(e.read())
		logger.exception("Something failed:")
		logger.critical('CRITICAL MSG: URL NOT RESPONDING!')
		return '{}: {}'.format(url, e)

with Executor(max_workers=4) as exe:
	logger.info('info:This is for normal chatter')
	template = 'http://www.{}.com'
	jobs = [exe.submit(
		fetch, template.format(u)) for u in urls]
	results = [job.result() for job in jobs]
print('\n'.join(results))


