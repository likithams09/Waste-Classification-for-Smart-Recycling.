from google.colab import files
uploaded = files.upload()
from google.colab import drive
drive.mount('/content/drive')
from tensorflow.keras.models import load_model

model = load_model("waste_classifier_model.h5")
print("Model loaded successfully!")
uploaded = files.upload()
import numpy as np
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt

img_path = list(uploaded.keys())[0]

img = image.load_img(img_path, target_size=(224,224))
img_array = image.img_to_array(img)
img_array = img_array / 255.0
img_array = np.expand_dims(img_array, axis=0)

plt.imshow(img)
plt.axis('off')
plt.show()

prediction = model.predict(img_array)

class_names = [
    "Cardboard",
    "Food Organics",
    "Glass",
    "Metal",
    "Miscellaneous Trash",
    "Paper",
    "Plastic",
    "Textile Trash",
    "Vegetation"
]

predicted_class = class_names[np.argmax(prediction)]
confidence = np.max(prediction) * 100

print("Predicted Waste Type:", predicted_class)
print(f"Confidence: {confidence:.2f}%")
