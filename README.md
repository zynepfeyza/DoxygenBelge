# Proje Açıklaması

Bu proje, bir Python uygulamasının belgelenmesi için örnek bir Doxygen yapılandırması sunmaktadır.

## Doxygen Kurulumu
Belgelendirmeyi oluşturabilmeniz için Doxygen'i yüklemelisiniz. Linux işletim sistemi ile çalıştığım için aşağıdaki komutu kullandım.
```sh
sudo apt-get install doxygen
```
Aşağıdaki komutu, sürüm numarasını yazdıracak bir komut ekranında çalıştırarak doğru şekilde yüklendiğini test edin.
```sh
doxygen --version
```
Benim versiyonum aşağıdaki gibi görünüyor.
```sh
1.9.1
```
## Bir Python Programı Oluşturma
Doxygen kullanarak kaynak kodundan belge oluşturabilmek için öncelikle kaynak koda sahip olmamız gerekiyor `DoxygenBelge` adında bir proje dizini oluşturalım. Bu dizinin altında bir `src` dizini oluşturalım. Kaynak kodumuzu buraya yerleştireceğiz. `src` dizininin içinde, `person.py` adında bir Python programı oluşturalım.
```sh
class Person:
    """
    @class Person
    @brief Bir kişiyi temsil eden sınıf.
    
    Bu sınıf, bir kişiyi temsil eder ve kişinin adını ve yaşını saklar.
    """
    .
    .
    .
```
## BURAYA @ # NE ANLAMA GELİYOR AÇIKLA

`person.py` dosyamızın çalıştırılabilir bir dosya olmasını sağlamak için aşağıdaki komut kullanılır. Bu komut dosya izinlerini değiştirmek için kullanılır. Dosya üzerinde hangi kullanıcıların hangi işlemleri yapabileceğini belirler. Bu komutta, `person.py` dosyasına tüm kullanıcılar için çalıştırma izni veririz.
```sh
sudo chmod a+x src/person.py
```
ve sonra dosyayı bu komutu girerek çalıştırırız.
```sh
./person.py
```
## Doxygen Yapılandırma Dosyası Oluşturma
Doxygen tabanlı yapılandırmamızın ve oluşturulan belgelerimizin bulunacağı bir dokümantasyon dizini oluşturalım. Proje dizini içinde, `src` dizinine paralel olarak bir `doxygen` dizini oluşturun (`docs` olarak da adlandırabilirsiniz.)
```sh
DoxygenBelge/
├── src/
│   └── person.py
└── doxygen/  (veya docs/)
```
 Kaynak kodu etkili bir şekilde analiz edip proje belgelerimizi oluşturabilmek için Doxygen, bir yapılandırma dosyasına ihtiyaç duyar. Bu dosya varsayılan olarak `Doxyfile` olarak adlandırılır ve burada proje ile ilgili bilgileri gireriz ve Doxygen'e Python kodunu nasıl işleyeceğini söyleriz.

 Komut penceresi içinde `doxygen` dizinine gidin ve aşağıdaki komutu çalıştırarak varsayılan bir `Doxyfile` dosyası oluşturun.
 ```sh
 cd doxygen
 ```
 ```sh
  doxygen -g
  ```
 Bu komut, geçerli dizin içinde bir `Doxyfile` yapılandırma dosyası oluşturacaktır.

Şimdi Doxyfile dosyasını düzenleyerek proje ile ilgili bilgileri girmemiz gerekiyor. Yapmak istediğimiz ilk değişiklik, Doxygen'e projemizin adını söylemektir. 
```sh
PROJECT_NAME = "My Project"
```
Proje adınız ne ise onu girebilirsiniz.
```sh
PROJECT_NAME = "Doxygen Örneği Projesi"
```
Bu, dokümantasyonumuzdaki projenin başlığı olacaktır.

Bu değişiklik, Javadoc tarzı kısa açıklamaların otomatik olarak tanınmasını sağlar.
```sh
JAVADOC_AUTOBRIEF      = NO
```
```sh
JAVADOC_AUTOBRIEF      = YES
```
Kodumdaki Javadoc tarzı yorum örnekleri
```
# Person sınıfı hakkında daha fazla ayrıntı.
class Person:
    ## @brief Person sınıfının yapıcı metodu.
    # @param name Kişinin adı.
    # @param age Kişinin yaşı.
    def __init__(self, name, age):
        self.name = name
        self.age = age
```
Bu değişiklik, `@brief` etiketini kullanarak yazdığınız kısa açıklamaları otomatik olarak tanır ve bunları kısa açıklama olarak işler. 

