import torch
from transformers import pipeline
from huggingface_hub import login
import json

login(token="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")

categories = "cat1, cat2, cat3, cat4, cat5"

# Check if CUDA is available and set the device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_id = "meta-llama/Meta-Llama-3-8B"

pipe = pipeline("text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto")

def classify_text(text):
    prompt = f"Classify the text provided into one of the following categories : {categories} based on the content in it. Also, return six metadata tags for the document that will make it easy to find this document in a large data base. Return the data as a JSON object with the following entries: 'category' and 'tags'."
    outputs = pipe(prompt, max_new_tokens=20, do_sample=True, temperature=0.1)
    return json.loads(outputs[0]["generated_text"].strip())





