import datetime
import logging
import logging.handlers
import os


class SettingUpLogger(object):
    def __init__(self):
        self.logger = None
        self.initialize_logger()

    def initialize_logger(self):
        log_dir = os.path.join("./logs")
        # 로그 디렉터리 생성
        if os.path.isdir(log_dir) is False:
            os.makedirs(log_dir)

        # 디버그 여부 확인
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        now_dt = datetime.datetime.now()
        now_dt = now_dt.strftime("%Y%m%d_%H%M%S")
        log_file_path = os.path.join(log_dir, (now_dt + ".logs"))
        log_file_max_bytes = 2 * 1024 * 1024  # 2MB

        # 콘솔과 파일 둘 다 출력 되도록 핸들러 설정
        file_handler = logging.handlers.RotatingFileHandler(filename=log_file_path, maxBytes=log_file_max_bytes,
                                                            backupCount=100,
                                                            encoding="utf-8")  # 2MB 로그파일 100개 쌓이면 후순위 로그 삭제

        # 로그 포매터
        formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

        self.logger.info(f"Complete: Logger Settings [{log_dir}]")

    def info(self, msg):
        self.logger.info(msg)
