import random
from data import *
import math
import re

# from textblob import TextBlob



 #Chooses the best response type
def lina_respond(input, userId):
    num_in_ = hasnum(input)
    store_input(input, userId, file='inputs')
    try:
         #Lina can find percentage
        if ("percentage" in input or "%" in input) and "of" in input:
            response = percentage(input)
         #Lina can do maths
        elif ("+" in input or "-" in input or "/" in input or "*" in input or "**" in input or "%" in input or "//" in input) and num_in_==True:
            response = basic_maths(input)
         #Lina can find log values
        elif "log" in input and num_in_ == True:
            response = find_log(input)
         #Lina can find factorial
        elif "factorial" in input or "!" in input:
            response = factorial(input)
         #Lina can find the largest prime factor
        elif 'prime' in input and ('number' in input or 'factor' in input) and 'largest' in input and hasnum(input) == True:
            response = largest_prime_factor(input)
         #Lina can find the smallest prime factor
        elif 'prime' in input and ('number' in input or 'factor' in input) and 'smallest' in input and hasnum(input) == True:
            response = smallest_prime_factor(input)
         #Lina can find if a number is prime
        elif 'prime' in input and num_in_:
            response = is_prime(input)
         #Lina can find factors of values
        elif 'factor' in input and not 'factorial' in input:
            response = factors(input)
         #Lina can convert roman numeral to decimal
        elif 'decimal' in input and any(char in input for char in 'ivxcdmv̅x̅l̅c̅d̅m̅') and num_in_ == False:
            response = roman_to_decimal(input)
         #Lina can convert decimal numeral to roman
        elif ('roman' in input or 'decimal' in input) and num_in_ == True:
            response = decimal_to_roman(input)
         #Lina can convert base values
        elif ('base' in input or 'binary' in input) and num_in_ == True:
            response = xBase_to_Decimal(input, only_val=False)
         #Lina can find HCf
        elif "hcf" in input and hasnum(input):
            response = find_hcf(input, False)
         #Lina can find LCM
        elif "lcm" in input and hasnum(input):
            response = find_lcm(input, False)
         #Lina can see if input is only digits
        elif input.isdigit():
            response = 'I can see you typed some numbers what am I supposed to do?'
         #Lina can convert numbers to words
        elif hasnum(input) == True and 'word' in input:
            response = num_to_word(input)
        return str(response)
    except Exception as e:
        # return e
        response = lina_response(input)
        return response



#  #Lina can understand human emotion
# def emotion(text):
#     blob = TextBlob(text)
#     sentiment = blob.sentiment.polarity 
#     return sentiment



 #Lina can Respond
def lina_response(input):
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
        return lina_response2(input)
        # return random.choice(responses['default'])

def lina_response2(input):
    max_matches = 0
    best_category = None

    # Iterate through basic responses
    for category, responses_list in list_responses.items():
        matches = sum(word in input for word in category.split())
        if matches > max_matches:
            max_matches = matches
            best_category = category

    set_global_variable(best_category)
    # print(best_category) #***
    if best_category is not None:
        return random.choice(list_responses[best_category])
    
    # If no exact matches, try to find partial matches
    for category, responses_list in list_responses.items():
        if any(word in input for word in category.split()):
            return random.choice(list_responses[category]), best_category

    return 'Sorry I did not understand'



 #Lina Can find factorial
def factorial(input):
    input = filter_input(input, type='number')
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



 #Lina can find if a number is prime
def is_prime(n, k=5):
    n = eval(filter_input(n, type='maths'))
    val_n = n
    if n <= 1:
        return f"No {val_n} is not a prime"
    if n <= 3:
        return f"Yes {val_n} is a prime"
    if n % 2 == 0:
        return f"No {val_n} is not a prime"

    # Write n as (2^r)*d + 1
    r = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return f"No {val_n} is not a prime"
    return f"Yes {val_n} is a prime"



 #Lina can find largest prime number
