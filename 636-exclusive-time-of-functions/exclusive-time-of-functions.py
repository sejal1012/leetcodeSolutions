class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        times = [0] * n
        stack = []
        previous_time = 0
        for log in logs:
            function_id, typ, timestamp = log.split(':')
            function_id = int(function_id)
            timestamp = int(timestamp)
            if typ == "start":
                if stack:
                    times[stack[-1]] += timestamp - previous_time
                stack.append(function_id)
                previous_time = timestamp
            else:
                times[stack.pop()] += timestamp - previous_time + 1
                previous_time = timestamp + 1
        return times
