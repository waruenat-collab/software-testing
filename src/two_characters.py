def two_characters(s: str) -> int:
    unique = set(s)
    max_len = 0

    for c1 in unique:
        for c2 in unique:
            if c1 == c2:
                continue

            filtered = [c for c in s if c == c1 or c == c2]

            valid = True
            for i in range(1, len(filtered)):
                if filtered[i] == filtered[i - 1]:
                    valid = False
                    break

            if valid:
                max_len = max(max_len, len(filtered))

    return max_len