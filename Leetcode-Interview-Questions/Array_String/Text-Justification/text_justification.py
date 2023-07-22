def fullJustify(words, maxWidth):
    results = []
    line = []
    line_lenth = 0

    for word in words:

        # Check if adding the current word exceeds maxWidth
        if line_lenth + len(line) + len(word) > maxWidth:

            # Calculate the number of extra spaces and gaps
            total_spaces = maxWidth - line_length
            num_gaps = len(line) - 1 if len(line) > 1 else 1

            # If line contaiins only one word or it's the last line, left-justify
            if num_gaps == 0 or len(line) == 1:
                formatted_line = ' '.join(line) + ' ' * (maxWidth - line_lenth)
            else:

                # Distribute extra spaces evenly between words
                spaces_between_words = total_spaces // num_gaps
                extra_spaces = total_spaces % num_gaps

                # Build the line with distributed spaces
                formatted_line = line[0]
                for i in range(1, len(line)):
                    spaces = spaces_between_words + (1 if i <= extra_spaces else 0)
                    formatted_line += ' ' * spaces + line[i]

            results.append(formatted_line)
            line = []
            line_lenth = 0

        # Add the current word to the line
        line.append(word)
        line_lenth += len(word) + 1 # +1 to account for the space between words

    # Last line (left-justified)
    last_line = ' '.join(line)
    results.append(last_line + ' ' * (maxWidth - len(last_line)))

    return results
