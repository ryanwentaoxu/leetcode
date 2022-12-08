class Solution:
    def convert(self, s: str, numRows: int) -> str:
        visited = {i:0 for i in range(len(s))}
        if numRows == 1:
            return s
        if numRows >= len(s):
            return s
        gap = 2 * (numRows - 2) + 2
        global_index = 0
        for i in range(numRows):
            visited[i] = global_index
            global_index += 1
            local_gap = gap - 2 * i
            index = 0
            if local_gap == gap or local_gap == 0:
                index = i + gap
                while index < len(s):
                    visited[index] = global_index
                    global_index += 1
                    index += gap
            else:
                sign = 0
                index = i + local_gap
                while index < len(s):
                    visited[index] = global_index
                    global_index += 1
                    if sign % 2 == 0:
                        index += 2 * i
                    else:
                        index += local_gap
                    sign += 1
        visited = {k: v for k, v in sorted(visited.items(), key=lambda item: item[1])}
        ans = ""
        for k, v in visited.items():
            ans += s[k]
        return ans
