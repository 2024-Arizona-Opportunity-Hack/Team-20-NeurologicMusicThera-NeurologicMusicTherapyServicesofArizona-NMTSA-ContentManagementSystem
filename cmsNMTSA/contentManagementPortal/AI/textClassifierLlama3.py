import torch
from transformers import pipeline
from huggingface_hub import login
import json
from contentManagement.models import Category

login(token="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")

category_objs = Category.objects.all()
categories = [x.name for x in category_objs]

categories = ", ".join(categories)

# Check if CUDA is available and set the device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_id = "meta-llama/Meta-Llama-3-8B"

pipe = pipeline("text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto")

def classify_text(text):
    prompt = f"Classify the text provided into one of the following categories : {categories} based on the content in it for the disability it used to treat. Also, return relevant metadata tags for the document, according to its contents, that will make it easy to find this document in a large data base. Return the data as a JSON object with the following entries: 'category' and 'tags'."
    outputs = pipe(prompt, max_new_tokens=20, do_sample=True, temperature=0.1)
    return json.loads(outputs[0]["generated_text"].strip())





