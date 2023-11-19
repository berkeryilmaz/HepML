## Genel Bakış

Bu Python modülü, belirtilen dosyalardan osiloskop verilerini okuma, birleştirme ve işleme işlevleri sunar. Osiloskop parametrelerini ve kanalları işlemek için özellikler içerir.

## Kurulum

Bu modülü kullanmak için aşağıdaki adımları izleyin:

1. Depoyu Proje Klasörünüze kopyalayın:


2. Python projenizde `Oscilloscope` modülünü içe aktarın:

```python
from Oscilloscope.Oscilloscope import Oscilloscope
```

## Kullanım

### Başlatma

Belirtilen dosya yolları ile bir `Oscilloscope` nesnesi başlatabilirsiniz:

```python
osci = Oscilloscope(file_paths=['0.bin', '1.bin',...])
```

## Veri Okuma ve Kaydetme
### JSON'dan Okuma

Osiloskop verilerini bir JSON dosyasından yükleyebilirsiniz:
```python
osc = Oscilloscope.loadFromJson('dosya/yol/veri.json')
```

### JSON Olarak Kaydetme
Osiloskop verilerini JSON formatında bir dosyaya kaydetmek için:
```python
osc.saveAsJson('cikti/veri.json')
```

## Veri Erişimi
Aşağıdaki özellikler ve metotlar kullanılabilir:

- **getActiveChannel()**: Aktif kanalları alır. Channel nesnesinden oluşan bir liste döndürür.
- **file_paths**: Başlatmada kullanılan dosya yollarının listesi. Stringlerden oluşan bir liste döndürür.
- **timebase** : Osiloskopun timebase parametresini alır. Timebase nesnesi döndürür.
- **sample**: Osiloskopun sample parametresini alır. Sample nesnesi döndürür.
- **channel**: Osiloskopun kanal listesini alır. Channel nesnesinden oluşan bir liste döndürür.
- **datatype**: Osiloskopun datatype parametresini alır. String bir değer döndürür.
- **runstatus**: Osiloskopun runstatus parametresini alır String bir değer döndürür.
- **idn**: Osiloskopun idn parametresini alır. String bir değer döndürür.
- **model**: Osiloskopun model parametresini alır. String bir değer döndürür.
- **trig**: Osiloskopun trig parametresini alır. Trig nesnesi döndürür.

---
# Channel Sınıfı
Channel sınıfı, osiloskop kanallarından gelen verileri yönetmek ve analiz etmek için kullanılır. Veri manipülasyonu, tepe noktaların tespiti ve çizim yapma gibi işlevleri içerir.

## Başlatma
```python
__init__(self, channel_dict)
```
### Parametreler:
- **channel_dict** (dict): Kanal bilgilerini içeren bir sözlük.
- **name** (str): Kanalın adı.
- **display** (str): Gösterim durumu ('AÇIK' veya 'KAPALI').
- **current_rate** (float): Veri düzenlemesi için geçerli oran.
- **current_ratio** (float): Veri düzenlemesi için geçerli oran.
- **measure_current_switch** (str): Akım ölçme anahtarı.
- **coupling** (str): Bağlama tipi.
- **probe** (str): Prob bilgisi.
- **scale** (float): Veri için ölçek faktörü.
- **offset** (float): Veri düzenlemesi için ofset.
- **frequence** (float): Frekans bilgisi.
- **inverse** (bool): Ters çevirme durumu.
- **data** (list, opsiyonel): Kanal verisi (varsa).

Belirtilen kanal bilgileriyle Channel nesnesini başlatır.

## Veri Yönetimi
    setData(self, raw_data)

### Parametreler:
    raw_data (list): İşlenecek ham veri.
Geçerli oran ve orantı kullanılarak ham veriyi işler ve kanalın veri özelliğini ayarlar.

## Tepe Noktalarının Tespiti
Belirtilen veri aralığındaki tepe noktalarının sayısını döndürür.
```python
channel.findPeaks(self, begin=None, end=None)
```
### Parametreler:
- **begin** (int, opsiyonel): Tepe arama için başlangıç indis.
- **end** (int, opsiyonel): Tepe arama için bitiş indis.
---

