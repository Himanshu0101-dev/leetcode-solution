class Solution:
    def minimumPushes(self, word: str) -> int:
        from collections import Counter
        freq = Counter(word)
        counts = sorted(freq.values(), reverse=True)

        total = 0
        for i, c in enumerate(counts):
            # Each "slot" has cost = (i // 8) + 1
            cost = (i // 8) + 1
            total += c * cost
        return total