def largest_prime_factor(in_value):
    in_value = filter_input(in_value, type = 'prime_factor')
    number = in_value
    '''# Get user input for the number
    user_input = int(input("Enter a number: "))
    # Find the largest prime factor
    result = largest_prime_factor(user_input)
    print(f"The largest prime factor of {user_input} is: {result}")'''
     #what is the largest prime number in 98473298742
      #Start with the smallest prime factor
    # if number > 999999999999999999999999:
    #     return f'The prime factor of {number} will be very huge for any computer to calculate'
    factor = 2
    for i in range(1000000):
        if factor * factor <= number:
            if number % factor == 0:
                number //= factor
            else:
                factor += 1
        else:
            return f"The largest prime factor of {in_value} is {number}"
    return f"Value is too large to calculate!"



 #Lina can find the smallest prime factor
def smallest_prime_factor(input):
    in_value = filter_input(input, type = "prime_factor")
    val = in_value
    factor = 2
    if val == 1:
        return "The smallest prime factor of 1 is 1"
    for i in range(1000000):
        if val > 1:
            if val % factor != 0:
                factor = factor + 1
            else:
                return f"The smallest prime factor of {in_value} is {factor}"
    return "Value is too large to calculate!"



 #Lina can find factors of values
def factors(input):
     #What are the factors of 15 "15 = 3*5"
    val = filter_input(input, type = 'factors')
    temp_val = val
    factor = 2
    val_return = ""
    # if val > 999999999:
    #     return "Value is too large to calculate please enter values below 1000000000"
    if val == 1:
        return "The factor of 1 is 1"
    for i in range(100000):
        if val > 1:
            if val % factor != 0:
                factor = factor + 1
            else:
                val = val // factor
                val_return = f"{val_return} * {str(factor)}"
        else:
            return f"The factors of {temp_val} are {val_return.lstrip(' * ')}"
    return f"Value is too large to calculate! The factors of {temp_val} is {val_return.lstrip(' * ')}*{val} (This is a incomple calculation to prevent system resource exhaustion calculation was not completed)"



 #Lina knows maths
def basic_maths(input):
       expression = filter_input(input, type='maths')
       if ("+(" not in input and "-(" not in input and "/(" not in input and "%(" not in input and "//(" not in input and  "**(" not in input and  "+(" not in input and "*(" not in input) and ("(" in input):
           expression = expression.replace("(", "*(")
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
        


 #Lina knows if an input has number
def hasnum(input):
    for char in input:
        if char.isdigit():
            return True
            


 #Lina can find percentage
def percentage(input):
    #what is the value of 22% of 66
    value = filter_input(input, type='percentage')
    try:
        temp_value = value.split("%")
        value_x = temp_value[0]
        value_y = temp_value[1]
        value_y = value_y.replace("of", "")
        return f"{value} is {float(value_x)/100 * float(value_y)}"
    except(ValueError):
        return "Only percentage of numbers can be found!"
    except:
        return "Unable to find percentage! Enter in the form x % of y"
    


 #Required values for cleanup
maths_expressions = {"+", "-", "/", "*", "(", ")", "{", "}", "[", "]", "%", "."}
baseConverter = {'decimal': 10, }
xBase_expression = {'base'}
 #cleans unwanted text
