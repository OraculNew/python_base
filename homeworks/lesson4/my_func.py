def my_range(begin, end, step=1):
    """Возвращает объект, который производит последовательность целых чисел от начала до конца, с заданным шагом.
    :param begin: начало последовательности Int
    :param end: конец последовательности Int
    :param step: шаг с которым производится последовательность Int. По умолчанию 1
    :return: последовательность целых чисел
    """
    while begin < end:
        yield begin
        begin += step


def my_reduce(func, list_obj):
    while len(list_obj) > 1:
        list_obj = [func(list_obj[0], list_obj[1])] + list_obj[2:]
    return list_obj
