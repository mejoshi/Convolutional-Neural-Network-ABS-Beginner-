from keras.models import load_model
from keras_preprocessing import image
import numpy as np


model = load_model('family.h5')

img = image.load_img('D:\\photos\\family_dataset\\validation\\_20181223_212425.JPG', target_size=(150,150))
img_np = image.img_to_array(img)
img_np_expand = np.expand_dims(img_np,axis=0)

prediction = model.predict(img_np_expand)
print(prediction)

model.summary()


