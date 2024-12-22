from data_mock import data_mock
from ns_dump_data import region_dump_data
from trigger_find import trigger_find

if __name__ == '__main__':
    data = data_mock(10000, 20, 5)
    result = trigger_find(*data)
    print(result)

    data = region_dump_data({"the black hawks", "the north pacific", "the south pacific", "the east pacific", "notas region"}, 5)
    result = trigger_find(*data)
    print(result)
