from logging import getLogger, FileHandler, Formatter


log = getLogger("dictionaries")
level = "DEBUG"
file_handler = FileHandler("logging.txt")
format = '%(asctime)%:%(levelname)%:%(message)%'
formatter = Formatter(format)
file_handler.setFormatter(formatter)
file_handler.setLevel(level=level)
log.exception('message')
log.addHandler(file_handler)