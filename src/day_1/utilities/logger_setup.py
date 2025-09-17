import logging
import toml
import os
from logging.handlers import RotatingFileHandler

def setup_logger():
    """
    Set up logging configuration from a TOML file.
    It uses the default config/logger_config.toml.
    Logs are stored in logs/rag.log with rotation (3 files, 1KB each).
    """
    # Define Core Paths 
    config_path = "config/logger_config.toml"  # Path to the configuration file.
    logs_dir = "logs"  # Directory where log files will be stored.

    # Read the Configuration File 
    with open(config_path, 'r', encoding='utf-8') as f:
        config = toml.load(f)

    # Retrieve settings 
    log_level = config.get('log', {}).get('level', 'INFO')
    log_format = config.get('log', {}).get('format', '%(asctime)s - %(levelname)s - %(message)s')
    log_file = config.get('log', {}).get('file', 'rag.log')


    # Ensure the logs directory exists; if not, create it.
    os.makedirs(logs_dir, exist_ok=True)

    # Construct the full path to the log file.
    logging_file = os.path.join(logs_dir, log_file)

    # Configure the File Handler (with Log Rotation) 
    handler = RotatingFileHandler(logging_file, maxBytes=1024, backupCount=3, encoding='utf-8')

    # Define the format for the log messages...
    formatter = logging.Formatter(log_format)

    # ...and apply it to our handler.
    handler.setFormatter(formatter)

    # Configure the Root Logger 
    root_logger = logging.getLogger()

    # Set the minimum level of messages to be logged (e.g., INFO, DEBUG, ERROR).
    root_logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))

    # IMPORTANT: Clear any existing handlers attached to the root logger.
    for h in root_logger.handlers[:]:
        root_logger.removeHandler(h)
    
    # Add our configured file handler to the root logger.
    root_logger.addHandler(handler)

    # Optional: Add a Handler for Console Output 
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    root_logger.addHandler(stream_handler)

    # Log an initial message to confirm that the logger was set up successfully.
    logging.info(f"Logger initialized with level {log_level}, format '{log_format}', file '{log_file}' (3 files, 1KB each)")