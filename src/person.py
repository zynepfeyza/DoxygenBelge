#
## @mainpage Doxygen Örneği Prejesi
#
## @section description_main Açıklama
# Doxygen ile kaynak kodu belgeleri oluşturmak için Doxygen tarzı yorumların
# nasıl kullanılacağını gösteren örnek bir Python programı.
#
## @section notes_main Notlar
# - Doxygen kurulumu, komutları, yapılandırma dosyası oluşturma gibi işlemler gerçekleştirildi.

##
# @file person.py
#
# @brief Doxygen tarzı yorumlara sahip örnek Python programı.
##

## @brief Person sınıfı
##
# Kişi bilgilerini temsil eden sınıf.
class Person:
    ## @brief Person sınıfının yapıcı metodu
    ##
    ## @param name Kişinin ismi.
    ## @param age Kişinin yaşı.
    def __init__(self, name, age):
       
        self.name = name
        self.age = age
        
    ## @brief Kişisel bir selamlaşma mesajı döndürür.
    ##
    # @return Selamlaşma mesajı.
    def greet(self):
        return f"Merhaba, benim adım {self.name} ve {self.age} yaşındayım."

# Person sınıfını kullanarak bir nesne oluşturulur
person1 = Person("Zeynep", 22)

# Nesnenin greet metodunu çağırılır
print(person1.greet())
