from transformers import AutoTokenizer, AutoModel

model_name = "downloads\VITA_ckpt"

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

# Load the model
model = AutoModel.from_pretrained(model_name)
pass