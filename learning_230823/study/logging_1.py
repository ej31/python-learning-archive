import logging

from learning_230822.jeff_log_preset import SettingUpLogger

logging.basicConfig(filename="logging.log", level=logging.DEBUG,
                    format="[%(levelno)s] [%(filename)s] [%(funcName)s] [%(lineno)d]: %(message)s")


def some_function():
    logging.info("함수가 호출 되었습니다.")


if __name__ == '__main__':
    SettingUpLogger()
