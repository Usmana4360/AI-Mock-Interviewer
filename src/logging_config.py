import logging

def setup_logging(log_file="app.log"):
    logging.basicConfig(
        level=logging.DEBUG,  # Adjust to INFO or WARNING for production
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),  # Log to a file
            logging.StreamHandler()  # Log to the console
        ]
    )
    return logging.getLogger()
