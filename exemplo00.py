from loguru import logger
import getpass
username = getpass.getuser()
#from sys import stderr

logger.add("meu_log.log")

#Trocando print por logger

logger.add("meu_app.log", level="CRITICAL")

def soma(x, y):
    try:
        soma = x + y
        logger.info("soma realizada com sucesso{soma}")
        return soma
    except:
        logger.critical("Erro ao somar")

soma(2, "3")
soma(2, 3)

