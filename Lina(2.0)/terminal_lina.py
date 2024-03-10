#Version 2.0
'''
How to use?
--Run this program and you will be able to use Lina in your terminal.

Where and what can I use it for?
----You can use Lina as your chatbot assistant. 
    A calculator that can talk to you. 
    You can make changes in main file and change it into a virtual assistant.
    You can use it as a virtual friend by changing its responses data.

Show Support:
--Support MrLwitwma by donating to him or just subscribing his youtube channel
Youtube: https://youtube.com/@mrlwitwma
Instagram: https://instagram.com/mrlwitwma
--Use Lina Online at https://lina.mrlwitwma.com, if link is unable check my channel pages for details on new site..

Folders Structure:
Lina(2.0)
    -lina.py
    -reponses.py
    -data.py
    -training.py
    -teminal_lina.py (Use this if you don't have Flask installed)
    -readme.txt
    -statics
        -lina.svg
        -new-chat.svg
        -script.js
        -style.css
    -templates
        -404.html
        -feedback.html
        -index.html

To use Lina on other files just import the lina_respond
example: 
    from training import lina_response
Make sure to lower your text for it to work properly
example:
    prompt = 'Hey what can you do?'
    response = lina_respond(promt.lower(), userId='XXXXXXXX')
    print(response)
#Here userId is used to store data of a specific user



---
 This software is free to use you can share the main file in GitHub with your friends, stealing it and selling it is forbidden. 
 Using this software and saying it is yours is fobidden is such things arises strict actions will be taken.
 If you are using this model in your videos please make sure to mention the Model and creator -Lina(2.0) by MrLwitwma [Mr(Mister), Lwitwma(Lwi-tw-ma)]
 Original Owner/ Creators: MrLwitwma
 Model: Lina(2.0)
---
'''

from training import lina_respond

while True:
    user_in = input('User: ')
    respond = lina_respond(user_in.lower(), userId='XXXXXXXX')
    print('Lina:', respond)