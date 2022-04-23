def showArgs(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(func.__name__, "args", *args, kwargs if len(kwargs) > 0 else "",
              "returns", res)

        return res

    return wrapper
