from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def CreateNet(x_train):
    model = Sequential()
    model.add(Dense(64, activation='sigmoid', input_shape=(x_train.shape[1],)))
    model.add(Dense(64, activation='sigmoid'))
    model.add(Dense(64, activation='sigmoid'))
    model.add(Dense(64, activation='sigmoid'))
    model.add(Dense(64, activation='sigmoid'))
    model.add(Dense(1, activation='sigmoid'))
    print(model.summary())
    model.compile(optimizer='rmsprop', loss='mse')
    try:
        model.load_weights('Weights.h5')
    except:
        print("Нет файла весов")
    finally:
        return model

def Lear(model, x_train, y_train):
    history = model.fit(x_train, y_train, epochs=100000, validation_split=0.1, verbose=2)
    model.save_weights('Weights.h5')
    return history

def Solve(model, x):
    pred = model.predict(x).flatten()
    return pred

"""def Result(model, x):
    pred = model.predict(x).flatten()
    return pred"""









