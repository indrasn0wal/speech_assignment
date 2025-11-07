# 🗣️ Forced Alignment using Montreal Forced Aligner (MFA)

## 📘 Objective
This project demonstrates a complete **Forced Alignment pipeline** using the **Montreal Forced Aligner (MFA)** tool.  
Forced alignment is the process of automatically matching an audio recording with its corresponding text transcription at the word and phoneme level.

---

## 📂 Dataset Preparation

### Step 1: Data Organization
Using the script **`data_preparation.py`**, the dataset was organized into the MFA-compatible format.

- Normalized transcript file extensions (`.TXT` → `.txt`)
- Placed all `.wav` and `.txt` pairs into a single directory:  
  ```
  mfa_corpus/
  ├── sample1.wav
  ├── sample1.txt
  ├── sample2.wav
  ├── sample2.txt
  ...
  ```

---

## ⚙️ Environment Setup

### Step 2: Install Miniconda & MFA
```bash
# Activate base environment
conda activate base

# Install mamba for faster installations
conda install -c conda-forge mamba

# Create new environment for MFA
mamba create -n aligner -c conda-forge montreal-forced-aligner

# Activate environment
conda activate aligner
```

---

## 🎧 Download Pretrained Models

```bash
# Download acoustic model
mfa model download acoustic english_us_arpa

# Download pronunciation dictionary
mfa model download dictionary english_us_arpa
```

---

## ✅ Step 3: Validation

Validate the corpus to identify missing or out-of-vocabulary (OOV) words:

```bash
mfa validate mfa_corpus english_us_arpa english_us_arpa
```

The validation output showed **OOV words**, which were stored in:
```
oov_words/oovs_found_english_us_arpa.txt
```

---

## 🧠 Step 4: Generating Pronunciations for OOV Words (Using G2P Model)

Download the pretrained G2P (Grapheme-to-Phoneme) model:

```bash
mfa model download g2p english_us_arpa
```
Train a g2p model on the english corpus:

```bash
mfa train_g2p /Users/indrasn0wal/Documents/MFA/pretrained_models/dictionary/english_us_arpa.dict my_trained_g2p
```
Now use the trained model to predict phoneme

```bash
mfa g2p oov_words/oovs_found_english_us_arpa.txt my_trained_g2p.zip oov_generated_trained.dict
```
---

## 📘 Step 5: Combine Dictionaries

Concatenate the original MFA dictionary with the newly generated OOV dictionary, and form a new dictionary with name combined.dict:

```bash
cat /Users/<your-username>/Documents/MFA/pretrained_models/dictionary/english_us_arpa.dict oov_generated_trained.dict > combined_trained.dict
```

---

## 🔍 Step 6: Re-Validate Corpus

Re-run validation using the combined dictionary to ensure there are **no OOV words** remaining:

```bash
mfa validate mfa_corpus combined_trained.dict english_us_arpa
```

✅ **Result:** No OOV words found.

---

## 🗣️ Step 7: Forced Alignment

Run the alignment process using the final combined dictionary:

```bash
mfa align mfa_corpus combined_trained.dict english_us_arpa aligned_output
```

---

## 📁 Step 8: Output Files

The output directory `/aligned_output` contains **TextGrid files** for each audio file:

```
aligned_output/
├── sample1.TextGrid
├── sample2.TextGrid
...
```

These can be visualized using **Praat** to inspect word and phoneme boundaries.

---

## 🧾 Files Included

| File | Description |
|------|--------------|
| `data_preparation.py` | Script to normalize and prepare corpus |
| `combined_trained.dict` | Final pronunciation dictionary |
| `aligned_output/` | Generated TextGrid alignment files |
| `oov_words/oovs_found_english_us_arpa.txt` | List of out-of-vocabulary words |
| `oov_generated_trained.dict` | Pronunciations generated using G2P |
| `README.md` | Setup and usage instructions |
| `report.pdf` | Summary of results and analysis |
