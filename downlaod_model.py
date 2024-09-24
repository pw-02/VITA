from transformers import AutoTokenizer, AutoModel

# Load the tokenizer and model
model_name = "downloads/VITA_ckpt"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)
