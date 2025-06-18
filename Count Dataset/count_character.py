# Define the categories for Khmer script elements
khmer_consonants = ['ក', 'ខ', 'គ', 'ឃ', 'ង', 'ច', 'ឆ', 'ជ', 'ឈ', 'ញ', 'ដ', 'ឋ', 'ឌ', 'ឍ', 'ណ', 'ត', 'ថ', 'ទ', 'ធ', 'ន', 'ប', 'ផ', 'ព', 'ភ', 'ម', 'យ', 'រ', 'ល', 'វ', 'ស', 'ហ', 'ឡ', 'អ']
khmer_vowels = ['ា', 'ិ', 'ី', 'ឹ', 'ឺ', 'ុ', 'ូ', 'ួ', 'ើ', 'ឿ', 'ៀ', 'េ', 'ែ', 'ៃ', 'ោ', 'ៅ', 'ំ', 'ះ', 'ៈ']
independent_vowels = ['ឥ', 'ឦ', 'ឧ', 'ឩ', 'ឲ', 'ឱ', 'ឪ', 'ឫ', 'ឬ', 'ឭ', 'ឮ', 'ឯ', 'ឰ']
khmer_numbers = ['០', '១', '២', '៣', '៤', '៥', '៦', '៧', '៨', '៩']
khmer_subscript = ['្']
khmer_diacritics = ['់', '៉', '៍', '័', '៏', '៎', '៌']
khmer_symbols = ['(', ')', ',', '.', '៕', '។', 'ៗ', '។ល។', '?', ' ', '%', '៛']

# Function to count each category in Khmer text
def count_khmer_elements(text):
    vowels_count = 0
    consonants_count = 0
    numbers_count = 0
    subscript_count = 0
    diacritics_count = 0
    independent_count = 0
    symbols_count = 0

    for char in text:
        if char in khmer_vowels:
            vowels_count += 1
        elif char in khmer_consonants:
            consonants_count += 1
        elif char in khmer_numbers:
            numbers_count += 1
        elif char in khmer_subscript:
            subscript_count += 1
        elif char in khmer_diacritics:
            diacritics_count += 1
        elif char in independent_vowels:
            independent_count += 1
        elif char in khmer_symbols:
            symbols_count += 1

    return vowels_count, consonants_count, numbers_count, subscript_count, diacritics_count, independent_count, symbols_count

# Read text from file
file_path = "/Users/chhornsotheavann/fine_tuned/Count Dataset/Dataset.txt"
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Call the function
vowels, consonants, numbers, subscript, diacritics, independent, symbols = count_khmer_elements(text)
total_char = (vowels + consonants + numbers + subscript + independent + diacritics + symbols)
# Print the results
print("Ammount of Dataset for Testing:")
print(f"{'Consonants-------------'} {consonants}")
print(f"{'Vowels-----------------'} {vowels}")
print(f"{'Numbers----------------'} {numbers}")
print(f"{'Diacritics-------------'} {diacritics}")
print(f"{'Independent------------'} {independent}")
print(f"{'Symbols----------------'} {symbols}")
print(f"{'Subscript--------------'} {subscript}")
print('')
print(f"{'Total Character--------'} {total_char}")
