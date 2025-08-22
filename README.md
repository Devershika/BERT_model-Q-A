# BERT_model-Q-A

## Question Answering with DistilBERT on SQuAD
This project fine-tunes a DistilBERT model for extractive Question Answering (QA) using the SQuAD dataset. The model learns to extract answer spans from a given context when provided with a question.

## Workflow

1. Load Dataset

  * Uses a subset of the SQuAD dataset
   (first 5,000 examples).
  
  * Split into train and test sets.

2. Preprocessing

  * Tokenize the dataset using distilbert-base-uncased.
  
  * Align character-level answer spans with token positions.

3. Model Setup

  * AutoModelForQuestionAnswering is initialized from Hugging Face.

  * A Trainer object is used for training with default data collator.

4. Training

  * Fine-tunes DistilBERT for 3 epochs with:
  
  * Learning rate: 2e-5
  
  * Batch size: 16
  
  * Weight decay: 0.01

5. Saving Model

  * Trained model and tokenizer are saved in qa_model/.

6. Inference
   
  * Load model with Hugging Face pipeline("question-answering").

  * Provide a question and context to get an extracted answer.
Load model with Hugging Face pipeline("question-answering").

Provide a question and context to get an extracted answer.
