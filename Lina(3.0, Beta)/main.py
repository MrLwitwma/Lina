import numpy as np
import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences


# Values to change based on model changes
modelPath = 'lina'    # Folder where model is saveds
max_sequence_length = 188  # Update this value to match the max sequence length used during training
# Load the pre-trained model
model = keras.models.load_model(modelPath)

# Load the tokenizer with the vocabulary used during training
tokenizer = Tokenizer(filters='', lower=False)
tokenizer.word_index = np.load(f'{modelPath}/word_index.npy', allow_pickle=True).item()  # Load the word index
tokenizer.index_word = {i: w for w, i in tokenizer.word_index.items()}  # Reverse the word index


# Function to generate text given a seed text
def generate_text(seed_text, num_next_words, max_sequence_len, printText):
    # If unsure of the length
    if num_next_words == 'auto':
        next_words = 1000
    else:
        next_words = num_next_words

    if printText:
        print(seed_text)  # Print the seed text before generating additional words
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        predicted_probs = model.predict(token_list, verbose=0)
        predicted_index = np.argmax(predicted_probs)
        output_word = tokenizer.index_word.get(predicted_index, '')
        seed_text += " " + output_word
        if printText:
            print(seed_text)
        if num_next_words == 'auto' and seed_text.count('---') >= 2:
            break
    return seed_text


def lina_respond(prompt, length, verbose, continue_prompt):
    '''
    It returns generated text value as a list
    example usage:
        prompt = 'What are prime numbers?'
        response = lina_respond(prompt, length=40, verbose=False, continue_prompt=False)
        print(response[1])
        Use [1] or greater as [0] is kept for the prompt

    prompt - User Prompt or users query
    length - Words it must generate, keep it small for faster response in your application, use auto if you are unsure of the length.
             example usage:
                lina_response(prompt, length='auto', verbose=False)
    verbose - Print the word generation process
    continue_prompt - Used for comlpeting unfinished prompt

    example usage2:
        prompt = 'What are prime numbers? --- Prime numbers are '
        response = ' '.join(lina_respond(prompt, length=40, verbose=False, continue_prompt=True))
        print(response)
    '''
    # print(prompt)
    if not continue_prompt:
        prompt += ' ---'
        generated_text = generate_text(prompt, length, max_sequence_length, verbose)
    else:
        generated_text = generate_text(prompt, length, max_sequence_length, verbose)
        return generated_text.replace('\n\n', '<linebreak> <linebreak>').replace('\n', '<linebreak>').split()
    generated_text = generated_text.split('---')
    return generated_text


 #Stores User Chats for improving future updates
def store_input(input, userId, file):
    with open(f'{file}.txt', 'a', encoding='utf-8') as f:
         f.write(f"{userId}: {input}\n")