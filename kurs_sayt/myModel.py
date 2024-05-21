import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import LabelEncoder 
from tensorflow.keras.preprocessing.text import Tokenizer 
from tensorflow.keras.preprocessing.sequence import pad_sequences 
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Embedding, Conv1D, MaxPooling1D, GlobalMaxPooling1D, Dense, Dropout 
 
data = pd.read_csv('dataset.csv')  
texts = data['text'].values 
labels = data['label'].values 

label_encoder = LabelEncoder() 
labels = label_encoder.fit_transform(labels) 
 
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42) 
 
max_words = 10000 
max_len = 500 
 
tokenizer = Tokenizer(num_words=max_words) 
tokenizer.fit_on_texts(X_train) 
 
X_train_seq = tokenizer.texts_to_sequences(X_train) 
X_test_seq = tokenizer.texts_to_sequences(X_test) 
 
X_train_pad = pad_sequences(X_train_seq, maxlen=max_len) 
X_test_pad = pad_sequences(X_test_seq, maxlen=max_len) 
 
embedding_dim = 100 
 
model = Sequential() 
model.add(Embedding(max_words, embedding_dim, input_length=max_len)) 
model.add(Conv1D(128, 5, activation='relu')) 
model.add(MaxPooling1D(pool_size=5)) 
model.add(Conv1D(128, 5, activation='relu')) 
model.add(GlobalMaxPooling1D()) 
model.add(Dense(128, activation='relu')) 
model.add(Dropout(0.5)) 
model.add(Dense(1, activation='sigmoid')) 
 
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy']) 
history = model.fit(X_train_pad, y_train, epochs=10, batch_size=32, validation_split=0.2)
    

model.save('model.h5') 
 
# Сохранение токенайзера 
with open('tokenizer.pkl', 'wb') as handle: 
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)