from loguru import logger




def square(x):
    try:
        return x**2
    except TypeError as e:
        logger.error(f'{x} is not a number')
        raise e

if __name__ == "__main__":
    print(square(2))
    try:
        print(square(k))
    except TypeError as e:
        print(e)
    #except NameError:
