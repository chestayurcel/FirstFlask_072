from flask import Flask, render_template, request  

app = Flask(__name__)  

@app.route('/', methods=['GET', 'POST'])  
def index():  
    result = None  
    if request.method == 'POST':  
        # Mengambil data dari form  
        nama = request.form.get('nama')  
        umur = request.form.get('umur')  
        
        # Proses data (contoh sederhana)  
        result = f"Halo {nama}, umur anda adalah {umur} tahun"  
    
    return render_template('index.html', result=result)  

if __name__ == '__main__':  
    app.run(debug=True)