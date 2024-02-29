import random
from flask import Flask, render_template, request, jsonify, redirect
from response import responses, responses2,responses3, responses4, responses5, responses6

app = Flask(__name__)

#Lina V:1.1.0


model="<b>Lina: </b>"
sys="SYS0:"


 #Lina can change any base value to decimal #what is 100 base 2 in decimal
def decimal_it(input):
    input = input.replace("what is","").replace("whatis","").replace("what",'').replace('is','').replace("indecimal","").replace("in decimal","").replace("in","").replace("decimal","")
    # 100 base 5 in decimal
    # [100, 5]
    base = input.split("base")
    try:
        my_base = int(base[1])
        val = int(base[0])
        val_len = len(str(val))
        val_len -= 1
        temp_val = 0
        error = ""
        for i in str(val):
            temp_val = int(i)*my_base**val_len + temp_val
            val_len -= 1
            if int(i) > my_base-1:
                error = "The question seems to be incorrect but "
            if val_len < 0:
                return f"{error}The answer in decimal base is {temp_val}"
    except:
        return "An Error occured!"

 #Lina knows maths
def maths(input):
       expression=input.replace("add", "").replace("sustract", "").replace("multiply", "").replace("divide", "").replace("what is", "").replace("=","").replace("?","").replace("by", "/").replace("find out", "")
       if ("+(" not in input and "-(" not in input and "/(" not in input and "%(" not in input and "//(" not in input and  "**(" not in input and  "+(" not in input and "*(" not in input) and ("(" in input):
           expression=input.replace("(", "*(")
       if "**" in expression:
           return exponent_limit(expression)
       try:          
          result = eval(expression)
          return f"The answer is {result}"
       except (SyntaxError, NameError,):
          return 'Invalid input. Please enter a valid arithmetic expression.'
       except (ZeroDivisionError):
            return "Division by zero cannot be done! anynumber divided by zero is undefined"

#Lina knows to keep exponentiation in limit
def exponent_limit(input):
        try:
            value = input.split("**")
            side1 = eval(value[0])
            side2 = eval(value[1])
            if side1 == 1 or side1 == 0 or side2 == 1 or side2 == 0:
                return f"The answer is {side1 ** side2}"
            try:
                side3 = eval(value[2])
                if side3 <= 9999:
                    side2 = side2**side3
                elif side3 >= 10000:
                    return "Error! Value is too large"
            except:
                pass
            if side1 >= 1000000000 or side2 >= 10000 or side1 <= -1000000000 or side2 <=-10000:
                return "Error! Value is above Limit"
            else:
                temp_val = str(side1) + "**" + str(side2)
                return f"{temp_val} is {side1**side2}"
        except(ValueError):
            return "Error! Value more than limit"
        except:
             return "Error! while calculating value"
             
 #Lina can convert bases
def decimal_to_binary(input):
    decimal_num=input.replace('what is','').replace('in binary','').replace("in base 2","").replace("in base two","").replace("find out", "")
    my_decimal=str(decimal_num)
    last_num=""
    temp_val = ""
    try:
        if ("+" in input or "-" in input or "/" in input or "*" in input or "**" in input or "%" in input or "//" in input):
            if "**" in input:
                decimal_num= exponent_limit(decimal_num)
                if "Error!" not in decimal_num:
                    temp_val = decimal_num.split("is")
                    decimal_num = temp_val[1]
                    temp_val = ""
                else:
                    return "Error! the value is too large" 
            decimal_num=eval(decimal_num)
            my_decimal=str(decimal_num)
            decimal_num=str(decimal_num)
            if "-" in decimal_num:
                decimal_num=decimal_num.lstrip("-")
                temp_val = "-"
        while True:
            decimal_num=int(decimal_num)
            binary_num1=decimal_num//2
            binary_num2=decimal_num%2
            decimal_num=binary_num1
            last_num=str(binary_num2) + str(last_num)
            if binary_num1<=0:
                break
        my_decimal = my_decimal.rstrip(" ").lstrip(" ")
        response=f"{my_decimal} in binary is {temp_val}{last_num}"
    except:
        response="Error coverting decimal to binary please enter a numeral"
    return response

 #Lina can find percentage
def percentage(input):
    try:
        temp_value = input.split("%")
        print(input)
        value_x = temp_value[0]
        value_y = temp_value[1]
        value_y = value_y.replace("of", "")
        return f"{input} is {float(value_x)/100 * float(value_y)}"
    except(ValueError):
        return "Only percentage of numbers can be found!"
    except:
        return "Unable to find percentage! Enter in the form x % of y"

 #Lina Can find factorial
def factorial(input):
    input = int(input.replace("what is", "").replace("find out","").replace("!","").replace("factorial","").replace("of","").replace("!",""))
    if input == 0:
        return "The Value of factorial of 0 or 0! is 1"
    elif input>1500:
        return "Sorry The Value is above my limit my limit is 1500"
    else:
        temp_val = 1
        factorial = int(input)
        while factorial>0:
            temp_val = factorial*temp_val
            factorial -= 1
            if factorial<=1:
                return f"The answer is {temp_val}"

 #Lina can change Roman numbers to decimal
