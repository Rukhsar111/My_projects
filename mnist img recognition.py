import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import keras

from sklearn.datasets import fetch_mldata
df=fetch_mldata('MNIST original')

dataset=pd.read_csv(r'C:\Users\Aatif\Desktop\Datasets\mnist_784.csv')


from  tensorflow import Keras

from tensorflow.python import keras
from Keras.Datasets import mnist

df=tf.keras.datasets.mnist.load_data()
(training_images,training_labels), (test_images,test_labels)=tf.keras.datasets.mnist.load_data()
(training_images,training_labels), (test_images,test_labels)=dataset





df=pd.DataFrame(df)

X= dataset.data
some_value=training_images[29]
final_img= some_value.reshape(28,28)



plt.imshow(some_value)
plt.imshow(final_img)





res=some_value.reshape(28,28)