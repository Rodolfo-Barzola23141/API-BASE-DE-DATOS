from sklearn.linear_model import LinearRegression
import numpy as np

# Datos de entrenamiento (ejemplo MUY simple)
X = np.array([[1], [2], [3]])  # Una sola característica
y = np.array([3, 5, 7])      # Valores correspondientes

model = LinearRegression()
model.fit(X, y)

def predict(feature): #recibe un valor directamente
    try:
        feature = float(feature) #convierte el valor a float
        prediction = model.predict(np.array([[feature]])) #realiza la prediccion
        return prediction[0]
    except (ValueError, TypeError): #captura los posibles errores
        return None