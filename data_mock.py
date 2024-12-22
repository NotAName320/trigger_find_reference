import random
import string


def data_mock(n: int, num_targets: int, min_trig: int) -> tuple[list[str], dict[str, int], int, set[str]]:
    rand_list: list = random.choices(range(1, 10000), k=n)
    rand_list.sort()
    return_map = {}
    for i in rand_list:
        random_str = ''
        while not random_str or random_str in return_map:
            random_str = "Region " + ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        return_map[random_str] = i
    return list(return_map.keys()), return_map, min_trig, set(random.sample(list(return_map.keys()), num_targets))
