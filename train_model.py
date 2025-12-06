# -------------------------------------------------------
# 🍅 Tomato Leaf Disease Detection - Model Training Script
# -------------------------------------------------------

# 1️⃣ Import Libraries
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.models import Model
import matplotlib.pyplot as plt
import os

# 2️⃣ Define Dataset Paths
train_dir = 'dataset/train'
val_dir = 'dataset/valid'

# 3️⃣ Data Preprocessing
# ImageDataGenerator helps normalize and feed images to the model
datagen = ImageDataGenerator(rescale=1./255)

train_data = datagen.flow_from_directory(
    train_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)
val_data = datagen.flow_from_directory(
    val_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)

# 4️⃣ Build the Model (Using MobileNetV2 as Base)
base_model = MobileNetV2(
    weights='imagenet',        # Use pretrained weights
    include_top=False,         # Remove top dense layers
    input_shape=(224, 224, 3)  # Input image shape
)

# Freeze base model layers (so only our layers train)
for layer in base_model.layers:
    layer.trainable = False

# 5️⃣ Add Custom Layers for Our Tomato Dataset
x = Flatten()(base_model.output)
x = Dense(128, activation='relu')(x)
x = Dropout(0.3)(x)
output = Dense(train_data.num_classes, activation='softmax')(x)

model = Model(base_model.input, output)

# 6️⃣ Compile the Model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 7️⃣ Train the Model
history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=10
)

# 8️⃣ Save the Model
os.makedirs('backend/model', exist_ok=True)
model.save('backend/model/model.h5')
print("\n✅ Model trained and saved successfully at backend/model/model.h5")

# 9️⃣ Plot Accuracy Graph
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy Over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()
