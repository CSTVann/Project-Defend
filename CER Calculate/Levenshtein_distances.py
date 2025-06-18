import matplotlib.pyplot as plt
import Levenshtein
import numpy as np

# Load ground truth and OCR result
with open("/Users/chhornsotheavann/fine_tuned/CER Calculate/Ground_Truth.txt", "r", encoding="utf-8") as f:
    ground_truth = [line.strip() for line in f]

with open("/Users/chhornsotheavann/fine_tuned/CER Calculate/default_tesseract.txt", "r", encoding="utf-8") as f:
    ocr_output = [line.strip() for line in f]

# Compute Levenshtein distances
distances = [
    Levenshtein.distance(gt, pred)
    for gt, pred in zip(ground_truth, ocr_output)
]

# Plot histogram
plt.figure(figsize=(10, 5))
plt.hist(distances, bins=range(0, max(distances)+2), edgecolor="black", log=True)
plt.xlabel("Levenshtein distance")
plt.ylabel("Count")
plt.title("Histogram of Levenshtein Distances")
plt.grid(True, axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
