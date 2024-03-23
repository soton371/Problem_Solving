from collections import Counter
data = [2, 4, 6, 8, 10, 12]

mean = sum(data) / len(data)

data.sort()

if len(data) % 2 == 0:
    median = (data[len(data) // 2 - 1] + data[len(data) // 2]) / 2
else:
    median = data[len(data) // 2]


counts = Counter(data)
mode = max(counts, key=counts.get)

print({"mean": mean, "median": median, "mode": mode})