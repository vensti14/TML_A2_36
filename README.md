# TML Assignment 2 - Model Stealing Attack

## Team 36

- **Prasad Pankaj Patil** (Student ID: 7076145) – prpa00003@stud.uni-saarland.de
- **Ananya Bhardwaz** (Student ID: 7076153) – anbh00002@stud.uni-saarland.de

---

## Project Description

This repository contains the implementation for **Assignment 2** of the *Trustworthy Machine Learning* course. The task involves performing a **Model Stealing Attack** against a victim encoder that is protected using the **Bucks for Buckets (B4B)** defense mechanism.  
The objective is to reconstruct the victim encoder’s functionality using only API access that returns obfuscated feature representations.

---

## Problem Setting

- The victim encoder is accessible only via API calls.
- The API applies random transformations (Affine, Pad + Shuffle, Binary, or combinations) to the representations before returning them.
- The attacker has no access to the victim’s internal parameters or weights.
- The goal is to train a stolen encoder that produces feature embeddings as close as possible to those of the victim.

---

## Key Files and Descriptions

| File                          | Description                                                                                                                    |
--------------------------------|---------------------------------------------------------------------------------------------------------------------------------
| `stealing.py`                 | Main pipeline for the model stealing attack. Handles querying, aggregation of representations, and initial dataset generation. |
| `defense.py`                  | Simulates the B4B defense mechanism for testing the robustness of the stolen model.                                            |
| `augment.py`                  | Contains various data augmentation functions used during both querying and training.                                           |
| `train_encoder.py`            | Script for training the stolen encoder using the collected (stolen) representations.                                           |
| `utils.py`                    | Helper functions for data processing, saving, logging, and visualization.                                                      |
| `submission_encoder.onnx`     | The stolen encoder model saved in ONNX format ready for evaluation.                                                            |
| `submission.csv`              | The outputs from the stolen encoder for the evaluation set.                                                                    |
| `requirements.txt`            | Lists all Python dependencies required to run the project.                                                                     |

---

## How to Run

1. **Install Dependencies:**
<pre lang="markdown"> ``` pip install -r requirements.txt ``` </pre>

2. **Run the Model Stealing Attack:**
<pre lang="markdown"> ``` python stealing.py ``` </pre>
This queries the victim API and stores the noisy representations.

3. **Train the Stolen Encoder:**
<pre lang="markdown"> ``` python train_encoder.py ``` </pre>

4. **The trained encoder is saved as:**
<pre lang="markdown"> ``` submission_encoder.onnx. ``` </pre>

---

## Output Files

**submission_encoder.onnx:** Stolen encoder model in ONNX format.
**submission.csv:** Prediction results for the private evaluation set.

---

## Project Structure

.
├── augment.py
├── defense.py
├── requirements.txt
├── stealing.py
├── train_encoder.py
├── utils.py
├── submission_encoder.onnx
└── submission.csv

---

## Contact

For any queries or support, contact:
**prpa00003@stud.uni-saarland.de**
**anbh00002@stud.uni-saarland.de**