def filter_input(value, type):
    temp_val = ''
    if type == 'number':
        return int(''.join([i + '' for i in value if i.isdigit()]))
    elif type == 'text':
        return int(''.join([i + '' for i in value if i.isalpha()])) #*** Check if errors!
    elif type == 'percentage':
        temp_val = value.split()
        # for i in temp_val:
        #     if '%' in i or i.isdigit() or 'of' in i or ' ' in i:  #Use Modules for cleaner code and fater performance
        #         final_val = final_val + i + ' '
        return ' '.join([i + ' ' for i in temp_val if '%' in i or i.isdigit() or 'of' in i or ' ' in i]).strip()
    elif type == 'prime_factor':
        return int(''.join([i + '' for i in value if i.isdigit()]))
    elif type == "factors":
        return int(''.join([i + '' for i in value if i.isdigit()]))
    elif type == 'logarithm':
         #What is value of log 200!,  what is value of log 200 base 20, find value of log 200 where base is 20
        default_base = 10
        temp_val = value.split()
        filtered_val = ' '.join([i + '' for i in temp_val if i.isdigit() or "log" in i or "base" in i])
         #log 200 base 200
        try:
            temp_val = filtered_val.split("base")
            log = float(temp_val[0].replace("log",""))
            base = float(temp_val[1])
        except:
            base = 10
            log = float(filtered_val.replace("log",""))
        return log, base
    elif type == 'maths':
        expression = ''.join([i + '' for i in value if i.isdigit() or i in maths_expressions])
        return expression
        # expression = input.replace("add", "").replace("sustract", "").replace("multiply", "").replace("divide", "").replace("what is", "").replace("=","").replace("?","").replace("by", "/").replace("find out", "")
     #***
    elif type == 'get_decimal':
         #What is 22 base 5 in decimal
        #what is 100 base 2 in decimal, what is 100 in decimal, 100 base 2 in decimal, 100 base 4 in base 10, find the value of 100 base 2
        temp_val = value.split('base')
        xbase_val = temp_val[0]
        base = temp_val[1]
        try:
            xbase_val = int(''.join([i + '' for i in xbase_val if i.isdigit()]))
            base = int(''.join([i + '' for i in base if i.isdigit()]))
        except:
            return 'Error'
        return xbase_val, base
    # What is 22 base 2 in base 2
    elif type == 'xBase_to_yBase':
        temporary = value.split(" ")
        # print(temporary) #***
        temp_val = ''.join([i + '' for i in temporary if i.isdigit() or 'base' in i])
        # print(temp_val) #***
        # Regular expression pattern to match the value, xBase, and yBase
        pattern = r"(\d+)base(\d+)base(\d+)"
        # Match the pattern in the string
        match = re.match(pattern, temp_val)
        if match:
            # Extract the matched groups
            return_val = match.group(1)
            xBase = match.group(2)
            yBase = match.group(3)
        return int(return_val), int(xBase), int(yBase)
    elif type == 'roman':
        if type == 'roman':
            # Regular expression pattern to match Roman numerals
            pattern = r'\b[IVXLCDMV̅X̅L̅C̅D̅M̅]+\b'
            matches = re.findall(pattern, value.upper())
            if matches:
                return matches[0]
            else:
                return None
        else:
            return None
    elif type == "2val":
        # Find the HCF of 1000, 2000
        val1, val2 = 0, 1
        length = len(value)-1
        for index, i in enumerate(value):
            if i.isdigit():
                temp_val += i
            if temp_val.isdigit() and (i.isdigit() == False or index==length):
                if val1 != 0:
                    val2 = temp_val
                else:
                    val1 = temp_val
                    temp_val = ''
        return int(val1), int(val2)



 #Lina can find logarithm
def find_log(input):
    value, base = filter_input(input, type = "logarithm")
    try:
        result = math.log(value, base)
    except(ZeroDivisionError) as e:
        return f'Please enter a valid value {e} error!'
    except Exception as e:
        return f'Please enter a valid value "Error Type: {e}"'
    return f"The value of log{value} base{base} is {result}"
    


 #Lina can convert any base to decimal base
def xBase_to_Decimal(input, only_val):
    if input.count('base') == 2:
        return xBase_to_yBase(input, False)
    #what is 100 base 2 in decimal, what is 100 in decimal, 100 base 2 in decimal, 100 base 4 in base 10, find the value of 100 base 2
    val, my_base = filter_input(input, type='get_decimal')
    try:
        # my_base = int(base[1])
        # val = int(base[0])
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
                if only_val:
                    return int(temp_val)
                else:
                    return f"{error}The answer in decimal base is {temp_val}"
    except:
        try:
            return xBase_to_yBase(input, False)
        except:
            return "An Error occured!"



 #Lina Can convert any base to any base
