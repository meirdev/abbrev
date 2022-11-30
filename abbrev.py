import re
import typing
from collections import Counter


def abbrev(*words: str, pattern: typing.Pattern | None = None) -> dict[str, str]:
    seen: typing.Counter[str] = Counter()
    abbrs: dict[str, str] = {}

    for word in words:
        for i in range(len(word)):
            abbr = word[: i + 1]

            if pattern is None or re.match(pattern, abbr):
                seen[abbr] += 1

                match seen[abbr]:
                    case 1:
                        abbrs[abbr] = word
                    case 2:
                        del abbrs[abbr]

    return abbrs
