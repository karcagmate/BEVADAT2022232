# %%
import tensorflow as tf

# %%
'''
Készíts egy metódust ami a mnist adatbázisból betölti a train és test adatokat. (tf.keras.datasets.mnist.load_data())
Majd a tanitó, és tesztelő adatokat normalizálja, és vissza is tér velük.


Egy példa a kimenetre: train_images, train_labels, test_images, test_labels
függvény neve: mnist_digit_data
'''

# %%
def mnist_digit_data():
    #fashion_mnist = tf.keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
    train_images=train_images/255.0
    test_images=test_images/255.0
    return train_images,train_labels,test_images,test_labels

# %%
'''
Készíts egy neurális hálót, ami képes felismerni a kézírásos számokat.
A háló kimenete legyen 10 elemű, és a softmax aktivációs függvényt használja.
Hálon belül tetszőleges számú réteg lehet.


Egy példa a kimenetre: model,
return type: keras.engine.sequential.Sequential
függvény neve: mnist_model
'''

# %%
def mnist_model():
    model=tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28,28)),
        tf.keras.layers.Dense(128,activation='softmax'),
        tf.keras.layers.Dense(10)
    ])
    return model

# %%
'''
Készíts egy metódust, ami a bemeneti hálot compile-olja.
Optimizer: Adam
Loss: SparseCategoricalCrossentropy(from_logits=False)

Egy példa a bemenetre: model
Egy példa a kimenetre: model
return type: keras.engine.sequential.Sequential
függvény neve: model_compile
'''

# %%
def model_compile(model:tf.keras.Sequential):
     model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
                  metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])
     return model
    
                  

# %%
'''
Készíts egy metódust, ami a bemeneti hálót feltanítja.

Egy példa a bemenetre: model,epochs, train_images, train_labels
Egy példa a kimenetre: model
return type: keras.engine.sequential.Sequential
függvény neve: model_fit
'''

# %%
def model_fit(model:tf.keras.Sequential,epochs,train_images,train_labels):
     model.fit(train_images,train_labels,epochs=epochs)
     return model

# %%
'''
Készíts egy metódust, ami a bemeneti hálót kiértékeli a teszt adatokon.

Egy példa a bemenetre: model, test_images, test_labels
Egy példa a kimenetre: test_loss, test_acc
return type: float, float
függvény neve: model_evaluate
'''

# %%
def model_evaluate(model:tf.keras.Sequential,test_images,test_labels):
    test_loss,test_acc=model.evaluate(test_images,test_labels,verbose=2)
    return test_loss,test_acc

# %%
#train_images,train_labels,test_images,test_labels=mnist_digit_data()
#model=mnist_model()
#compile=model_compile(model)
#fit=model_fit(compile,6,train_images,train_labels)
#test_loss,test_acc=model_evaluate(fit,test_images,test_labels)
#print(test_loss)
#print(test_acc)





# %%