def roman_to_decimal(input):
    input = input.replace("what","").replace("is","").replace("find","").replace("the","").replace("value","").replace("of","").replace("out","").replace("in","").replace("roman","").replace("decimal","").replace('convert', "")
    temp_val = ""
    for char in input:
        if "i" in char or "v" in char or "x" in char or "l" in char or "c" in char or "d" in char or "m" in char:
            temp_val += char
    if "xxxx" in input or "iiii" in input or "IXV" in input or "vv" in input or "ivi" in input or "iiv" in input or "ixi" in input or "iix" in input or "ll" in input or "il" in input or "vl" in input  or "xxl" in  input or "cccc" in input or "lc" in input or "xxc" in input or "vc" in input or "ic" in input or "xcx" in input or "xd" in input or "id" in input or "vd" in input or "dd" in input or "cdc" in input or "ld" in input or "im" in input or "vm" in input or "xm" in input or "lm" in input or "cmc" in input or "mmmm" in input or "dm" in input or "cxcc" in input or "ixx" in input or "cmd" in input:
        return f'The value you provided "{temp_val.upper()}" is in incorrect Roman Numeral Form please provide the correct form to convert to decimal'
    val_decimal = temp_val.replace("cm","900+").replace("m","1000+").replace("cd","400+").replace("d","500+").replace("xc","90+").replace("c","100+").replace("XL","40+").replace("l","50+").replace("ix","9+").replace("x","10+").replace("iv","4+").replace("v","5+").replace("iii","3+").replace("ii","2+").replace("i","1+")#3989 limit for now
    temp_val = f'The value of {temp_val.upper()} in decimal is {eval(val_decimal.rstrip("+"))}'
    return temp_val

 #Lina can respond
def lina_respond(input):
    if input in responses: #basic responses
        return random.choice(responses[input])
    elif input in responses2: #AI based
        return random.choice(responses2[input])
    elif input in responses3: #coding based
        return random.choice(responses3[input])
    elif input in responses4: #maths based
        return random.choice(responses4[input])
    elif input in responses5: #famous people
        return random.choice(responses5[input])
    elif input in responses6: #codes based
        return random.choice(responses6[input])
    else:
        return random.choice(responses['default'])

 #Lina knows if an input has number
def hasnum(input):
    for char in input:
            if char.isdigit():
                return True


#Flask Work


@app.route('/')
def home():
    return render_template('index.html')

 #Lina's About
@app.route('/about/')
def about():
    return render_template('/about/index.html')

 #Lina's user feedback
@app.route('/feedback/')
def index():
    return render_template('/feedback/index.html') #If error opening feedback change to "/feedback/index.html"
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


 #Main Response Systsem
@app.route('/get_response', methods=['POST'])
def get_response():
    user_task=request.form['user_input']
    print("User input:",user_task)#***
    user_input=user_task.lower().rstrip(" ").rstrip(".").rstrip("?")
    user_input=user_input.replace("what's", "what is").replace("'ve "," have ").replace("'ll ", "will ").replace("you're", "you are")
    num_in_ = hasnum(user_input) #check if input has numbers
   #Lina Can Find Factorial
    if "!" in user_input or "factorial" in user_input or "factorial of" in user_input:
        try:
            temp_val = user_input
            response = factorial(temp_val)
            return jsonify({"response": model + response})
        except:
            user_input = user_input.rstrip("!")
   #Lina can change any base to decimal
    if "log" not in user_input and  ("base" in user_input) and (user_input or "in decimal" in user_input or "in base 10" in user_input or "indecimal" in user_input or "inbase10" in user_input):
        response = decimal_it(user_input)
   #Lina convert base10 to base2
    elif ("what is" in user_input and "in binary" in user_input) or ("what is" in user_input and ("in base 2" in user_input or "base two" in user_input)) or "in binary" in user_input or "in base 2" in user_input or "in base two" in user_input:
        response = decimal_to_binary(user_input)
    #Lina can find percentage
    elif "% of" in user_input or "%of" in user_input:
        user_input = user_input.replace("find out", "").replace("what is", "")
        response = percentage(user_input)
   #Lina do maths
    elif ("+" in user_input or "-" in user_input or "/" in user_input or "*" in user_input or "**" in user_input or "%" in user_input or "//" in user_input) and num_in_==True:
        response = maths(user_input)
   #Lina can chanage roman numbers to decimal
    elif "log" not in user_input and  ("convert" in user_input or "find" in user_input or "what" in user_input) and ("roman" in user_input or "decimal" in user_input or "value" in user_input) and ("i" in user_input or "v" in user_input or "x" in user_input or "l" in user_input or "c" in user_input or "d" in user_input or "m" in user_input):
        response = roman_to_decimal(user_input)
    else:
        response=lina_respond(user_input)
    return jsonify({"response":model + response})

    
if __name__=="__main__":
    app.run(debug=True, port=8080)