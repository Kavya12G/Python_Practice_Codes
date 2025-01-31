def frequencySort(self, s: str) -> str:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        sorted_str = []

        for char, count in sorted_chars:
            sorted_str.append(char * count)

        return ''.join(sorted_str)