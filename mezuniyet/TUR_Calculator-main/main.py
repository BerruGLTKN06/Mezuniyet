# İçe Aktarma
from flask import Flask, render_template, request
import random


app = Flask(__name__)
messages = [
                '''Sera gazları arttıkça küresel sıcaklık da yükseliyor. 2011-2020, kayıtlardaki en sıcak on yıl oldu. 1980'lerden beri her on yıl bir öncekinden daha sıcak geçiyor. Sıcak hava dalgaları ve orman yangınları artıyor. Ayrıca, Arktik bölgesi küresel ortalamadan iki kat daha hızlı ısınıyor.''',
                '''Sıcaklıklar arttıkça daha fazla nem buharlaşıyor, bu da şiddetli yağışlar ve yıkıcı fırtınalara yol açıyor. Tropikal fırtınalar, siklonlar ve kasırgalar, ısınan okyanus sularıyla daha güçlü hale geliyor. Bu fırtınalar, evleri ve toplulukları yok ederek can kaybına hatta büyük ekonomik zararlara neden oluyor.''',
                '''İklim değişikliği, su kaynaklarını azaltarak kuraklığı artırıyor. Su sıkıntısı çeken bölgelerde durum daha da kötüleşiyor. Tarımsal kuraklık, mahsulleri tehdit ederken, ekolojik kuraklık ekosistemleri zorluyor. Kum ve toz fırtınaları artıyor, çöller genişliyor ve tarım arazileri azalıyor. Birçok insan, yeterli suya erişememe riskiyle karşı karşıya.''',
                '''İklim değişikliği, türlerin hayatta kalmasını tehdit ediyor. Sıcaklıklar arttıkça riskler büyüyor ve tür kaybı hızlanıyor. Önümüzdeki on yıllarda bir milyon tür yok olma tehlikesiyle karşı karşıya. Orman yangınları, aşırı hava olayları ve istilacı türler bu süreci hızlandırıyor. Bazı türler uyum sağlayabilirken, birçoğu yok olacak.''',
                '''Yoksulluk ve yerinden edilme İklim değişikliği insanları yoksulluğa sürükleyen ve yoksulluğu sürdüren faktörleri artırır. Sel baskınları kentsel gecekondu mahallelerini süpürebilir, evleri ve geçim kaynaklarını yok edebilir. Sıcaklık, açık hava işlerinde çalışmayı zorlaştırabilir. Su kıtlığı mahsulleri etkileyebilir. Geçtiğimiz on yılda (2010-2019), hava olaylarından kaynaklanan olaylar her yıl ortalama 23,1 milyon insanı yerinden etti ve çok daha fazlasını yoksulluğa karşı savunmasız bıraktı. Mültecilerin çoğu, iklim değişikliğinin etkilerine uyum sağlamaya en savunmasız ve en az hazır ülkelerden geliyor.''' 
                    ]

@app.route('/su222')
def facts():
    return f'<p>{random.choice(messages)}</p>'


def result_calculate(size, lights, device):
    # Elektrikli cihazların enerji tüketimini hesaplamaya olanak tanıyan değişkenler
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 




@app.route('/')
def index():
    return render_template('index.html')
# İkinci sayfa
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# Üçüncü sayfa
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',                           
                            size = size, 
                            lights = lights                           
                           )

# Hesaplama
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )
# Form
@app.route('/form')
def form():
    return render_template('form.html')

#Formun sonuçları


@app.route('/submit', methods=['POST'])
def submit_form():
    # Veri toplama için değişkenleri tanımlayın
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    date = request.form['date']
    gender = request.form['gender']

    # Verilerinizi kaydedebilir veya e-posta ile gönderebilirsiniz
    return render_template('form_result.html', 
                           # Değişkenleri buraya yerleştirin
                           name=name,
                           email=email,
                           address=address,
                           date=date,
                           gender=gender,

                           )

app.run(debug=True)
