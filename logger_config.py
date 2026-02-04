import logging


def logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    fmt = logging.Formatter("%(name)s - %(levelname)s - %(message)s")

    # Handler pour la console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(fmt)

    # Handler pour le fichier de log
    file_handler = logging.FileHandler("app.log", encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(fmt)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger


log = logger()

logging.debug("Test pour la console")
logging.info("Test pour l'info")
logging.warning("Test pour lwarning")
