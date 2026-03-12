# Waste Classification for Smart Recycling

## Project Overview
Waste Classification for Smart Recycling is an intelligent system designed to automatically identify and classify waste materials using image processing and deep learning techniques. The system uses a Convolutional Neural Network (CNN) model to analyze waste images and classify them into categories such as organic (wet waste), dry waste, and metal waste. Proper waste segregation is essential for efficient recycling and environmental protection. Manual waste sorting is often slow, labor-intensive, and prone to human error. This project aims to develop an automated waste classification system that improves the efficiency of recycling processes. By using artificial intelligence, the system can quickly analyze waste images and determine the correct category. The proposed solution can support smart waste management systems and help reduce environmental pollution.The project aims to reduce manual effort in waste segregation and support smart recycling systems.


## Problem Statement
Waste segregation is an important step in recycling and waste management. However, manual waste sorting is inefficient and time-consuming. Human errors during waste segregation can lead to mixing of recyclable and organic waste, which reduces recycling efficiency. Many traditional waste management systems lack intelligent mechanisms to automatically identify waste types. As a result, large amounts of recyclable materials end up in landfills, causing environmental damage. Therefore, there is a need for an automated system that can accurately classify waste materials using modern technologies such as Artificial Intelligence and Deep Learning.
Therefore, an automated AI-based waste classification system is required to improve waste segregation accuracy and scalability.

## Proposed Solution
The proposed system uses a Convolutional Neural Network (CNN) model to automatically classify waste images. The model is trained using a dataset of labeled waste images containing different types of materials. During training, the CNN learns important visual features such as color, texture, and shape from the images. When a new waste image is given as input, the trained model processes the image and predicts its category. The system classifies waste into organic (wet waste), dry waste, and metal waste. This automated classification system can be integrated into smart recycling systems or waste sorting machines to improve waste management efficiency.


## Technology Stack
- Programming Language: Python
- Frameworks: TensorFlow, Keras
- Model:MobileNetV2 (Transfer Learning),CNN
- Libraries: NumPy, OpenCV, Matplotlib
- Platform: Google Colab

## Key Features
- AI-based waste classification
- 9-class waste detection
- Transfer Learning using MobileNetV2
- Real-time image prediction
- Confidence score display
- Scalable for smart recycling systems

## Dataset
- Training Images: 1911
- Validation Images: 473
- Total Classes: 9

## Model Performance

| Model     | Accuracy  |
| --------- | --------- |
| CNN Model | **92.5%** |

The CNN model achieved 92.5% accuracy, demonstrating strong performance in classifying waste images into the correct categories.

## System Architecture
1. Image Input
2. Image Preprocessing (Resize 224×224, Normalization)
3. Feature Extraction using MobileNetV2
4. Dense Classification Layers
5. Softmax Output Layer
6. Waste Category Prediction

## Future Enhancements
- Increase dataset size
- Fine-tune MobileNetV2 layers
- Deploy as Web Application
- Deploy as Mobile Application
- Integrate with IoT Smart Waste Bins
- Improve accuracy to 90+ and add more waste categories

## Contributors
- Likitha M S
- Ramya S Uliger
- Kanan

Mentor: Dr. Sridhar Devarajan
