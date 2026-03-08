import tensorflow as tf
import numpy as np
import cv2

model = tf.keras.models.load_model("waste_model.h5")

classes = ["cardboard","glass","metal","paper","plastic","trash","battery","organic","e-waste"]

img = cv2.imread("test.jpg")
img = cv2.resize(img,(224,224))
img = img/255.0
img = np.reshape(img,(1,224,224,3))

prediction = model.predict(img)

print("Predicted Class:",classes[np.argmax(prediction)])
print("Confidence:",np.max(prediction))
