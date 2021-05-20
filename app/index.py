from flask import Flask

app = Flask(__name__)


@app.route('/')
def factorial(n):
     
    # single line to find factorial
    return 1 if (n==1 or n==0) else n * factorial(n - 1);
 
# Driver Code
num = 5;
print("Factorial of",num,"is",
factorial(num))!"


app.run(host='0.0.0.0', port=5000)
