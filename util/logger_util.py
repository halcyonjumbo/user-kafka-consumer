import logging

class LoggerUtil:
    def __init__(self):
        pass

    def get_logger(self, class_name: str) -> logging.Logger:
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(class_name)
        return self.logger