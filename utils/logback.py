import logging
import datetime

fecha = datetime.datetime.now()
formatter_date = fecha.strftime("%Y-%m-%d")
file_name = f'{formatter_date}.log'

logging.basicConfig(level=logging.INFO,
                    format='[%(levelname)s] - %(asctime)s ---> %(message)s',
                    filename=file_name,
                    filemode='w')