class CommonContainer():
	def __init__(self):
		pass

	def _get_logger(self):
			import logging
			logger = logging.getLogger(__name__)
			logger.setLevel(logging.INFO)
			handler = logging.FileHandler('logs.log')
			handler.setLevel(logging.INFO)
			formatter = logging.Formatter('[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s')
			handler.setFormatter(formatter)
			logger.addHandler(handler)
			return logger
