class Client:

    def __init__(self, age, name, organization, gender):
        self.hehe = age
        self.__name = name
        self.__organization = organization
        self.__gender = gender

    def age(self):
        return f"age는 {self.hehe} 입니다."

    def name(self):
        return f"name는 {self.__name} 입니다."

    def organization(self):
        return f"organization는 {self.__organization} 입니다."

    def gender(self):
        return f"gender는 {self.__gender} 입니다."


samsung_client = Client(50, "김갑수", "삼성", "남")
print(samsung_client.age())
print(samsung_client.hehe)
