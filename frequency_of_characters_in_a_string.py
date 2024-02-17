def character_frequency(text):
    text = text.lower()
    frequency_map = {}
    for char in text:
        if char in frequency_map:
            frequency_map[char] += 1
        else:
            frequency_map[char] = 1
    return frequency_map
