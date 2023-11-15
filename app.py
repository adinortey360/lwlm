class BasicLanguageModel:
    def __init__(self, context_window=2):
        # Dictionary to store word probabilities
        self.word_probabilities = {}
        # Set the context window size
        self.context_window = context_window

    def train(self, sentences):
        for sentence in sentences:
            words = sentence.split()
            for i in range(len(words) - 1):
                current_word = words[i]
                next_word = words[i + 1]

                # Use tuple to represent the sequence of words
                word_sequence = tuple(words[max(0, i - self.context_window + 1):i + 1])

                # Check if the current word sequence is already in the dictionary
                if word_sequence in self.word_probabilities:
                    # Check if the next word is already associated with the current word sequence
                    if next_word in self.word_probabilities[word_sequence]:
                        # Increment the count for the next word
                        self.word_probabilities[word_sequence][next_word] += 1
                    else:
                        # Initialize the count for the next word
                        self.word_probabilities[word_sequence][next_word] = 1
                else:
                    # Initialize the current word sequence in the dictionary
                    self.word_probabilities[word_sequence] = {next_word: 1}

    def predict_next_word(self, current_word_sequence):
        # Initialize the predictions dictionary
        predictions = {}

        # Try to find a match in the dictionary for the current word sequence
        for i in range(len(current_word_sequence), 0, -1):
            subsequence = tuple(current_word_sequence[-i:])
            if subsequence in self.word_probabilities:
                # Get the dictionary of next words and their counts
                next_words = self.word_probabilities[subsequence]

                # Calculate probabilities based on counts
                total_count = sum(next_words.values())
                probabilities = {word: count / total_count for word, count in next_words.items()}

                # Update the predictions dictionary
                predictions.update(probabilities)

        return predictions

# Example usage
training_data = [
    "I love programming",
    "Programming is fun",
    "I love Python",
    "Python is versatile",
    "Machine learning is fascinating",
    "Fascinating subjects include artificial intelligence",
    "Artificial intelligence is shaping the future",
    "The future of technology is unpredictable",
    "Unpredictable events often lead to innovation",
    "Innovation drives progress in society",
    "Society faces challenges that require creative solutions",
    "Creative thinking is crucial for problem-solving",
    "Problem-solving skills are essential in everyday life",
    "Life is full of surprises and opportunities",
    "Opportunities arise when one least expects them",
    "Expect the unexpected in your journey",
    "Journey towards success is filled with obstacles",
    "Obstacles can be overcome with determination and hard work",
    "Hard work is the key to achieving your goals",
    "Goals give purpose and direction to life",
    "Life without purpose can feel empty and unfulfilling",
    "Unfulfilling experiences teach valuable lessons",
    "Lessons learned shape our perspectives and actions",
    "Actions speak louder than words",
    "Words have the power to inspire and influence",
    "Influence can be positive or negative",
    "Negative experiences offer opportunities for growth",
    "Growth is a continuous process throughout life",
    "Life is a journey of self-discovery and personal development"
]

# Create and train the basic language model with a larger context window
basic_model = BasicLanguageModel(context_window=3)
basic_model.train(training_data)

# Predict the next word given a current word sequence
current_word_sequence = ("I", "love", "is", "a", "continuous", "process")
predictions = basic_model.predict_next_word(current_word_sequence)

# Display predictions
print(f"Next word predictions for '{current_word_sequence}': {predictions}")
