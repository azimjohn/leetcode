class Solution:
    def lengthLongestPath(self, input: str) -> int:
        levels = {}
        max_path_len = 0
        entries = input.split("\n")

        for entry in entries:
            tabs = entry.count("\t")
            current_path_len = len(entry) - tabs

            if tabs > 0:
                current_path_len += levels[tabs-1] + 1

            if "." in entry:
                max_path_len = max(max_path_len, current_path_len)
            else:
                levels[tabs] = current_path_len

        return max_path_len


if __name__ == "__main__":
    s = Solution()
    print(s.lengthLongestPath("""
dir
\tsubdir1
\t\tfile1.ext
\t\tsubsubdir1
\tsubdir2
\t\tsubsubdir2
\t\t\tfile2.ext
    """))
    print(len("dir/subdir2/subsubdir2/file2.ext"))
