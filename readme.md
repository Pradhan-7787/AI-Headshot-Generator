# AI Headshot Generator

![Header Image](header_image.png)

## Overview

This project is an AI-powered headshot generator that utilizes Convolutional Neural Networks (CNNs) to generate professional headshots from the CelebA dataset.

## Getting Started

### Prerequisites

- Python 3.11.5
- TensorFlow
- Other dependencies (specified in `requirements.txt`)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Pradhan-7787/AI-Headshot-Generator.git
    cd AI-Headshot-Generator
    ```

2. **Download the CelebA dataset:**
    - Download the CelebA dataset from [this Google Drive link](https://drive.google.com/drive/folders/0B7EVK8r0v71pQ3NzdzRhVUhSams?resourcekey=0-Kpdd6Vctf-AdJYfS55VULA&usp=sharing).
    - Extract the ZIP file.
    - Place the contents of the extracted ZIP file into the `data/celeba/lfw/` directory in the root of the project.

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. **Run the training script:**

    ```bash
    python src/train.py
    ```

2. **Trained models:**
   - Models will be saved in the `saved_models/` directory.

## Contributors

- [Suryakant Pradhan](https://github.com/Pradhan-7787)

## License

This project is licensed under the [MIT License](LICENSE).
