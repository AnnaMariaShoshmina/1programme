import os
import numpy as np
from keras.models import Model
from keras.layers import Dense, Input
from keras.utils import np_utils
import matplotlib.pyplot as plt

X = []
for i in range(-20,20):
    for j in range(-20,20):
        X.append([i/10, j/10])
X = np.array(X)
Y = [1 if x ** 3 + y ** 3 <= 3*x*y
    else 0
    for [x, y] in X
]

l0 = Input(shape=(2,))
l1 = Dense(6, activation='sigmoid', use_bias=True)(l0)
l2 = Dense(1, activation='sigmoid', use_bias=False)(l1)

model = Model(input=l0, output=l2)

model.compile(
    loss='mean_squared_error',
    optimizer='adam',
    metrics=['accuracy']
)

if os.path.isfile("smart_duckling.h5"):
    model.load_weights("smart_duckling.h5")
else:
    model.fit(
        X, Y,
        epochs=5000,
        verbose=False
    )
    model.save("smart_duckling.h5")

 
plt.axis('equal')

c = np.r_[-2:2:0.1]

XY = np.transpose([np.tile(c, len(c)), np.repeat(c, len(c))])

Z = model.predict(XY)

for (x, y), z in zip(XY, Z):
    plt.scatter(x, y, c='red' if z[0] >= 0.5 else 'green')

plt.show()

def saturate(v):
    return min(1, max(0, v))

for (x, y), z in zip(XY, Z):
    plt.scatter(x, y, color=[(1, 1-saturate(z[0]), 1-saturate(z[0]))])

plt.show()
