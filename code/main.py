from flask import Flask,render_template,request
import pickle

app= Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/udp.html')
def udp():
    return  render_template('udp.html')

@app.route('/icmp.html')
def icmp():
    return  render_template('icmp.html')

@app.route('/attack.html')
def attack():
    return  render_template('attack.html')

@app.route('/tcp.html')
def tcp():
    return  render_template('tcp.html')

@app.route('/udp_validation',methods=['POST'])
def udp_validate():
    if request.method == 'POST':
        p1=request.form.get('p1')
        p2 = request.form.get('p2')
        p3 = request.form.get('p3')
        p4 = request.form.get('p4')
        p5 = request.form.get('p5')
        val=udp_test([p1,p2,p3,p4,p5])
        print(val)
        if(val==1):
            return render_template('attack.html')
        else:
            return  render_template('normal.html')

def udp_test(attribute):
    model = pickle.load(open("./saved_model/tcp_syn_data.sav", 'rb'))
    result = model.predict([attribute])
    print(type(result))
    print(result[0])
    num=result[0]
    return num


@app.route('/tcp_validation',methods=['POST'])
def tcp_validate():
    if request.method == 'POST':
        p1=request.form.get('p1')
        p2 = request.form.get('p2')
        p3 = request.form.get('p3')
        p4 = request.form.get('p4')
        p5 = request.form.get('p5')
        val=tcp_syn_test([p1,p2,p3,p4,p5])
        print(val)
        if(val==1):
            return render_template('attack.html')
        else:
            return  render_template('normal.html')

def tcp_syn_test(attributes):
    model = pickle.load(open("./saved_model/tcp_syn_data.sav", 'rb'))
    result1 = model.predict([attributes])
    print(result1)
    num1=result1[0]
    return num1

@app.route('/icmp_validation',methods=['POST'])
def icmp_validate():
    if request.method == 'POST':
        p1=request.form.get('p1')
        p2 = request.form.get('p2')
        p3 = request.form.get('p3')
        p4 = request.form.get('p4')
        p5 = request.form.get('p5')
        p6 = request.form.get('p6')
        p7 = request.form.get('p7')
        val=icmp_test([p1,p2,p3,p4,p5,p6,p7])
        print(val)
        if(val==1):
            return render_template('attack.html')
        else:
            return  render_template('normal.html')

def icmp_test(attributes):
    model = pickle.load(open("./saved_model/icmp_data.sav", 'rb'))
    result2 = model.predict([attributes])
    print(result2)
    num2=result2[0]
    return num2

if __name__=="__main__":
    app.run(debug=True)