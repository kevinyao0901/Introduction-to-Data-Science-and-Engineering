from keras.models import Model
from keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Dropout

def VGG19(input_shape=(224, 224, 3), num_classes=1000, conv_filters=(64, 128, 256, 512, 512), fc_units=(4096, 4096), dropout_rate=0.5):
    # 定义输入层
    inputs = Input(shape=input_shape)

    x = inputs
    for filters in conv_filters:
        x = Conv2D(filters=filters, kernel_size=(3, 3), padding="same", activation="relu")(x)
        x = Conv2D(filters=filters, kernel_size=(3, 3), padding="same", activation="relu")(x)
        x = MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(x)

    x = Flatten()(x)
    for units in fc_units:
        x = Dense(units=units, activation="relu")(x)
        x = Dropout(rate=dropout_rate)(x)

    outputs = Dense(units=num_classes, activation="softmax")(x)

    model = Model(inputs=inputs, outputs=outputs, name="VGG19")

    return model

if __name__ == "__main__":
    VGG19().summary()