```python
channel.countPeaks(self, begin=None, end=None)
```
### Parametreler:
- **begin** (int, opsiyonel): Tepe sayımı için başlangıç indis.
- **end** (int, opsiyonel): Tepe sayımı için bitiş indis.



## Veri Görselleştirme
Osiloskop ekranını simule etmek için aşağıdaki fonksiyon kullanılır
```python
osc.showOscilloscopeScreen()
```

Kanalın verisini belirlenen tepe noktalarıyla birlikte çizim olarak görüntüler.
```python
channel.showPlot(self, title='', begin=None, end=None)
```
### Parametreler:
- **title** (str, opsiyonel): Çizimin başlığı.
- **begin** (int, opsiyonel): Çizim için başlangıç indis.
- **end** (int, opsiyonel): Çizim için bitiş indis.

---
Tespit edilen tepe noktalarıyla birlikte kanalın verisini çizim olarak oluşturur ve belirtilen yolda görüntü olarak kaydeder.

```python
channel.savePlot(self, path, title, begin=None, end=None)
```
### Parametreler:
- **path** (str): Çizim görüntüsünün kaydedileceği yol.
- **title** (str): Çizim başlığı.
- **begin** (int, opsiyonel): Çizim için başlangıç indis.
- **end** (int, opsiyonel): Çizim için bitiş indis.
---
Kanalın verisini tespit edilen tepe noktalarıyla birlikte çizim için hazırlar.
```python
channel.setPlot(self, title, begin=None, end=None)
```
### Parametreler:
- **title** (str): Çizim başlığı.
- **begin** (int, opsiyonel): Çizim için başlangıç indis.
- **end** (int, opsiyonel): Çizim için bitiş indis.

---

# Sample Sınıfı
Sample sınıfı, örnekleme (sample) verilerini temsil etmek için kullanılır. Bu sınıf, örnek verilerin belirli özelliklerini içerir ve bir __init__ metoduyla başlatılır.

## Başlatma
```python
__init__(self, sample_dict)
```
### Parametre:
- **sample_dict** (dict): Örnek sözlüğü, örnek özelliklerini içerir.
- **fullscreen** (bool): Tam ekran durumu.
- **slowmove** (bool): Yavaş hareket durumu.
- **datalen** (int): Veri uzunluğu.
- **samplerate** (float): Örnekleme hızı.
- **type** (str): Örnek türü.
- **depmem** (str): Bağımlı bellek bilgisi.
- **precision** (str): Hassasiyet bilgisi.
 
Bumetot, verilen örnek sözlüğüyle Sample nesnesini başlatır. Örnek özelliklerini belirtilen sözlükteki değerlere atar.

---
# TimeBase Sınıfı
TimeBase sınıfı, zaman bazlı verileri temsil etmek için kullanılır. Bu sınıf, zaman bazlı verilerin belirli özelliklerini içerir ve __init__ metoduyla başlatılır.

## Başlatma
```python
__init__(self, time_base_dict)
```
### Parametre:
- **time_base_dict** (dict): Zaman bazlı sözlük, zaman bazlı özellikleri içerir.
- **scale** (float): Ölçeklendirme faktörü.
- **hoffset** (float): Yatay ofset.

Bu metot, verilen zaman bazlı sözlükle TimeBase nesnesini başlatır. Zaman bazlı özellikleri belirtilen sözlükteki değerlere atar.

---

# Trig Sınıfı
Trig sınıfı, tetikleme (triggering) parametrelerini temsil etmek için kullanılır. Bu sınıf, belirli tetikleme özelliklerini içerir ve __init__ metoduyla başlatılır. Ayrıca __dict__ özelliği ile veriyi sözlük formatında döndürür.

