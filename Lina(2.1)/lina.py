#Version 2.1
'''
How to use?
--Run this program and go to http://127.0.0.1:5000, your site is ready.

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
Lina(2.1)
    -assistant.py (Use it as a voice assistant)
    -lina.py
    -reponses.py
    -data.py
    -training.py
    -teminal_lina.py (Use this if you don't have Flask installed)
    -readme.txt
    -license.txt
    -statics
        -lina.svg
        -new-chat.svg
        -script.js
        -style.css
        -copy-code.js
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
 If you are using this model in your videos please make sure to mention the Model and creator -Lina(2.1) by MrLwitwma [Mr(Mister), Lwitwma(Lwi-tw-ma)]
 Original Owner/ Creators: MrLwitwma
 Model: Lina(2.1)
---
'''



from flask import Flask, render_template, request, jsonify, redirect
from training import lina_respond

model = "<b>Lina</b><br>"
app = Flask(__name__)

 #Main Page
@app.route('/')
def home():
    return render_template('index.html')

 #Lina's user feedback
@app.route('/feedback/')
def index():
    return render_template('feedback.html')
@app.route('/submit', methods=['POST'])
def submit_feedback():
    name = request.form.get('name')
    email = request.form.get('email')
    feedback = request.form.get('feedback')
    if feedback:
        with open('feedback.txt', 'a') as f:
            f.write(f"Name: {name}\n")
            f.write(f"Email: {email}\n")
            f.write(f"Feedback: {feedback}\n")
            f.write("-" * 30 + "\n")
    return redirect('/')

 #Custom 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

 #Send response to user input
@app.route('/get_response', methods=['POST'])
def get_response():
    user_task = request.form['user_input']
    userId = request.form['user_id']
    user_input = user_task.lower()
    response = lina_respond(user_input, userId)
    return jsonify({"response":model + response })


if __name__ == '__main__':
    app.run(debug=True)