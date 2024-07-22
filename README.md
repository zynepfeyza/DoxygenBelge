# Proje Açıklaması

Bu proje, bir Python uygulamasının belgelenmesi için örnek bir Doxygen yapılandırması sunmaktadır.

## Doxygen Kurulumu
Belgelendirmeyi oluşturabilmeniz için Doxygen'i yüklemelisiniz. Linux işletim sistemi ile çalıştığım için aşağıdaki komutu kullandım.
```sh
sudo apt-get install doxygen
```
Aşağıdaki komutu, sürüm numarasını yazdıracak bir terminal ekranında çalıştırarak doğru şekilde yüklendiğini test edin.
```sh
doxygen --version
```
Benim versiyonum aşağıdaki gibi görünüyor.
```sh
1.9.1
```
## Bir Python Programı Oluşturma
Doxygen kullanarak kaynak kodundan belge oluşturabilmek için öncelikle kaynak koda sahip olmamız gerek. Ben bunun için `person.py` adında bir Python programı oluşturdum.
```
class Person:
    """
    @class Person
    @brief Bir kişiyi temsil eden sınıf.
    
    Bu sınıf, bir kişiyi temsil eder ve kişinin adını ve yaşını saklar.
    """
```





