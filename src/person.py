## @file person.py
## @brief Doxygen tarzı yorumlara sahip örnek Python programı.
##
## @section description_person Person Sınıfı
## Person sınıfı, kişilerin bilgilerini temsil eder.
##
## @section usage_person Kullanım
## Bu sınıf, kişisel bilgileri almak ve selamlaşma mesajı döndürmek için kullanılabilir.
class Person:
    ## @brief Person sınıfı
    ##
    ## Kişi bilgilerini temsil eden sınıf.
    def __init__(self, name, age):
        ## @brief Sınıfın yapıcı metodu
        ##
        ## @param name Kişinin ismi.
        ## @param age Kişinin yaşı.
        self.name = name
        self.age = age

    ## @brief Kişisel bir selamlaşma mesajı döndürür.
    ##
    ## @return Selamlaşma mesajı.
    def greet(self):
        return f"Merhaba, benim adım {self.name} ve {self.age} yaşındayım."

# Person sınıfını kullanarak bir nesne oluşturulur
person1 = Person("Zeynep", 22)

# Nesnenin greet metodunu çağırılır
print(person1.greet())
