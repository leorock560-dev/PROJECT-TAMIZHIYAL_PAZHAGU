import numpy as np
import pickle as pkl
from tensorflow.keras.models import load_model

model = load_model("transliterator.keras")

with open("mappings.pkl", "rb") as f:
    m = pkl.load(f)

input_char_to_num  = m["input_char_to_num"]
target_char_to_num = m["target_char_to_num"]
max_input_len      = m["max_input_len"]
num_to_target      = {v: k for k, v in target_char_to_num.items()}

def predict_word(word):
    encoded = [input_char_to_num.get(ch, 0) for ch in word]
    encoded = encoded[:max_input_len]                           
    padded  = encoded + [0] * (max_input_len - len(encoded))     

    pred = model.predict(np.array([padded]), verbose=0)
    predicted_indices = np.argmax(pred[0], axis=1)
    return ''.join(num_to_target[i] for i in predicted_indices if i != 0)