import logging as log

# 기본 로깅 설정 (로그 레벨을 WARNING으로 설정)
log.basicConfig(level=log.WARNING)

# 다양한 로그 레벨의 메시지 기록
log.debug("This is a debug message")  # 0
log.info("This is an info message")  # 1
log.warning("This is a warning message")  # 2
log.error("This is an error message")  # 3
log.critical("This is a critical message")  # 4
