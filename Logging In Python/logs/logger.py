import logging

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

## Configuring logging

logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d  %H:%M:%S'
)

## Log messeages
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("Thisis a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")