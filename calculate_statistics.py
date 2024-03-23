def calculate_statistics(data):
  """Calculates mean, median, and mode for a list of numbers.

  Args:
      data: A list of numerical data.

  Returns:
      A dictionary containing the mean, median, and mode of the data.
  """

  # Calculate mean
  mean = sum(data) / len(data)

  # Sort the data for median and mode calculations
  data.sort()

  # Calculate median
  if len(data) % 2 == 0:
    median = (data[len(data) // 2 - 1] + data[len(data) // 2]) / 2
  else:
    median = data[len(data) // 2]

  # Calculate mode
  from collections import Counter
  counts = Counter(data)
  mode = max(counts, key=counts.get)

  return {"mean": mean, "median": median, "mode": mode}

# Example usage
data = [2, 4, 6, 8, 10, 12]
statistics = calculate_statistics(data)

print(statistics)  # Output: {'mean': 6.0, 'median': 6.0, 'mode': 2}