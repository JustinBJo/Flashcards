# Flashcard Learning Application

A command-line flashcard memorization application for learning word lists and testing your knowledge.

## Features

- 📚 **Multiple Word Lists**: Load any JSON-based word list
- 🎓 **Learn Mode**: Practice with immediate feedback
- 📝 **Test Mode**: Scored assessments with detailed results
- 🔀 **Random Selection**: Words and questions presented randomly
- 📊 **Performance Tracking**: View scores, percentages, and missed words

## Installation

1. Ensure you have Python 3.6+ installed
2. Clone or download this repository
3. No additional dependencies required (uses only Python standard library)

## Project Structure

```
flashcards/
├── wordlists/           # JSON word list files
│   ├── spanish.json
│   ├── programming.json
│   └── vocabulary.json
├── src/
│   ├── main.py                 # Main application entry point
│   ├── wordlist_manager.py     # Manages word list loading
│   ├── learn_mode.py           # Learn mode implementation
│   └── test_mode.py            # Test mode implementation
└── README.md
```

## Usage

### Running the Application

```bash
cd e:\repos\Flashcards
python src/main.py
```

### Creating Word Lists

Create JSON files in the `wordlists/` directory with the following format:

```json
{
  "word1": "meaning1",
  "word2": "meaning2",
  "word3": "meaning3"
}
```

**Example** (`wordlists/french.json`):
```json
{
  "hello": "bonjour",
  "goodbye": "au revoir",
  "please": "s'il vous plaît",
  "thank you": "merci"
}
```

### Learn Mode

In Learn Mode, you can practice in three ways:

1. **Word → Meaning**: Given a word, provide its meaning
2. **Meaning → Word**: Given a meaning, provide the word
3. **Random**: Alternates randomly between both directions

- Get immediate feedback on each answer
- Type `quit` at any time to return to the menu
- Practice as long as you want without scoring

### Test Mode

In Test Mode, you receive a scored assessment:

1. Choose number of questions (1-100, limited by wordlist size)
2. Answer randomly selected questions (no duplicates)
3. Questions randomly show either word or meaning
4. Receive final score with:
   - Total correct/total questions
   - Percentage score
   - List of incorrect answers with correct solutions

## Examples

### Starting the Application
```
==================================================
     FLASHCARD LEARNING APPLICATION
==================================================

Available Word Lists:
--------------------------------------------------
  1. spanish
  2. programming
  3. vocabulary
--------------------------------------------------

Enter wordlist name (or 'quit' to exit): spanish

✓ Loaded 'spanish' with 40 word pairs.
```

### Learn Mode Session
```
==================================================
           LEARN MODE OPTIONS
==================================================
  1. Word → Meaning (given word, provide meaning)
  2. Meaning → Word (given meaning, provide word)
  3. Random (alternates randomly)
  4. Back to main menu
==================================================

Your choice: 1

Word: hello
Your answer: hola
✓ Correct!
```

### Test Mode Results
```
==================================================
              TEST RESULTS
==================================================

Score: 8/10
Percentage: 80.0%

==================================================
  INCORRECT ANSWERS (2)
==================================================

Question 3:
  Asked: Word - yesterday
  Your answer: manana
  Correct answer: ayer
  [Word: 'yesterday' = Meaning: 'ayer']

Question 7:
  Asked: Meaning - hermano
  Your answer: brother
  Correct answer: brother
  [Word: 'brother' = Meaning: 'hermano']

==================================================
```

## Tips

- Answers are case-insensitive
- Leading and trailing spaces are ignored
- Start with Learn Mode to familiarize yourself with the words
- Use Test Mode to assess your progress
- Create custom word lists for any subject you're studying

## Customization

You can easily extend this application by:

- Adding more word lists in the `wordlists/` directory
- Modifying the maximum test questions (default: 100)
- Adding fuzzy matching for typo tolerance
- Implementing spaced repetition algorithms
- Adding progress tracking across sessions

## License

This is a free and open-source project. Feel free to modify and distribute as needed.

## Support

For issues or questions, please refer to the source code documentation or create an issue in the repository.

---

Happy Learning! 📚✨
