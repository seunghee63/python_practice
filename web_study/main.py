from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# @app.route('/')
# def helloWorld():
#     return 'Hello, World'

# @app.route('/name')
# def helloName():
#     return 'Hello,name'

# @app.route('/name/<name>')
# def helloName(name):
#     return 'Hello,%s!' % name

@app.route('/<int:number>')
def helloName(number):
    return "It's %d" % number

@app.route('/')
def helloWorld():
    return render_template('hello.html')

@app.route('/score')
def score():
    return render_template('score.html')  

#요청은 request.form에 다 담김!
@app.route('/result', methods=['GET','POST'])
def result():
    if request.method == 'GET': #입력값 없이 바로 주소쳐서 넘어갔을 경우
        return "It's GET"
    
    return render_template('result.html',result = request.form)  
    #return (jsonify(request.form))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5000)