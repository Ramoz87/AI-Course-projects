# Test without convolutional, pooling or hidden layers:

`model = tf.keras.models.Sequential([
        tf.keras.layers.Input(shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(NUM_CATEGORIES, activation='softmax')
    ])`
Result: accuracy: 0.7806 - loss: 37.2155

# Tests with convolutional and/or pooling layers:

## 1 convolution layer
`model = tf.keras.models.Sequential([
        tf.keras.layers.Input(shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
        
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(NUM_CATEGORIES, activation='softmax')
    ])`
Result: accuracy: 0.8946 - loss: 1.1506

## 1 convolution(32 filters) and 1 pooling(2x2) layers
`model = tf.keras.models.Sequential([
        tf.keras.layers.Input(shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
        
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
       
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(NUM_CATEGORIES, activation='softmax')
    ])`
Result: accuracy: 0.9242 - loss: 0.6550

## 1 convolution(128 filters) and 1 pooling(2x2) layers
`model = tf.keras.models.Sequential([
        tf.keras.layers.Input(shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
        
        tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(NUM_CATEGORIES, activation='softmax')
    ])`
Result: accuracy: 0.9430 - loss: 0.6693

## 2 convolution and 2 pooling layers
`model = tf.keras.models.Sequential([
        tf.keras.layers.Input(shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
        
        tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(NUM_CATEGORIES, activation='softmax')
    ])`
Result: accuracy: 0.9185 - loss: 0.3756

## 1 convolution(128 filters) and 1 pooling(5x5) layers
`model = tf.keras.models.Sequential([
        tf.keras.layers.Input(shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
        
        tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(5, 5)),

        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(NUM_CATEGORIES, activation='softmax')
    ])`
Result: accuracy: 0.9002 - loss: 0.5179

# Tests with convolutional, pooling and hidden layers:

`model = tf.keras.models.Sequential([
        tf.keras.layers.Input(shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
        
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation="relu"),

        tf.keras.layers.Dense(NUM_CATEGORIES, activation='softmax')
    ])`
Result: accuracy: 0.9107 - loss: 0.6556

`model = tf.keras.models.Sequential([
        tf.keras.layers.Input(shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
        
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(256, activation="relu"),

        tf.keras.layers.Dense(NUM_CATEGORIES, activation='softmax')
    ])`
Result: accuracy: 0.9366 - loss: 0.5895

`model = tf.keras.models.Sequential([
        tf.keras.layers.Input(shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
        
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(256, activation="relu"),
        tf.keras.layers.Dropout(0.1),

        tf.keras.layers.Dense(NUM_CATEGORIES, activation='softmax')
    ])`
Result: accuracy: 0.9479 - loss: 0.2566