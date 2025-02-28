from singleton_decorator import singleton


@singleton
class SingletonLogger:
    def log(self, message):
        print(f"[LOG]: {message}")
