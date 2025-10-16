#Uso do decorator de log e timer
from utils_log import log_decorator
from timer_decorator import time_measure_decorator
# pydantic
# pandera
import time

@time_measure_decorator
# @log_decorator
def soma(x, y):
    time.sleep(2)
    return x + y

soma(2, "3")
soma(2, 3)



