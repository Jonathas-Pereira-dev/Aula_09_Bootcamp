from loguru import logger

logger.add("meu_log.log")

#Trocando print por logger

logger.add("meu_app.log")

def soma(x, y):
    try:
        soma = x + y
        logger.info("soma realizada com sucesso{soma}")
        return soma
    except:
        logger.critical("Erro ao somar")

soma(2, "3")
soma(2, 3)

