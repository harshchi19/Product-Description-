# Product-Description App

Welcome to the Image and Text Processing App! This application allows you to upload an image, classify it using a pre-trained MobileNetV2 model, and generate descriptive text based on the image's class and user-selected parameters.

## Features

- **Image Classification**: Utilizes a pre-trained MobileNetV2 model to classify uploaded images.
- **Text Generation**: Generates descriptive text based on the image's class, using a GPT-2 model. Users can customize the writing style, length, and number of paragraphs.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/harshchi19/Product-Description-.git
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

   If you encounter an error with the transformers library, ensure you have the correct version:
   ```bash
   pip install transformers==4.11.3
   ```

4. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Upload Image**: Click on the "Upload Image" button to upload an image (JPG, JPEG, PNG formats supported).

2. **Image Classification**: The uploaded image will be classified, and the predicted class will be displayed.

3. **Text Generation**: Customize the text generation by selecting a writing style, text length, and number of paragraphs. Click the "Generate Description" button to create the descriptive text based on the image's class.


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- The `transformers` library by Hugging Face for the GPT-2 model.
- The `torch` library for PyTorch.
- The `Pillow` library for image processing.
- Streamlit for providing an easy-to-use framework for creating web applications.

