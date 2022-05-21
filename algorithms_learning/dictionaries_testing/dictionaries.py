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

def find_dublicate(list) -> list:
    dub = []
    log.debug("About to start functino!")
    if list == []:
        log.debug("You cannot chack for empy list!")
    for i in range(len(list)):
        for j in range(i, len(list)):
            if list[i] == list[j]:
                dub.append(list[i])
    return dub

find_dublicate([1,2,4,4,2,4,5,6,7,8,9,9])
    