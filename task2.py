import types

def flat_generator(list_of_lists):
    for sublist in list_of_lists:
        for element in sublist:
            yield element

def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    expected_result = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    actual_result = []

    for item in flat_generator(list_of_lists_1):
        actual_result.append(item)

    assert actual_result == expected_result

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

if __name__ == '__main__':
    test_2()