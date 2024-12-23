# Loading CLIP
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

#Prepare Images and Categories
# Load and prepare the image
image = Image.open("/content/dog.webp")

# Define your categories (labels for classification)
categories = ["cat", "dog", "fish", "fox", "wolf", "shark"]

from google.colab import drive
drive.mount('/content/drive')

inputs = processor(text=categories, images=image, return_tensors="pt", padding=True)

with torch.no_grad():
    outputs = model(**inputs)

# Get the logits (similarity scores) between the image and text
logits_per_image = outputs.logits_per_image
probs = logits_per_image.softmax(dim=1)  # Convert logits to probabilities

# Get the category with the highest probability
predicted_label = categories[probs.argmax().item()]
print(f"Predicted label: {predicted_label}")

# Get the top N predicted categories for search tagging
top_n = 3  # Choose how many labels to assign
top_n_indices = probs.topk(top_n).indices.squeeze(0).tolist()
predicted_labels = [categories[i] for i in top_n_indices]
print(f"Top {top_n} labels: {predicted_labels}")
