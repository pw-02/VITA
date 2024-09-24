from transformers import AutoTokenizer, AutoModel

# Load the tokenizer and model
model_name = "OpenGVLab/InternViT-300M-448px"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)
