from transformers import AutoTokenizer, AutoModel

model_name = "downloads/InternViT-300M-448px"
model_name = "downloads/audio-encoder-2wh_zh_en_audioset_Mixtral-8x7B_New-base-tunning"

# Load the tokenizer
# tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

# Load the model
model = AutoModel.from_pretrained(model_name)
pass