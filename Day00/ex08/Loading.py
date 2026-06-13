import os as os


def ft_tqdm(lst: range) -> None:
    """
    ft_tqdm(lst: range) --> None

    Prints a progress bar for the defined lst range similar to the one
    of tqdm function but without elapsed time, estimated remaining time
    and speed in iteractions per second.
    """
    total = len(lst)
    terminal_width = os.get_terminal_size().columns
    left = len(f"100%|| {total}/{total} [00:01<00:00, 191.61it/s]")
    bar_len = terminal_width - left - 1

    if bar_len < 1:
        bar_len = 1

    for i, item in enumerate(lst, 1):
        percent = int(i / total * 100)
        filled_part = int((i / total) * bar_len)
        bar = "█" * (filled_part) + " " * (bar_len - filled_part)
        total_line = f"\r{percent}%|{bar}| {i}/{total}"
        os.write(1, total_line.encode())
        yield item

    os.write(1, b"\n")
    return None
