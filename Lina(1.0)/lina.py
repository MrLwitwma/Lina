from flask import Flask, render_template, request, jsonify
import random
import wikipedia
from responses import lina_responses

app = Flask(__name__)

def generate_response(input_text):
    responses=lina_responses
    if input_text in responses:
        return random.choice(responses[input_text])
    else:
        try:
            page_summary = wikipedia.summary(input_text)
            return f"I'm sorry, I don't have that information, but here's what I found: {page_summary}"
        except wikipedia.exceptions.DisambiguationError as e:
            # Handle disambiguation errors, where Wikipedia is unsure of the topic
            options = e.options[:5]  # Display the first 5 suggestions
            return f"I'm not sure which topic you mean. Here are some options: {', '.join(options)}"
        except:
            return "Sorry I don't have any data based on your input"
  #maths
def maths(input):
       expression=input.replace("add", "").replace("sustract", "").replace("multiply", "").replace("divide", "").replace("what is", "")
       if ("+(" not in input and "-(" not in input and "/(" not in input and "%(" not in input and "//(" not in input and  "**(" not in input and  "+(" not in input and "*(" not in input) and ("(" in input):
           expression=input.replace("(", "*(")
       try:          
          result = eval(expression)
          response=f"The answer is {result}"
       except (SyntaxError, NameError,):
          response='Invalid input. Please enter a valid arithmetic expression.'
       return response
  # decimal base to binary base(2)
def decimal_to_binary(input):
    decimal_num=input.replace('what is','').replace('in binary','')
    last_num=""
    try:
        decimal_num=int(decimal_num)
        my_decimal=str(decimal_num)
        while True:
            binary_num1=decimal_num//2
            binary_num2=decimal_num%2
            decimal_num=binary_num1
            last_num=str(binary_num2) + str(last_num)
            if binary_num1<=0:
                break
        response=my_decimal + " in binary is " + last_num
    except:
        response="Error coverting decimal to binary please enter a numeral"
    return response
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input ='User:'
    user_input = request.form['user_input']
    user_input = user_input.lower().rstrip(" ").rstrip(".").rstrip("!").rstrip("?")
    user_input = user_input.replace(" u ", " you ").replace(" r ", " are ")
    if ("+" in user_input or "-" in user_input or "/" in user_input or "*" in user_input or "**" in user_input or "%" in user_input or "//" in user_input):
        response = maths(user_input)
    elif "what is" in user_input and "in binary" in user_input or "in binary" in user_input:
        response = decimal_to_binary(user_input)
    else:
        response = generate_response(user_input)
    return jsonify({"response": "Lina: " + response})


if __name__ == '__main__':
    app.run(debug=True)