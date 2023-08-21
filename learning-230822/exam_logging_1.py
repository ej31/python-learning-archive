import logging

# 기본 로깅 설정 (로그 레벨을 WARNING으로 설정)
logging.basicConfig(level=logging.WARNING)

# 다양한 로그 레벨의 메시지 기록
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