def xBase_to_yBase(input, only_val):
    # 100 base 5 in base 2 => 100,5,2
    value, xBase, yBase= filter_input(input, type='xBase_to_yBase')
    decimal_val = xBase_to_Decimal(f'{value} in base {xBase}', only_val=True)
    # 100 base 5 in base 2 => 25 in base 2 => 25, 2
    temp_val = ''
    try:
        while True:
            temp_val = str(decimal_val % yBase) + temp_val
            decimal_val //= yBase
            if decimal_val == 0:
                if only_val:
                    return int(temp_val)
                else:
                    return f'{value} base {xBase} in base {yBase} is {temp_val}'
    except Exception as e:
        print(e)



 #Lina can convert roman to decimal
def roman_to_decimal(input):
    roman = filter_input(input, type='roman')
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'V̅': 5000, 'X̅':10000, 'L̅': 50000, 'C̅': 100000, 'D̅': 500000, 'M̅': 1000000}
    decimal = 0
    prev_value = 0
    
    try:
        for numeral in reversed(roman):
            value = roman_numerals[numeral]
            if value < prev_value:
                decimal -= value
            else:
                decimal += value
            prev_value = value
    except:
        return "Your Input contains Roman Symbols that my System can't process"

     #V̅X̅L̅C̅D̅M̅
    invalid_sequences = ['IIII', 'VV', 'XXXX', 'LL', 'CCCC', 'DD', 'MMMM', 'V̅V̅', 'X̅X̅X̅', 'L̅L̅', 'C̅C̅C̅C̅', 'D̅D̅', 'M̅M̅M̅M̅',
                         'IXX', 'IL', 'IC', 'ID', 'IC', 'IM', 'IV̅', 'IX̅', 'IL̅', 'IC̅', 'ID̅', 'IM̅',
                         'VX', 'VL', 'VC', 'VD', 'VC', 'VM', 'VV̅', 'VX̅', 'VL̅', 'VC̅', 'VD̅', 'VM̅',
                         'XXL', 'XXC', 'XD', 'XM', 'XV̅', 'XL̅', 'XC̅', 'XD̅', 'XM̅',
                         'LC', 'LD', 'LC', 'LM', 'LV̅', 'LX̅', 'LL̅', 'LC̅', 'LD̅', 'LM̅',
                         'CCM', 'CCX̅', 'CV̅', 'CX̅', 'CL̅', 'CC̅', 'CD̅', 'CM̅',
                         'DM', 'DV̅', 'DX̅', 'DL̅', 'DC̅', 'DD̅', 'DM̅',
                         'MMX̅', 'ML̅', 'MC̅', 'MD̅', 'MM̅',
                         'X̅X̅L̅', 'MC̅', 'MD̅', 'MM̅',
                         ]
    for seq in invalid_sequences:
        if seq in roman:
            return f"It is an Invalid Roman numeral! but to satisfy you the answer is {decimal}"
    return f'{roman} in decimal  is {decimal}'


 #Lina can convert decimal values to roman values 
