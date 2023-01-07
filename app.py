from flask import Flask
from flask import render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("home.html")  
@app.route('/primitive')
def primitive():
    return render_template("primitive.html")  
@app.route('/primitive',methods=['POST'])
def myres():
    text1=int(request.form['num'])
    from math import sqrt
    def isPrime( n):	
        if (n <= 1):
            return False
        if (n <= 3):
            return True        
        if (n % 2 == 0 or n % 3 == 0):
            return False
        i = 5
        while(i * i <= n):
            if (n % i == 0 or n % (i + 2) == 0) :
                return False
            i = i + 6
        return True
    def power( x, y, p):
        res = 1 
        x = x % p 
        while (y > 0):       
            if (y & 1):
                res = (res * x) % p           
            y = y >> 1 
            x = (x * x) % p
        return res
    def findPrimefactors(s, n) :      
        while (n % 2 == 0) :
            s.add(2)
            n = n // 2        
        for i in range(3, int(sqrt(n)), 2):          
            while (n % i == 0) :
                s.add(i)
                n = n // i        
        if (n > 2) :
            s.add(n)
    def findPrimitive( n) :
        s = set()
        if (isPrime(n) == False):
            return -1        
        phi = n - 1        
        findPrimefactors(s, phi)        
        for r in range(2, phi + 1):
            flag = False
            for it in s:                
                if (power(r, phi // it, n) == 1):
                    flag = True
                    break                           
            if (flag == False):
                return r        
        return -1
    return render_template("primitive.html",res=str(findPrimitive(text1)))    
@app.route('/fast')
def fast():
    return render_template("fast.html")  
@app.route('/fast',methods=['POST'])
def my():
    b=int(request.form['b'])
    e=int(request.form['e'])
    m=int(request.form['m'])
    def FastModularExponentiation(b, k, m):
        return pow(b, k, m)
    return render_template("fast.html",res=str(FastModularExponentiation(b,e,m)))    
@app.route('/chinease')
def chinese():
    return render_template("chinease.html")
@app.route('/chinease',methods=['POST'])  
def reminder():
    a=str(request.form['a'])
    m=str(request.form['m'])
    a1=a.split("-")
    m1=m.split("-")
    a1 = [int(i) for i in a1]
    m1=[int(i) for i in m1]
    from functools import reduce
    def chinese_remainder(n, a):
        sum = 0
        prod = reduce(lambda a, b: a*b, n)
        for n_i, a_i in zip(n, a):
            p = prod // n_i
            sum += a_i * mul_inv(p, n_i) * p
        return sum % prod
    def mul_inv(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1: return 1
        while a > 1:
            q = a // b
            a, b = b, a%b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0: x1 += b0
        return x1
    return render_template("chinease.html",res=str(chinese_remainder(m1,a1)))
@app.route('/shift')
def shift():
    return render_template("swift.html")
@app.route('/shift',methods=["POST"])
def cipher():
    text=request.form['txt']
    key=int(request.form['key'])
    def encypt_func(txt, s):  
        result = ""  
        for i in range(len(txt)):  
            char = txt[i]            
            if (char.isupper()):  
                result += chr((ord(char) + s - 65) % 26 + 65)  
            else:  
                result += chr((ord(char) + s - 97) % 26 + 97)  
        return result 
    return render_template("swift.html",res=encypt_func(text,key))
@app.route('/additive')
def add():
    return render_template("additive.html")
@app.route('/additive',methods=["POST"])
def ad():
    a=int(request.form['a'])
    m=int(request.form['m'])
    def addInverse(A, M):
        for X in range(0, M):
            if (((A % M) + (X % M)) % M == 0):
                return X
        return -1
    return render_template("additive.html",res=addInverse(a,m))