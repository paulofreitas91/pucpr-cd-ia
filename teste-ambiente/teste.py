import sys 
# Verifica a instalação do scikit-learn
try:
    import sklearn
    print(f"scikit-learn version: {sklearn.__version__}")
except ImportError:
    print("scikit-learn não está instalado. Por favor, instale usando 'pip install scikit-learn'.")

# Verifica a instalação do TensorFlow
try:
    import tensorflow as tf
    print(f"TensorFlow version: {tf.__version__}")
except ImportError:
    print("TensorFlow não está instalado. Por favor, instale usando 'pip install tensorflow'.")




# Teste básico para PyCharm Community Edition
print("\n\n #####PyCharm Community Edition está instalado e pronto para uso####\n\n")



# Teste básico de Python
print(f"\n\n #####Versão do Python: {sys.version}\n\n")
input("Pressione Enter para continuar...")


print("\n\n #####Vamos testar um modelo do sklearn\n\n")
# Exemplo de uso do scikit-learn para classificação simples
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Carrega o conjunto de dados Iris
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Cria e treina um classificador SVM
clf = SVC(kernel='linear', random_state=42)
clf.fit(X_train, y_train)

# Faz previsões no conjunto de teste
y_pred = clf.predict(X_test)

# Calcula a acurácia
accuracy = accuracy_score(y_test, y_pred)
print(f"\n\n #####Acurácia do classificador SVM: {accuracy:.2f} \n\n")
input("Pressione Enter para continuar...")

#Tentando o tensorflow
print("\n\n #####Vamos testar um modelo do tensorflow..\n\n")
import tensorflow as tf
from tensorflow.keras import layers, models, datasets
import matplotlib.pyplot as plt

# Carrega o conjunto de dados MNIST
(x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()

# Normaliza os dados de pixel para o intervalo [0, 1]
x_train, x_test = x_train / 255.0, x_test / 255.0

# Adiciona uma dimensão para os canais de cor (no caso do MNIST, é grayscale)
x_train = x_train[..., tf.newaxis]
x_test = x_test[..., tf.newaxis]

# Define o modelo CNN
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compila o modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Treina o modelo
history = model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# Avalia o modelo
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"\n\n ##### Acurácia no conjunto de teste: {test_acc} \n\n")
input("Pressione Enter para continuar...")

# Plota a acurácia de treinamento e validação ao longo das épocas
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Épocas')
plt.ylabel('Acurácia')
plt.legend()
plt.show()

