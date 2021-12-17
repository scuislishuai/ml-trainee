import tensorflow as tf
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# preprocessing

x_train, x_test = x_train / 255., x_test / 255.

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),  # 28 * 28 => 784
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=['sparse_categorical_accuracy'])

model.fit(x=x_train, y=y_train, epochs=5, batch_size=32,
          validation_data=(x_test, y_test),
          validation_freq=20)
model.summary()