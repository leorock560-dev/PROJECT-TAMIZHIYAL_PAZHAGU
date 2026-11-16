import pandas as pd
import numpy as np
import pickle as pkl
import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, RepeatVector, Dense, TimeDistributed
from tensorflow.keras.callbacks import EarlyStopping

print("TensorFlow version:", tf.__version__)

early_stop = EarlyStopping(
    monitor="val_loss",
    patience=5,
    restore_best_weights=True
)

data = pd.read_csv("transliterations8.csv")
data = data.dropna(subset=['tanglish_words', 'tamil_words'])

input_text  = data['tanglish_words'].astype(str).tolist()
target_text = data['tamil_words'].astype(str).tolist()

input_char  = sorted(set(ch for word in input_text  for ch in word))
target_char = sorted(set(ch for word in target_text for ch in word))

input_char_to_num  = {ch: i + 1 for i, ch in enumerate(input_char)}
target_char_to_num = {ch: i + 1 for i, ch in enumerate(target_char)}

input_vocab_size  = len(input_char_to_num)  + 1   # +1 for pad token
target_vocab_size = len(target_char_to_num) + 1

print(f"Input vocab size : {input_vocab_size}")
print(f"Target vocab size: {target_vocab_size}")

encoded_input  = [[input_char_to_num[ch]  for ch in word] for word in input_text]
encoded_target = [[target_char_to_num[ch] for ch in word] for word in target_text]

max_input_len  = max(len(w) for w in encoded_input)
max_target_len = max(len(w) for w in encoded_target)

def post_pad(sequences, max_len):
    return np.array([seq + [0] * (max_len - len(seq)) for seq in sequences])

X = post_pad(encoded_input,  max_input_len)
Y = post_pad(encoded_target, max_target_len)

print(f"X shape: {X.shape},  Y shape: {Y.shape}")

Y_cat = to_categorical(Y, num_classes=target_vocab_size)
print(f"Y_cat shape: {Y_cat.shape}")

model = Sequential([
    Embedding(input_dim=input_vocab_size, output_dim=128, mask_zero=True),
    LSTM(256),
    RepeatVector(max_target_len),
    LSTM(256, return_sequences=True),
    TimeDistributed(Dense(target_vocab_size, activation='softmax'))
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.summary()

model.fit(X, Y_cat, epochs=50, batch_size=64, validation_split=0.2, callbacks=[early_stop])

def predict_word(tanglish_word):
    encoded = [input_char_to_num.get(ch, 0) for ch in tanglish_word]

    encoded = encoded[:max_input_len]
    padded  = encoded + [0] * (max_input_len - len(encoded))

    pred = model.predict(np.array([padded]), verbose=0)         
    predicted_indices = np.argmax(pred[0], axis=1)               

    num_to_target = {v: k for k, v in target_char_to_num.items()}
    return ''.join(num_to_target[i] for i in predicted_indices if i != 0)

with open("mappings.pkl", "wb") as f:
    pkl.dump({
        "input_char_to_num":  input_char_to_num,
        "target_char_to_num": target_char_to_num,
        "max_input_len":      max_input_len,
        "max_target_len":     max_target_len,
        "input_vocab_size":   input_vocab_size,
        "target_vocab_size":  target_vocab_size,
    }, f)

model.save("transliterator.keras")
print("Model and mappings saved.")

test_word = input_text[0]
print(f"Sample — Input: {test_word!r}  →  Predicted: {predict_word(test_word)!r}  |  Actual: {target_text[0]!r}")