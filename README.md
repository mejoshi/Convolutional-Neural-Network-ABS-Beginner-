# Convulation Neural Network
CNN or Convulation Neural Network, I've created a CNN architecure, where i added 4 CRP, 1 flatten and 6 hidden layers. I've got 89% Accuracy with this architecure.


Layer (type)                  Output Shape            Param   

conv2d_1 (Conv2D)            (None, 148, 148, 32)      896       
activation_1 (Activation)    (None, 148, 148, 32)      0         
max_pooling2d_1 (MaxPooling2 (None, 74, 74, 32)        0         

conv2d_2 (Conv2D)            (None, 72, 72, 32)        9248      
activation_2 (Activation)    (None, 72, 72, 32)        0         
max_pooling2d_2 (MaxPooling2 (None, 36, 36, 32)        0         

conv2d_3 (Conv2D)            (None, 34, 34, 32)        9248      
activation_3 (Activation)    (None, 34, 34, 32)        0         
max_pooling2d_3 (MaxPooling2 (None, 17, 17, 32)        0         

conv2d_4 (Conv2D)            (None, 15, 15, 32)        9248      
activation_4 (Activation)    (None, 15, 15, 32)        0         
max_pooling2d_4 (MaxPooling2 (None, 7, 7, 32)          0  

flatten_1 (Flatten)          (None, 1568)              0 

dense_1 (Dense)              (None, 1024)              1606656   
dense_2 (Dense)              (None, 720)               738000    
dense_3 (Dense)              (None, 600)               432600    
dense_4 (Dense)              (None, 712)               427912    
dense_5 (Dense)              (None, 600)               427800    
dense_6 (Dense)              (None, 512)               307712    
dense_7 (Dense)              (None, 7)                 3591  

Total params: 3,972,911
Trainable params: 3,972,911
Non-trainable params: 0


Number of class we have is 7 (7 members of the family)
Now, i've used my dad's image, to see the accuracy.

{'big_brother': 0, 'me': 1, 'dad': 2, 'grandmother': 3, 'sis': 4, 'mom': 5, 'younger_brother': 6}

prediction : [[0. 0. 1. 0. 0. 0. 0.]]
As you can see, this model is good. Model successfully recognised my dad.
