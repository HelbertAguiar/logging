# Logging

Save few simple code demonstrating cases of use of python library known logging

    logging.basicConfig(
            filename = './log/main.log',
            filemode = 'w',
            level = logging.DEBUG,
            format = '%(asctime)s.%(msecs)03d %(levelname)8s %(module)s - %(funcName)s: %(message)s',
            datefmt = '%Y-%m-%d %H:%M:%S',
        ) 

## Links

https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
