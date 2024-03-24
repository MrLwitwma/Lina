#Version 3.0
'''
How to use?
--Run this program and Lina is ready to use in your Terminal.

Where and what can I use it for?
----You can use Lina as your chatbot assistant. 
    A calculator that can talk to you. 
    You can make changes in main file and change it into a virtual assistant.
    You can use it as a virtual friend by changing its responses data.
    Poem Writer/ Story Writer.

Show Support:
--Support MrLwitwma by donating to him or just subscribing/following his Social Media Accounts
Youtube: https://youtube.com/@mrlwitwma
Instagram: https://instagram.com/mrlwitwma
GitHub: https://github.com/mrlwitwma
--Use Lina Online at https://lina.mrlwitwma.com, if link is unable check my channel pages for details on new site..

Folders Structure:
Lina(3.0)
    -lina.py
    -main.py
    -reponses.py
    -data.py
    -training.py
    -teminal_lina.py (Use this if you don't have Flask installed)
    -readme.md
    -requirements.txt
    -static
        -lina.svg
        -new-chat.svg
        -script.js
        -style.css
    -templates
        -404.html
        -feedback.html
        -index.html
    -lina
        -variables
            -variables.index
            -variables.data-00000-of-00001
        -assets
            -
        -word_index.npy 
        -saved_model.pb 
        -readme.md 
        -fingerprint.pb 
        -keras_metadata.pb 
        -datas.txt

To use Lina(3.0) on other files just import the lina_respond
example: 
    from main import lina_respond
Using Lina(3.0) can be a harder than (2.0) but ya its simple too
    prompt = "Hey Can you Help me solve my Maths Homework?"
    response = lina_respond(prompt, 'auto', False, False)[1]
    print(response)
# Here it takes 4 parameteres
prompt, length, verbose, continue_prompt
prompt -- takes user Input or Query
length -- How many words it must generate, 'auto' if you want complete sentence.
verbose -- True/False, if True it prints the genrating text in terminal.
continue_prompt -- True/False, if it is True it will continue the previous broken prompt(Recommended to be False unless using the WebVersion)

Why is there [1]?
    The lina_respond() funtion returns a list of value if it is kept in (continue_prompt=False), [0] is the Prompt or user input and [1] is the response from lina you can also use [2] if your (next_word) length is large like 100 or more.


To use Lina(2.0) on other files just import the lina_respond_algo
example:
    from training import lina_response_algo
Make sure to lower your text for it to work properly
example:
    prompt = 'Hey what can you do?'
    response = lina_response(promt.lower(), userId='XXXXXXXX')
    print(response)
#Here userId is used to store data of a specific user



---
 This software is free to use you can share the main file in GitHub with your friends, stealing it and selling it is forbidden. 
 Using this software and saying it is yours is forbidden is such things arises strict actions will be taken.
 If you are using this model in your videos please make sure to mention the Model and creator -Lina(3.0) by MrLwitwma [Mr(Mister), Lwitwma(Lwi-tw-ma)]
 Original Owner/ Creators: MrLwitwma
 Model: Lina(3.0)
---
'''
from main import lina_respond

while True:
    user_in = input('User: ')
    respond = lina_respond(user_in, 'auto', False, False)[1]
    print('Lina:', respond)