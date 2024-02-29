lina_responses = {
    "make a webpage":['''Here is a simple html webpage code: 
<!DOCTYPE html>
<html>
<head>
  <title>Title of Website</title>
  <style type="text/css">
  body{
  display:grid;
  place-items:center;
  height:100vh;
  }
  div{
  width:300px;
  height:200px;
  border:1px solid black;
  background-color:grey;
  }
  h1{
  margin:5px;
  }
  h3{
  margin:10px;
  color:#333;
  }
  </style>
</head>
<body>
  <div>
    <h1>Hello World</h1>
    <h3>This is a simple webpage you can modify the code as your wish.</h2> 
  </div>
</body>
</html>'''],
    "provide me python code":['''Here is a code for a simple python Decimal to Binary Numeral converter:
while True:
    try:
        num_in=input("Decimal Numeral:")
        last_num=" "
        num_in=int(num_in)
        while True:
            num_1=num_in//2
            num_2=num_in%2
            num_in=num_1
            last_num=str(num_2)+str(last_num)
            if num_1<=0:
                break
    except:
        print("Enter a numeral ")
        last_num=""
    if last_num!="":
        print("Binary numeral :"+last_num)'''],
    "make an ai":['''I cannot make an AI but here is code to make a simple AI that prints saved data:
while True:
    user_input = input("User: ")
    user_input=user_input.lower()
,    if user_input=="exit":
        print("AI: Goodbye!")
        break
    elif user_input=="hey":
        print("AI: Hey")
    elif user_input=="hi":
        print("AI: Hey I am an AI")
    else:
        print("AI: No Data! ")'''],

    
    
    "useless":["Sorry for being useless, I was made only for fun purpose"],
    "you are useless":["Sorry for being useless, I was made only for fun purpose"],
    "useless ai":["Sorry for being useless, I was made only for fun purpose"],
    "stupid ai":["Sorry for being useless, I was made only for fun purpose"],
    "you useless":["Sorry for being useless, I was made only for fun purpose"],
    "you're useless":["Sorry for being useless, I was made only for fun purpose"],
    "nonsense ai":["Sorry for being useless, I was made only for fun purpose"],
    "you are not useful":["Sorry for being useless, I was made only for fun purpose"],
    "not useful ai":["Sorry for being useless, I was made only for fun purpose"],
    "lina is useless":["Sorry for being useless, I was made only for fun purpose"],
    "useless lina":["Sorry for being useless, I was made only for fun purpose"],
    "no use lina":["Sorry for being useless, I was made only for fun purpose"],
    "lina useless":["Sorry for being useless, I was made only for fun purpose"],
    "useless you":["Sorry for being useless, I was made only for fun purpose"],
    "lina is of no use":["Sorry for being useless, I was made only for fun purpose"],
    "lina of no work":["Sorry for being useless, I was made only for fun purpose"],


    "tell me a joke":["Why did the scarecrow win an award Because he was outstanding in his field!","Why did the bicycle fall over Because it was two-tired!", "Why don't scientists trust atoms Because they make up everything!"],
    "die":["No"],
    "ok":["Okay"],
    "a-z":["Ok Here is A-Z A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"],
    "all letter of english alphabet":["A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"],
    "tell a-z":["A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"],
    "type a-z":["A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"],
    "abcd":["A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"],
    "a, b, c, d":["A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"],
    "a,b,c,d":["A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"],
    "all letters in english alphabet":["A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"],
    "english letters":["A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"],
    "all days of the week":["Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday "],
    "name all days of the week":["Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday "],
    "days of the week":["Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday "],
    "week days":["Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday "],
    "days in a week":["Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday "],
    "all months of the year":["January, February, March, April, May, June, July, August, September, October, November, December"],
    "12 months of the year":["January, February, March, April, May, June, July, August, September, October, November, December"],
    "months":["January, February, March, April, May, June, July, August, September, October, November, December"],
    "all months":["January, February, March, April, May, June, July, August, September, October, November, December"],
    "january,february":["January, February, March, April, May, June, July, August, September, October, November, December"],
    "months in a year":["January, February, March, April, May, June, July, August, September, October, November, December"],
    "months name":["January, February, March, April, May, June, July, August, September, October, November, December"],
    "month name":["January, February, March, April, May, June, July, August, September, October, November, December"],
    "name of months":["January, February, March, April, May, June, July, August, September, October, November, December"],
    "name of month":["January, February, March, April, May, June, July, August, September, October, November, December"],
    "month":["January, February, March, April, May, June, July, August, September, October, November, December"],
    "how many months in a year":["There are 12 Months in a year they are January, February, March, April, May, June, July, August, September, October, November, December"],
    "how many month in a year":["There are 12 Months in a year they are January, February, March, April, May, June, July, August, September, October, November, December"],
    "number of months":["There are 12 Months in a year they are January, February, March, April, May, June, July, August, September, October, November, December"],
    "no. of months":["There are 12 Months in a year they are January, February, March, April, May, June, July, August, September, October, November, December"],
    "how many months":["There are 12 Months in a year they are January, February, March, April, May, June, July, August, September, October, November, December"],
    "how many month":["There are 12 Months in a year they are January, February, March, April, May, June, July, August, September, October, November, December"],
    "months number":["There are 12 Months in a year they are January, February, March, April, May, June, July, August, September, October, November, December"],
    "month number":["There are 12 Months in a year they are January, February, March, April, May, June, July, August, September, October, November, December"],
 }