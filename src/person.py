## @file person.py
# @brief Person sınıfını tanımlar.
#
# @section description_person Açıklama
# Bir isme ve yaşa sahip bir kişiyi temsil eden basit bir sınıf.
#
# @section libraries_person Kütüphaneler/Modüller
# - Yok.
#
# @section author_person Yazar(lar)
# - [Adınız] tarafından [Tarih] tarihinde oluşturulmuştur.
# - [Adınız] tarafından [Tarih] tarihinde değiştirilmiştir.
#
# @section notes_person Notlar
# - Yorumlar Doxygen uyumludur.
#
# @section todo_person Yapılacaklar
# - Yok.

## @brief Bir kişiyi temsil eden sınıf.
#
# Person sınıfı hakkında daha fazla ayrıntı.
class Person:
    ## @brief Person sınıfının yapıcı metodu.
    # @param name Kişinin adı.
    # @param age Kişinin yaşı.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    ## @brief Selamlama metodu.
    # @return Selamlaşma metni.
    def greet(self):
        return f"Merhaba, benim adım {self.name} ve {self.age} yaşındayım."

# Person sınıfını kullanarak bir nesne oluşturun
person1 = Person("Ali", 30)

# Nesnenin greet metodunu çağırın
print(person1.greet())
