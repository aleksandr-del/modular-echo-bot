#!/usr/bin/env python3


from logger import logging_config
import logging
import logging.config

logging.config.dictConfig(logging_config)
logger = logging.getLogger("logger")
logger.info("Starting ...")
