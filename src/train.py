# File: train.py
from data_loader import load_data
from model import build_model

if __name__ == "__main__":
    dataset_path = 'data/celeba/lfw'  # Adjust this path based on your actual directory structure
    image_size = (128, 128)
    batch_size = 32
    epochs = 10

    train_generator, validation_generator = load_data(dataset_path, image_size, batch_size)
    model = build_model(input_shape=(image_size[0], image_size[1], 3))

    history = model.fit(
        train_generator,
        epochs=epochs,
        validation_data=validation_generator
    )

    # Save the trained model
    model.save('saved_models/celeba_headshot_generator.h5')
