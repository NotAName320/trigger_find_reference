from collections import deque


def trigger_find(dump: list[str], update_times: dict[str, int], min_interval: int, targets: set[str]):
    queue: deque[str] = deque()
    return_list: list[tuple[str, str, int]] = []
    latest: str = ""
    for d in dump:
        if len(queue) == 0 or update_times[queue[0]] != update_times[d]:
            queue.appendleft(d)
        while len(queue) != 0 and update_times[queue[-1]] + min_interval <= update_times[d]:
            latest = queue.pop()
        if d in targets:
            return_list.append((d, latest, update_times[d]-update_times[latest]))
    return return_list