# Retreival Based Question Answering System


## A project with a Streamlit interface that returns the most accurate predefined answer to a given question.

- The project is based on a dataset containing around 90,000 question-answer pairs.
- It uses the Hugging Face sentence transformer model `all-MiniLM-L6-v2` for embedding the sentences.
- This model is chosen because it is small, fast, and effective at generating sentence embeddings.
- The user interface is built with Streamlit.  When a user asks a question through the Streamlit app, the question is embedded using the same model.
- FAISS is used to find the most similar question from the dataset.
- The matched answer is then shown to the user.
- The project also includes an evaluation script to test the model’s performance.


