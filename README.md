# Waste Classification for Smart Recycling

## Project Overview
Waste Classification for Smart Recycling is an AI-powered system that automatically classifies waste images into different categories to improve recycling efficiency. The system uses Deep Learning and Transfer Learning techniques with the MobileNetV2 model to identify waste types accurately.

The project aims to reduce manual effort in waste segregation and support smart recycling systems.

---

## Problem Statement
Manual waste segregation is slow, inefficient, and prone to human errors. Improper waste sorting leads to reduced recycling efficiency and increased landfill waste. Traditional sensor-based systems can only detect limited waste types and lack intelligent image recognition capabilities.

Therefore, an automated AI-based waste classification system is required to improve waste segregation accuracy and scalability.

---

## Proposed Solution
The proposed system uses a Deep Learning model based on Transfer Learning with MobileNetV2 to classify waste images into 9 different categories. The system processes an input image, extracts features using the pretrained MobileNetV2 model, and predicts the waste category with a confidence score.

This solution can be integrated into smart recycling systems or smart bins to automate waste sorting.

---

## Technology Stack
- **Programming Language:** Python
- **Frameworks:** TensorFlow, Keras
- **Model:** MobileNetV2 (Transfer Learning)
- **Libraries:** NumPy, OpenCV, Matplotlib
- **Platform:** Google Colab

---

## Key Features
- AI-based waste classification
- 9-class waste detection
- Transfer Learning using MobileNetV2
- Real-time image prediction
- Confidence score display
- Scalable for smart recycling systems

---

## Dataset
- Training Images: 1911
- Validation Images: 473
- Total Classes: 9

---

## Model Performance
| Model | Validation Accuracy |
|------|---------------------|
| Basic CNN | ~50% |
| MobileNetV2 | **67.6%** |

Transfer learning significantly improved the model performance.

---

## System Architecture
1. Image Input
2. Image Preprocessing (Resize 224×224, Normalization)
3. Feature Extraction using MobileNetV2
4. Dense Classification Layers
5. Softmax Output Layer
6. Waste Category Prediction

---

## Future Enhancements
- Increase dataset size
- Fine-tune MobileNetV2 layers
- Deploy as Web Application
- Deploy as Mobile Application
- Integrate with IoT Smart Waste Bins
- Improve accuracy to 80%+

---

## Contributors
- Likitha M S
- Ramya S Uliger
- Kanan

Mentor: Dr. Sridhar Devarajan
