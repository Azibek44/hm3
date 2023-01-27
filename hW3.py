class Bank:
    def __init__ (self,__name) -> None:
        self.__name = __name
        self.__balance = 0
    def money_x(self):
        user = int(input("Пополнить баланс: "))
        self.__balance += user 
        return f"имя владельца: {self.__name},на вашем счете: {self.__balance}"
    def kill(self):
        user = int(input("Сколько вы хотите обналичить :"))
        if self.__balance >= user:
            self.__balance -=user
            return f"обналичили: {user},остаток: {self.__balance}" 
        else:
            return f"недостаточно средств: {self.__balance}"
    def __jeckpot(self):
        return f"умножит вашь счет на 10, ваш счет: {self.__balance * 10}"
    def user (self,name,__balanse):
        self.name = name
        self.__balanse = __balanse
        return f"Name: {self.name}, Balance: {self.__balanse + self.__balance}"

ban = Bank("Ajybek")
print(ban.money_x())
print(ban.kill())
print(ban.user("Bekbolot",100))
print(ban._Bank__jeckpot())