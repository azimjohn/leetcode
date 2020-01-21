class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(int, version1.split(".")))
        version2 = list(map(int, version2.split(".")))
        version1_size = len(version1)
        version2_size = len(version2)

        maxlen = max([version1_size, version2_size])
        if version1_size < maxlen:
            version1.extend([0]*(maxlen-version1_size))

        if version2_size < maxlen:
            version2.extend([0]*(maxlen-version2_size))

        if tuple(version1) == tuple(version2):
            return 0
        elif tuple(version1) > tuple(version2):
            return 1
        else:
            return -1
