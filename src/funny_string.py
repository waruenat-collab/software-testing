def funny_string(s: str) -> str:
    diffs = []
    for i in range(len(s) - 1):
        diffs.append(abs(ord(s[i]) - ord(s[i + 1])))

    rs = s[::-1]
    rdiffs = []
    for i in range(len(rs) - 1):
        rdiffs.append(abs(ord(rs[i]) - ord(rs[i + 1])))

    if diffs == rdiffs:
        return "Funny"
    return "Not Funny"