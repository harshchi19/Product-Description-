import streamlit as st

try:
    from transformers import GPT2LMHeadModel, GPT2Tokenizer
except ImportError as e:
    st.error(f"Error: {e}. Please ensure that the transformers library is installed. You can try installing it with 'pip install transformers==4.11.3'.")
    import sys
    sys.exit(1)

import torch
from PIL import Image as PILImage

class TextGenerator:
    def __init__(self, model_name="gpt2"):
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        self.model.eval()

    def generate_text(self, prompt, max_length=50):
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        output_ids = self.model.generate(input_ids, max_length=max_length, num_beams=5, no_repeat_ngram_size=2)
        generated_text = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)
        return generated_text

class ImageClassifier:
    def __init__(self):
        # Use a pre-trained MobileNetV2 model for image classification
        self.model = torch.hub.load('pytorch/vision:v0.10.0', 'mobilenet_v2', pretrained=True)

    def classify_image(self, uploaded_image):
        # Open the uploaded image with PIL
        image = PILImage.open(uploaded_image)

        # Resize the image to the required dimensions (224, 224)
        image = image.resize((224, 224))

        # Convert the image to a NumPy array
        img_tensor = torch.tensor(np.array(image))

        # Perform normalization
        img_tensor = img_tensor.permute(2, 0, 1).unsqueeze(0).float() / 255.0

        # Classify the image
        with torch.no_grad():
            outputs = self.model(img_tensor)

        _, preds = torch.max(outputs, 1)
        class_label = preds.item()
        return class_label

    def process_input(self, uploaded_image, writing_style, length, paragraphs):
        # Image classification
        predicted_class = self.classify_image(uploaded_image)

        # Text generation
        text_generator = TextGenerator()
        words_per_paragraph = length // paragraphs
        generated_description = ""

        for _ in range(paragraphs):
            prompt = f"An image of class {predicted_class}. This image features class {predicted_class} with a {writing_style} writing style. "
            prompt += f"The {writing_style} description is {words_per_paragraph} words long, and contains {paragraphs} paragraphs."
            generated_paragraph = text_generator.generate_text(prompt, max_length=words_per_paragraph)
            generated_description += generated_paragraph + "\n\n"

        return generated_description.strip()

def main():
    st.title("Image and Text Processing App")

    # Upload image
    uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    # Image classifier
    if uploaded_image is not None:
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
        image_classifier = ImageClassifier()
        class_label = image_classifier.classify_image(uploaded_image)
        st.write(f"Predicted class: {class_label}")

        # Text generation
        writing_style = st.selectbox("Select writing style", ["formal", "informal"])
        length = st.slider("Select text length", min_value=100, max_value=1000, value=50, step=10)
        paragraphs = st.slider("Select number of paragraphs", min_value=1, max_value=5, value=3, step=1)

        if st.button("Generate Description"):
            generated_description = image_classifier.process_input(uploaded_image, writing_style, length, paragraphs)
            st.subheader("Generated Description:")
            st.write(generated_description)

if __name__ == "__main__":
    main()