def decimal_to_roman(input):
    input = filter_input(input, type='number')
    temp_val = input
    # 1231 in roman
    # MCCXXXI
    return_value = ''
    if input == 0:
        return "In Roman numerals, there isn't a symbol for zero"
    while True:
        if int(input) > 3999999:
            return 'Value is above Limit!!'
        elif int(input) / 1000000 >= 1:
            input -= 1000000
            return_value += "M" + "\u0305"
        elif int(input) / 900000 >= 1:
            input -= 900000 
            return_value += "C" + "\u0305" + "M" + "\u0305"
        elif int(input) / 500000 >= 1:
            input -= 500000
            return_value += "D" + "\u0305"
        elif int(input) / 400000 >= 1:
            input -= 400000 
            return_value += "C" + "\u0305" + "D" + "\u0305"
        elif int(input) / 100000 >= 1:
            input -= 100000
            return_value += "C" + "\u0305"
        elif int(input) / 90000 >= 1:
            input -= 90000
            return_value += "X" + "\u0305" + "C" + "\u0305"
        elif int(input) / 50000 >= 1:
            input -= 50000
            return_value += "L" + "\u0305"
        elif int(input) / 40000 >= 1:
            input -= 40000
            return_value += "X" + "\u0305" + "L" + "\u0305"
        elif int(input) / 10000 >= 1:
            input -= 10000
            return_value += "X" + "\u0305"
        elif int(input) / 9000 >= 1:
            input -= 9000
            return_value += "M" + "X" + "\u0305"
        elif int(input) / 5000 >= 1:
            input -= 5000
            return_value += "V" + "\u0305"
        elif int(input) / 4000 >= 1:
            input -= 4000
            return_value += "M" + "V" + "\u0305"
        elif int(input) / 1000 >= 1:
            input -= 1000
            return_value += "M"
        elif int(input) / 900 >= 1:
            input -= 900
            return_value += "CM"
        elif int(input) / 500 >= 1:
            input -= 500
            return_value += "D"
        elif int(input) / 400 >= 1:
            input -= 400
            return_value += "CD"
        elif int(input) / 100 >= 1:
            input -= 100
            return_value += "C"
        elif int(input) / 90 >= 1:
            input -= 90
            return_value += "XC"
        elif int(input) / 50 >= 1:
            input -= 50
            return_value += "L"
        elif int(input) / 40 >= 1:
            input -= 40
            return_value += "XL"
        elif int(input) / 10 >= 1:
            input -= 10
            return_value += "X"
        elif int(input) / 9 >= 1:
            input -= 9
            return_value += "IX"
        elif int(input) / 5 >= 1:
            input -= 5
            return_value += "V"
        elif int(input) / 4 >= 1:
            input -= 4
            return_value += "IV"
        elif int(input) / 1 >= 1:
            input -= 1
            return_value += "I"
        else:
            return f'{temp_val} in roman is {return_value}'



 #Lina can find HCF
def find_hcf(input, onlyNum):
    val_x, val_y = filter_input(input, "2val")
    if val_x > val_y:
        x = val_x
        y = val_y
    else:
        x = val_y
        y = val_x
    for i in range(10000):
        next_y = x%y
        x, y = y, next_y
        
        if next_y == 0 and onlyNum:
            return x
        elif next_y == 0:
            return f'HCF of ({val_x}, {val_y}) is {x}'
    return ValueError('Value was too Large')



 #Lina can find LCM
def find_lcm(input, onlyNum = False):
    x, y = filter_input(input, "2val")
    val = x * y
    return_val = val/find_hcf(input, onlyNum=True)
    if onlyNum:
        return return_val
    return f'Lcm of ({x}, {y}) is {return_val}'



 #Lina can convert Scientific to Numeral (1.1e+1) -> 11
def scientific_to_numeral(scientific_notation):
    if "e" not in scientific_notation:
        return scientific_notation
    # Split the scientific notation into coefficient and exponent parts
    coefficient, exponent = scientific_notation.split('e')
    # Convert coefficient to a float
    coefficient = float(coefficient)
    # Convert exponent to an integer
    exponent = int(exponent)
    # Multiply coefficient by 10 raised to the exponent
    numerical_value = coefficient * (10 ** exponent)
    return str(numerical_value)



 #Lina can change users input number to words
ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
thousands = ['', 'thousand', 'million', 'billion', 'trillion']
def num_to_word(input):
    num = num_input = filter_input(input, type='number')
    if int(num)<0 or int(num)>999999999999999:
        return 'The number is out of range'
    if num == 0:
        return 'zero'
    words = ''
    for i in range(len(thousands)):
        if num % 1000 != 0:
            words = helper(num % 1000) + thousands[i] + ' ' + words
        num //= 1000
    return f'{num_input} in words is {words.strip()}'
def helper(num):
    if num == 0:
        return ''
    elif num < 10:
        return ones[num] + ' '
    elif num < 20:
        return teens[num - 10] + ' '
    elif num < 100:
        return tens[num // 10] + ' ' + helper(num % 10)
    else:
        return ones[num // 100] + ' hundred ' + helper(num % 100)



 #Stores User Chats for improving future updates
def store_input(input, userId, file):
    with open(f'{file}.txt', 'a', encoding='utf-8') as f:
         f.write(f"{userId}: {input}\n")




#-------------***----------#