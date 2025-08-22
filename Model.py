!pip install transformers datasets evaluate -qq

from datasets import load_dataset
from transformers import AutoTokenizer, DefaultDataCollator
from transformers import AutoModelForQuestionAnswering, TrainingArguments, Trainer
from transformers import pipeline

#Load dataset
squad = load_dataset("squad", split="train[:5000]")

#Train test split
squad = squad.train_test_split(test_size=0.2)
squad["train"][0]
