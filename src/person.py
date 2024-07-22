class Person:
    """
    @class Person
    @brief Bir kişiyi temsil eden sınıf.
    
    Bu sınıf, bir kişiyi temsil eder ve kişinin adını ve yaşını saklar.
    """
    
    def __init__(self, name: str, age: int):
        """
        @brief Person sınıfının yapıcı metodu.
        
        @param name Kişinin adı.
        @param age Kişinin yaşı.
        """
        self.name = name
        self.age = age

    def greet(self) -> str:
        """
        @brief Kişiyi tanıtan metot.
        
        @return Kişiyi tanıtan merhaba mesajı.
        """
        return f"Merhaba, ben {self.name}, {self.age} yaşındayım."
