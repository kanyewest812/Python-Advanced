import string

def analyze_text_file(input_file, output_file):
    line_count = 0
    word_count = 0
    word_freq = {}

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line_count += 1
            
            line_clean = line.lower().translate(str.maketrans('', '', string.punctuation))
            words = line_clean.split()
            word_count += len(words)

            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Total number of lines: {line_count}\n")
        f.write(f"Total number of words: {word_count}\n\n")
        f.write("Word frequency:\n")

        for word in sorted(word_freq):
            f.write(f"{word}: {word_freq[word]}\n")

analyze_text_file("C:/python/week5/text.txt", "analysis.txt")
print("Analysis complete. Results saved to analysis.txt")
