# File: data_loader.py
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def load_data(dataset_path, image_size=(128, 128), batch_size=32):
    datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

    train_generator = datagen.flow_from_directory(
        dataset_path,
        target_size=image_size,
        batch_size=batch_size,
        class_mode='binary',  # Assuming binary classification for simplicity
        subset='training'
    )

    validation_generator = datagen.flow_from_directory(
        dataset_path,
        target_size=image_size,
        batch_size=batch_size,
        class_mode='binary',
        subset='validation'
    )

    return train_generator, validation_generator
