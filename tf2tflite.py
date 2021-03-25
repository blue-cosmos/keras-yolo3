import tensorflow as tf
import sys
from tensorflow import keras
model = keras.models.load_model(sys.argv[1])
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
with open(sys.argv[2], "wb") as fout:
    fout.write(tflite_model)