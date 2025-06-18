import Levenshtein
import editdistance  # You need to install: pip install editdistance
import os

def calculate_accuracy(ground_truth, ocr_output):
    # --- Character-level ---
    gt_chars = ground_truth.replace(" ", "")
    ocr_chars = ocr_output.replace(" ", "")

    cer = Levenshtein.distance(gt_chars, ocr_chars) / len(gt_chars) if len(gt_chars) > 0 else 0
    char_accuracy = (1 - cer) * 100

    # --- Word-level ---
    gt_words = ground_truth.split()
    ocr_words = ocr_output.split()

    wer = editdistance.eval(gt_words, ocr_words) / len(gt_words) if len(gt_words) > 0 else 0
    word_accuracy = (1 - wer) * 100

    return cer, char_accuracy, wer, word_accuracy

# --- Load files ---
base_dir = '/Users/chhornsotheavann/fine_tuned/CER Calculate'

with open(f'{base_dir}/Ground_Truth.txt', 'r', encoding='utf-8') as f:
    ground_truth_text = f.read().strip()

with open(f'{base_dir}/Fine_Tuned.txt', 'r', encoding='utf-8') as f:
    ocr_output_text = f.read().strip()

# Ground_Truth
# Fine_Tuned
# default_tesseract
# max_iterations10k

# --- Calculate ---
cer, char_acc, wer, word_acc = calculate_accuracy(ground_truth_text, ocr_output_text)

# --- Print results ---
print(f"Character Error Rate (CER): {cer:.2%}")
print(f"Character Accuracy: {char_acc:.2f}%")
print(f"Word Error Rate (WER): {wer:.2%}")
print(f"Word Accuracy: {word_acc:.2f}%")
