import streamlit as st
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle
import faiss
from zipfile import ZipFile

data = pd.read_csv('data/df_merged.csv')    # combined latest dataset

with ZipFile('my-embeddings.zip', 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()
    zip.extractall()

# streamlit adjustments
st.title(":rainbow[~I'm Here To Answer~]:information_desk_person:")
question = st.text_input("", placeholder= "Go ahead, ask your ultimate, top-shelf, mind-blowing question!")
button = st.button(":rainbow[~Unleash Truth~]")

with st.spinner("Coming right up—freshly baked with 0s and 1s!"):
    if button and question :
        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

        with open("my-embeddings.pkl", "rb") as fIn:
            cache_data = pickle.load(fIn)
            embeddings = cache_data['embeddings']
        embeddingsQ = model.encode(question)
        embeddingsQ = np.array(embeddingsQ).reshape(1, -1).astype("float32")

        index = faiss.IndexFlatL2(embeddings.shape[1])
        # Pass the index to IndexIDMap
        index = faiss.IndexIDMap(index)
        # Add vectors and their IDs, set to be DF indexes
        index.add_with_ids(embeddings, data.index.values)
        # Serialise index and store it as a pickle
        with open("faiss_index1.pickle", "wb") as f:
            pickle.dump(faiss.serialize_index(index), f)

        L2, ID = index.search(np.array(embeddingsQ).astype("float32"), k=1)
        index_list = ID.flatten().tolist()
        results = data.loc[index_list, :]

        results['L2_distance'] = L2.flatten().tolist()

        st.write(results['answers'].iloc[0])