## Başlatma
```python
__init__(self, trig_dict)
```
### Parametre:
- **trig_dict** (dict): Tetikleme sözlüğü, tetikleme özelliklerini içerir.
- **mode** (str): Tetikleme modu.
- **type** (str): Tetikleme tipi.
- **items** (TrigItems): Tetikleme öğeleri.
- **sweep** (str): Tara (sweep) bilgisi.

Bu metot, verilen tetikleme sözlüğüyle Trig nesnesini başlatır. Tetikleme özelliklerini belirtilen sözlükteki değerlere atar.

---

# TrigItems Sınıfı
TrigItems sınıfı, tetikleme öğelerini temsil etmek için kullanılır. Bu sınıf, belirli tetikleme öğelerini içerir ve __init__ metoduyla başlatılır.

## Başlatma
```python
__init__(self, trig_items_dict)
```

### Parametre:
- **trig_items_dict** (dict): Tetikleme öğeleri sözlüğü, tetikleme öğesi özelliklerini içerir.
- **channel** (str): Kanal bilgisi.
- **level** (float): Seviye bilgisi.
- **edge** (str): Kenar bilgisi.
- **coupling** (str): Bağlama bilgisi.
- **holdoff** (float): Bekleme süresi bilgisi.

Bu metot, verilen tetikleme öğeleri sözlüğüyle TrigItems nesnesini başlatır. Tetikleme öğesi özelliklerini belirtilen sözlükteki değerlere atar.

---

# Örnek Kullanım

Oscilloscpoe sınıfımızı projemize dahil edelim
```python
from Oscilloscope.Oscilloscope import Oscilloscope
```

Oscilloscpoe sınıfından bir tane osc isimlli nesne oluşturalım. 
Bu nesnin bilgileri osiloskoptan sağlanan dosyalardan okunacaksa:
```python
osc = Oscilloscope(['0.bin','1.bin'])
```

Bu nesnin bilgileri data önce kaydedilen bir json dosyasından okunacaksa:
```python
osc = Oscilloscope.loadFromJson('dosya/yol/veri.json')
```

Bu nesnin osiloskop ekranını simule edelim:
```python
osc.showOscilloscopeScreen()
```


Bu nesnenin herhangi bir değerini alalım. Örnek Sample:
```python
sample = osc.sample
```

Sample'ın samplerate değerini almak istersek:
```python
samplerate = osc.sample.samplerate
```

Osiloskopun kayıt sırasında aktif kanallarını çağıralım. Burası bize array dönecektir. İlk aktif kanalı almak için [0] eklemelyiz.
```python
active_channel_list = osc.getActiveChannel()
active_channel = active_channel_list[0]
```

Aktif kanaldaki datayı ekrana yazdıralım:
```python
print(active_channel.data)
```

Aktif kanaldaki datayı grafik üzerinde görmek için:
```python
active_channel.showPlot('Ölçüm verisi')
```

Aktif kanaldaki datanın belirli bir aralığını grafik üzerinde görmek için:
```python
active_channel.showPlot('Ölçüm verisi',1000,2000)
```

Aktif kanaldaki datanın grafiğini kaydetmek için :
```python
active_channel.savePlot('images/olcum_verisi.png','Ölçüm verisi')
```

Aktif kanaldaki datanın grafiğini belirli bir aralığını kaydetmek için: 
```python
active_channel.savePlot('images/olcum_verisi.png','Ölçüm verisi',1000,2000)
```

Aktif kanaldaki datadaki tepe noklarını almak karşılık gelen indisleri almak için: 
```python
peaks = active_channel.findPeaks()
```

Aktif kanaldaki datanın belirli aralıktaki tepe noklarını almak karşılık gelen indisleri almak için: 
```python
peaks = active_channel.findPeaks(1000,2000)
```

Aktif kanaldaki datadaki tepe noklarının sayısını almak için: 
```python
peak_count = active_channel.countPeaks()
```

Aktif kanaldaki datanın belirli aralıktaki tepe noklarını sayısını almak için: 
```python
peak_count = active_channel.countPeaks(1000,2000)
```