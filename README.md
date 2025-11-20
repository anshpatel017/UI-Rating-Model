# SGP UI Model - Image Rating Classification

A deep learning model built with YOLOv8 for automated image quality rating classification. This model predicts image ratings on a scale of 1-5 based on visual quality metrics.

## Overview

This project implements a YOLOv8-based classifier that automatically rates images into five quality categories (rating_1 through rating_5). The model is trained to evaluate image quality and provide confidence scores for predictions.

## Dataset Structure

The dataset is organized into five class folders representing different rating levels:

```
dataset/
├── rating_1/     # Low quality images
├── rating_2/     # Below average quality images
├── rating_3/     # Average quality images
├── rating_4/     # Good quality images
└── rating_5/     # Excellent quality images
```

Each folder contains training images for the respective rating category.

### Dataset Link
[Add your dataset link here - e.g., Kaggle, Google Drive, or hosted repository]

## Project Structure

```
UI Model/
├── rate.py              # Main inference script
├── best.pt              # Trained YOLOv8 model weights
├── v_4_model.ipynb      # Jupyter notebook with model training and evaluation
├── image_*.jpg          # Sample test images
└── README.md            # This file
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/anshpatel017/SGP-UI-Model.git
cd UI-Model
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Rate a single image:
```bash
python rate.py image_1.jpg
```

**Output:**
```
Predicted Rating: 4 / 5
Confidence: 0.95
```

### How It Works

The `rate_image()` function:
1. Loads the trained YOLOv8 model
2. Performs inference on the input image
3. Extracts the predicted class (rating_1 to rating_5)
4. Returns the rating number (1-5) and confidence score

## Model Details

- **Framework:** YOLOv8 (Ultralytics)
- **Input:** Image file path
- **Output:** Rating (1-5) and confidence score
- **Model File:** `best.pt`

## Requirements

- ultralytics
- torch
- torchvision
- opencv-python
- numpy

See `requirements.txt` for complete dependencies and versions.

## Training

The model was trained using the Jupyter notebook `v_4_model.ipynb`. This notebook includes:
- Data loading and preprocessing
- Model training with YOLOv8
- Validation and evaluation
- Performance metrics

To retrain or modify the model, refer to the notebook for detailed steps.

## Results

The model achieves high accuracy in classifying images into the five rating categories. Confidence scores indicate the model's certainty in its predictions.

## Author

**Ansh Patel**
- GitHub: [@anshpatel017](https://github.com/anshpatel017)
- Email: andhgpatel017@gmail.com

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Built with [YOLOv8](https://github.com/ultralytics/ultralytics)
- Dataset structure follows standard classification conventions

---

For questions or issues, please open an issue on the GitHub repository.
