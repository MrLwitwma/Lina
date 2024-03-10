INTRODUCING Lina a female AI that can help you do mathematical problems and help you while coding.
Note: Lina can provide incorrect or inaccurate information please don't depend fully on Lina!



'''
How to use?
--Run the program lina.py and go to http://127.0.0.1:5000

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



Details:
    Version(1.0)
        Launched:27/08/23
        Features:
            *Can solve basic mathematical problems
            *Can Find Binary of any Decimal Number
            *Can respond to user if the input matches the saved data
        Problems:
            *Mathematical task can cause crash(23971293871237**21367218736)
            *UI is not stable(The container shakes and the values goes out of boundary)
            *System doesn't respond on dividing numbers by 0

    Version(1.1)
        Launched: 01/11/23
        New Features:
            *Can find percentage of values
            *Dark and Light UI
            *Links Provided are clickable
            *Better PC experience
            *Can Find Factorial of values(Limit 1500, to avoid crashes)
            *Can convert any base value to decimal base value
            *Can convert roman numeral to decimal numeral
            *Feedback System added!
        Problems:
            *Unorganised files
            *Bad text recognision
        Fixing:
            *Added Limitations on exponentiation(**) to avoid crash
            *Tells error when number divided by 0(ZeroDivisionError Fixed)
            *Fixed UI(Container fixed)
    Version(2.0)
        Launched: 01/03/2024
        New Features:
            *New UI
            *More Accurate reponses to user
            *Find factors of values
            *Find largest and smallest prime factors
            *One Base value to another Base value (xBase to yBase)
            *Number to words
            *Decimal to Roman Numeral
        Problems:
            *Null so Far
        Fixing:
            *Organised files
            *Better text recognision


    Latest Version(2.0):
        All Features:
            *Can solve basic mathematical problems
            *Can Find Binary of any Decimal Number
            *Can respond to user if the input matches the saved data
            *Can find percentage of values
            *Dark and Light UI with Cleaner UI
            *Links Provided are clickable
            *Better PC experience
            *Can Find Factorial of values(Limit 1500, to avoid crashes)
            *Can convert any base value to decimal base value
            *More Accurate reponses to user
            *Find factors of values
            *Find largest and smallest prime factors
            *One Base value to another Base value (xBase to yBase)
            *Number to words
            *Decimal to Roman Numeral
            *Roman to decimals






What can Lina do? What are its limitations?
    Ability:
        Lina is an AI that is made to help user to do mathematical task as well as some coding based tasks. It was actually made by the creator to learn how an AI works, it was made as a test bot. It can work as a text assistant and help you do some basic tasks. 
    Limitations:
        It is not like it can do anything, it has limitations and the task it can do(Mathematical tasks) is also limited(To avoid crashes in server). It does not have a alogorithem to learn so it can only do what is stored in its system to do! It cannot generate text on its own it only works with the data that is stored in its system.