import time
from loguru import logger
from functools import wraps


# Decorador de medida de tempo
def time_measure_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print.info(f"Função '{func.__name__}' executada em {end_time - start_time:.4f} segundos")
        return result
    return wrapper

# Exemplos de uso:
# def (x,y,z)
# (x=1, y=2, z=3)