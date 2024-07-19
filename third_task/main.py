"""Main Script"""


import sys
from pathlib import Path
from collections import Counter


def parse_log_line(line: str) -> dict:
    """
    Parses the log string and returns information
    about log in format of dictionary

    Args:
    line (str): the string with info about log.

    Returns:
    dict: Information about log (date, time, 
    level, description)
    """
    log_date, log_time, log_level, *log_description = line.split()
    log_dict = {
        "date": log_date,
        "time": log_time,
        "level": log_level,
        "description": " ".join(log_description)
    }
    return log_dict


def load_logs(file_path: Path) -> list[dict]:
    """
    Loads logs from file.
    
    Args:
    file_path (Path): The path to log file.

    Returns:
    list[dict]: List of logs from log file.
    """
    log_list = []

    with open(file_path, "r", encoding="utf-8") as log_file:
        log_lines = log_file.readlines()

    for log_line in log_lines:
        log_list.append(parse_log_line(log_line))

    return log_list


def filter_logs_by_level(logs: list, level: str) -> list[dict]:
    """
    Filters the logs depending on its levels.
    
    Args:
    logs (list): The list of logs.
    level (str): The log level.

    Returns:
    list[dict]: all logs matching the given level. 
    """

    filtered_log_list = list(filter(lambda x: x["level"].lower() == level, logs))

    return filtered_log_list


def count_logs_by_level(logs: list) -> dict[int]:
    """
    Counts the logs by its levels.

    Args:
    logs (list): The list of logs

    Returns:
    dict[int]: the number of logs depending on its levels.
    """

    log_levels = [log['level'] for log in logs]
    count_levels = Counter(log_levels)
    sorted_list = sorted(count_levels.items(),
                         key=lambda x: x[1],
                         reverse=True)

    return dict(sorted_list)


def display_log_counts(counts: dict):
    """
    Displays results in readable format.

    Args:
    counts (dict): Log counts.
    """
    # Creates the header of table
    left_header = "Log level"
    right_header = "Counts"

    # Defines the maximum width of left column
    max_len_left = len(max(counts.keys(), key=len))
    if max_len_left > len(left_header):
        max_len_left_col = max_len_left
    else:
        max_len_left_col = len(left_header)

    # Defines the maximum width of right column
    max_len_right = len(max([str(val) for val in counts.values()], key=len))
    if max_len_right > len(right_header):
        max_len_right_col = max_len_right
    else:
        max_len_right_col = len(right_header)

    # Displays the table
    print(f"{left_header : <{max_len_left_col}} | {right_header : <{max_len_right_col}}")
    print("-" * (max_len_left_col + 3 + max_len_right_col))
    for key, val in counts.items():
        print(f"{key : <{max_len_left_col}} | {val : <{max_len_right_col}}")


def main():

    """
    The main function
    """
    level = ""

    if len(sys.argv) < 2:
        print("Error: Please enter the path to the file.")
        sys.exit(1)

    elif len(sys.argv) == 2:
        file_path = Path(sys.argv[1])

    elif len(sys.argv) == 3:
        file_path = Path(sys.argv[1])
        level = sys.argv[2].lower()

    else:
        print("Error: Too many arguments entered.")
        print("Please enter the path to the file and log level")
        sys.exit(1)

    try:
        logs = load_logs(file_path)
        counted_logs = count_logs_by_level(logs)
        display_log_counts(counted_logs)

        if level:
            filtered_logs = filter_logs_by_level(logs, level)
            print(f"\nLog details for '{level.upper()}' level")
            for log in filtered_logs:
                date, time, _, description = log.values()
                print(f"{date} {time} - {description}")

    except FileNotFoundError:
        print("Error: The file not found")

    except ValueError:
        print("Error: The file is corrupted or doesn't have logs")


if __name__ == '__main__':
    main()
