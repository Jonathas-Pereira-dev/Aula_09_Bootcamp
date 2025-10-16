from loguru import logger

#Trocando print por logger

logger.add("meu_app.log")

def soma(x, y):
    logger.info(x)
    logger.info(y)
    logger.info(x + y)
    return x + y

soma(2, 3)

