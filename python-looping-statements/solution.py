
def countdown_with_skip(start: int) -> list:
    """
    Count down from start to 1, skipping 3.
    """
    countdown = start
    result = []

    while countdown >= 1:
        if countdown == 3:
            countdown -= 1
            continue

        result.append(countdown)
        countdown -= 1

    return result


def find_first_negative(numbers: list) -> int | None:
    """
    Find the first negative number using a while loop.
    Return None if no negative number exists.
    """
    index = 0

    while index < len(numbers):
        if numbers[index] < 0:
            result = numbers[index]
            break

        index += 1
    else:
        return None

    return result


def sum_with_index(numbers: list) -> dict:
    """
    Map each index to the running sum.
    """
    result = {}
    running_sum = 0

    for index, number in enumerate(numbers):
        running_sum += number
        result[index] = running_sum

    return result


def manual_iteration_trace(items: list) -> list:
    """
    Retrieve elements using iter() and next().
    """
    iterator = iter(items)
    result = []

    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break

        result.append(item)

    return result
