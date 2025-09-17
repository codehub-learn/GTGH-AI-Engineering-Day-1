import yaml
import logging


def setup_logging(config_path="config/config.yaml"):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    level = config.get("logging", {}).get("level", "INFO").upper()
    log_file = config.get("logging", {}).get("file", None)
    
    if log_file:
        logging.basicConfig(
            level=getattr(logging, level, logging.DEBUG),
            filename=log_file,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )
    else:
        logging.basicConfig(
            level=getattr(logging, level, logging.DEBUG),
            format="%(asctime)s - %(levelname)s - %(message)s",
        )
