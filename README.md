# Müşteri Segmentasyon Projesi

Bu proje, müşteri hareketlerini istatistiksel olarak incelemek ve müşteri segmentasyonu yapmak amacıyla geliştirilmiştir. Kullanıcı davranışları, harcamalar ve diğer demografik verilerle müşteriler farklı segmentlere ayrılmaktadır.

## Teknolojiler
Segmentasyon için kullanılan teknolojiler:

*KMeans Clustering:* Müşteriler, KMeans algoritması kullanılarak segmentlere ayrılmaktadır. Bu algoritma, verilerin kümelenmesini sağlar ve müşterilerin benzer özelliklere sahip gruplarda toplanmasını mümkün kılar.
Görselleştirme için kullanılan teknolojiler:

*Dash:* Kullanıcı arayüzü oluşturulmuş ve görselleştirmeler Dash framework'ü kullanılarak yapılmıştır.
*Plotly:* Dinamik grafiklerin oluşturulmasında ve görselleştirmelerde Plotly kütüphanesi kullanılmıştır.

## Kurulum
Projenin gereksinimlerini yüklemek ve Docker ile çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

### 1. GitHub'dan Projeyi Klonlayın
İlk olarak, projeyi GitHub'dan indirmeniz gerekecek. Bunun için aşağıdaki komutu kullanarak projeyi klonlayın:

"git clone https://github.com/eliften/chippin_task.git"

"cd chippin_task"
### 2. Docker ile Kurulum
Proje, Docker kullanılarak kurulup çalıştırılabilir. Bunun için aşağıdaki adımları izleyin:

Docker'ı yükleyin: Docker'ı yüklemek için Docker İndirme Sayfası üzerinden uygun sürümü indirin ve yükleyin.

Proje klasörüne gidin:



"cd /path/to/your/cloned/project"

Docker imajını oluşturun: Proje klasöründe Dockerfile ve gerekli diğer dosyalar bulunduğundan, aşağıdaki komut ile Docker imajını oluşturabilirsiniz:

"docker build -t customer-segmentation ."

Docker konteynerini çalıştırın: Docker imajını oluşturduktan sonra, konteyneri çalıştırmak için şu komutu kullanın:

"docker run -p 8050:8050 customer-segmentation"

Bu komut, uygulamanın Docker konteynerinde çalışmasını sağlar ve uygulama http://localhost:8050 adresinde erişilebilir olacaktır.

"/statistics" endpointi ile veri setinin genel  istatistiklerini, "/predictions" endpointi ile  segmentasyon çıktılarını görüntüleyip export edebilirsiniz.

### 3. Dockerfile Yapılandırması
Projenizin Dockerfile'ı şu şekilde yapılandırılmıştır:

Dockerfile

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
Bu Dockerfile, aşağıdaki adımları takip eder:

Python 3.10-slim imajını kullanarak temel Docker imajını oluşturur.
requirements.txt dosyasını kopyalar ve gerekli Python kütüphanelerini yükler.
Uygulamanın tüm dosyalarını konteyner içine kopyalar.
Uygulamayı çalıştırmak için python app.py komutunu çalıştırır.

### 4. Gereksinimleri Yükleyin
Docker ile kurulum yapılacağı için, uygulama konteyner içinde çalıştırılacaktır. Ancak, normal kurulumda gereksinimleri yüklemek için şu komutu kullanabilirsiniz:

"pip install -r requirements.txt"

5. Dash Uygulamasını Başlatın

Uygulama, Docker ile başlatıldığında otomatik olarak çalışacaktır. Ancak, normal bir ortamda çalıştırmak için şu komutu kullanabilirsiniz:



"python app.py"

Bu adımları takip ederek uygulamanızı başlatabilirsiniz.

Kullanım
Segmentasyon Modeli:

KMeans algoritması ile segmentasyon yapılır.

Müşteri segmentleri şu şekilde adlandırılmaktadır:

Yeni Müşteriler

Sadık Müşteriler

Potansiyel Churn

Churn Müşteriler

Potansiyel Müşteriler


Modelin Kaydedilmesi:

Uygulama, modelin başarısını değerlendirdikten sonra kmeans_model.pkl olarak kaydeder.
Tahminler:

predict_data fonksiyonu ile yeni müşteri verileri üzerinde tahmin yapılabilir ve müşteri segmentleri tahmin edilir.

## Gereksinimler

dash==2.18.2
dash-bootstrap-components==1.7.1
dash-core-components==2.0.0
dash-html-components==2.0.0
dash-table==5.0.0
Flask==3.0.3
joblib==1.4.2
numpy==2.2.2
pandas==2.2.3
plotly==6.0.0
requests==2.32.3
retrying==1.3.4
scikit-learn==1.6.1
scipy==1.15.1
threadpoolctl==3.5.0
tzdata==2025.1
urllib3==2.3.0
zipp==3.21.0

## Geliştirici Notları

### Modelin Eğitim ve Tahmin Süreçleri:

Modelin eğitimi ve tahmin süreci KMeans algoritması ile gerçekleştirilir.
Segmentasyon etiketleri, label_clusters fonksiyonu ile her müşteri için atanır.
Veri Seti:

Proje, müşteri verilerini işlemek için Pandas ve Numpy gibi kütüphaneleri kullanmaktadır.
