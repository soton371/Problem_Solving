def reverse_words(str):
  words = str.split()
  reversed_words = words[::-1]
  return ' '.join(reversed_words)

# Example usage
input_str = 'geeks quiz practice code'
reversed_str = reverse_words(input_str)

print(reversed_str)  # Output: code practice quiz geeks