Java ve Python tabanlı kaynak kodu için oluşturulan dokümantasyonu optimize etmek için değiştirilir.
```sh
OPTIMIZE_OUTPUT_JAVA   = NO
```
```sh
OPTIMIZE_OUTPUT_JAVA   = YES
```
Bu ayar, kaynak kodunda bulunan tüm elemanların belgelenmesi gerektiğini belirtir. Bunu `YES` olarak ayarlamalıyız
```sh
EXTRACT_ALL = NO
```
```sh
EXTRACT_ALL = YES
```
Dokümantasyonunuzda, private ve static class üyelerini de dahil etmek istiyorsanız bu ayarları yapabilirsiniz.
```sh
EXTRACT_PRIVATE = YES

EXTRACT_STATIC = YES
```
Bu ayar, Doxygen tarafından üretilen belgelerde, kapsam adlarının gizlenmesini sağlar. Dokümantasyonun daha temiz ve okunabilir görünmesini sağlamak için kullanılır. Bu durumda, `Person::name` yerine sadece `name` gösterilir.
```sh
HIDE_SCOPE_NAMES       = NO
```
```sh
HIDE_SCOPE_NAMES       = YES
```
Bu ayar, kısa açıklamaların alfabetik sıraya göre sıralanmasını sağlar. Yani, belgelerdeki açıklamalar isimlerine göre A'dan Z'ye doğru sıralanır. Kullanıcıların belirli bir açıklamayı bulmasını kolaylaştırır. 
```sh
SORT_BRIEF_DOCS = NO
```
```sh
SORT_BRIEF_DOCS = YES
```
Bu ayar, Doxygen'in kaynak kodları bulmak için hangi dizinleri kontrol edeceğini belirtir. 

```sh
INPUT = 
```
```sh
INPUT = ../src
```
`../src` ifadesi, konfigürasyon dosyasının bulunduğu dizinin bir üst düzeyinde bulunan `src` adlı dizini işaret eder.

Bu ayar, Doxygen’in LaTeX formatında dokümantasyon oluşturmasını sağlar. LaTeX, genellikle yüksek kaliteli belgeler oluşturmak için kullanılan bir tür işaretleme dilidir.
```sh
GENERATE_LATEX = YES
```
```sh
GENERATE_LATEX = NO
```
LaTex tabanlı dokümantasyon oluşturmayı planlamadığım için `NO` olarak değiştiriyorum

Bu ayarlardan, `OPTIMIZE_OUTPUT_JAVA` ve `INPUT`,Doxygen ile Python kodunu belgelendirmek için gerçekten gereken ayarlardır. Diğerleri, dokümantasyonun çıkarılması ve okunabilirliğinin iyileştirilmesini sağlar.

Ayarlar tamamlandığında, güncellenmiş `Doxyfile`  dosyanızı kaydedin.

## Doxygen'i Çalıştırma

Yapılandırma dosyası güncellendiğine göre, Python tabanlı projemiz için HTML tabanlı dokümantasyonu oluşturmak üzere Doxygen'i çalıştıralım. Doxyfile ile aynı dizinde (`doxygen`) , Doxygen yürütülebilir dosyasını çalıştırın.
```sh
doxygen
```
Tamamlandığında, projeniz için oluşturduğu tüm HTML tabanlı belgelerinizi içeren bir html dizini oluşturduğunu görmelisiniz.

## Oluşturulan Belgeleri Görüntüleme
`html` dizininde bulunan `index.html` dosyasını tarayıcınızda açın. Bu ana proje sayfasıdır ve `person.py` programımızdaki komutu içeren yorum bloğunda belirttiğimiz tüm bilgileri bölümlere ayırarak görüntüler.

## ÖZET
Python tabanlı bir proje için Doxygen yardımcı programını kullanarak kaynak kodundan proje dokümantasyonunu nasıl oluşturacağımızı öğrendik. Sadece başkalarına kodunuzu daha kolay anlamaları için araçlar sağlamakla kalmaz, aynı zamanda bir süredir o kod üzerinde çalışmamış orijinal programcıya da yardımcı olabilir.











