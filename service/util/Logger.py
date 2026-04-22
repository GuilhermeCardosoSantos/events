# util/logger.py
import os
import logging
from datetime import datetime

def log(router: str, func: str, message: str, exception: Exception = None, level: str = "error"):
    """
    Cria um log global por aplicação e data, com suporte a diferentes níveis de log.

    Estrutura de pastas:
        logs/<router>/<YYYY-MM-DD>/<func>_<HH-MM-SS>.log

    Parâmetros:
    - router: nome do aplicativo ou módulo (ex: "point", "crawler")
    - func: nome da função onde o log é gerado
    - message: mensagem descritiva
    - exception: exceção capturada (opcional)
    - level: nível do log ('error', 'warning', 'info', 'debug'), padrão='error'

    Esse logger centraliza mensagens críticas ou informativas por router e função.
    """
    # Pasta de logs por router e data
    today = datetime.now().strftime("%Y-%m-%d")
    log_dir = os.path.join("logs", router, today)
    os.makedirs(log_dir, exist_ok=True)

    # Arquivo de log com hora
    timestamp = datetime.now().strftime("%H-%M-%S")
    log_file = os.path.join(log_dir, f"{func}_{timestamp}.log")

    # Configura logger
    logger = logging.getLogger(f"{router}.{func}")
    logger.setLevel(logging.DEBUG)  # captura todos os níveis

    # Remove handlers antigos
    if logger.hasHandlers():
        logger.handlers.clear()

    # Handler de arquivo
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Mapear string level para função de logging
    level_map = {
        "error": logger.error,
        "warning": logger.warning,
        "info": logger.info,
        "debug": logger.debug,
    }
    log_func = level_map.get(level.lower(), logger.error)

    # Loga a mensagem
    if exception:
        log_func(f"{message}: {exception}", exc_info=True)
    else:
        log_func(message)