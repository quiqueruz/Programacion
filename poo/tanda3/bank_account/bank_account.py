"""
Implementa la clase BankAccount. Cada cuenta corriente tiene un número de cuenta de 10 dígitos. El número de
cuenta se genera de forma aleatoria cuando se crea una cuenta nueva y no puede haber dos objetos con el mismo número
de cuenta. La cuenta se puede crear con un saldo inicial; en caso de no especificar saldo, se pondrá a cero
inicialmente. En una cuenta se pueden hacer ingresos y gastos. También es posible hacer una transferencia entre una
cuenta y otra. No se permite el saldo negativo. En el siguiente capítulo se propone un ejercicio como mejora de éste,
en el que se pide llevar un registro de los movimientos realizados.
"""
import random


class BankAccount:
    __registered_accounts = []

    def __init__(self, balance: int = 0):
        if balance < 0:
            raise ValueError("El saldo no puede ser negativo")
        while True:
            account_number = random.randint(1, 9999999999)
            if account_number not in BankAccount.__registered_accounts:
                BankAccount.__registered_accounts.append(account_number)
                self.__account = account_number
                break
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, add_money):
        if add_money < 0:
            raise ValueError("El dinero a sumar no puede ser negativo")
        self.__balance += add_money

    def withdraw(self, subtract_money):
        if subtract_money < 0:
            raise ValueError("El dinero a sumar no puede ser positivo")
        if subtract_money > self.__balance:
            raise ValueError("No puedes quitar mas dinero del que tienes en la cuenta")
        self.__balance -= subtract_money

    def transfer(self, other: 'BankAccount', money):
        self.withdraw(money)
        other.deposit(money)

    def __str__(self):
        return f"Número de cta: {self.__account} Saldo: {'%.2f' % self.__balance} €"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__balance})"


if __name__ == '__main__':
    cuenta1 = BankAccount()
    cuenta2 = BankAccount(1500)
    cuenta3 = BankAccount(6000)
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)
    cuenta1.deposit(2000)
    cuenta2.withdraw(600)
    cuenta3.deposit(75)
    cuenta1.withdraw(55)
    cuenta2.transfer(cuenta3, 100)
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)
