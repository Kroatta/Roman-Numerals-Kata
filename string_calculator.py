import re

def add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiters = [",", "\n"]

    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        custom_delimiter = parts[0][2:]
        if custom_delimiter.startswith("[") and custom_delimiter.endswith("]"):
            matches = re.findall(r"\[(.*?)\]", custom_delimiter)
            delimiters.extend(re.escape(m) for m in matches)
        else:
            delimiters.append(re.escape(custom_delimiter))
        numbers = parts[1]

    regex_pattern = "|".join(delimiters)
    parts = re.split(regex_pattern, numbers)
    nums = [int(n) for n in parts if n]
    negatives = [n for n in nums if n < 0]

    if negatives:
        raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")

    return sum(n for n in nums if n <= 1000)
