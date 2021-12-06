# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    the_bank.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/19 22:08:47 by mli               #+#    #+#              #
#    Updated: 2021/12/06 22:52:02 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

    def __str__(self):
        name = self.name if hasattr(self, 'name') else None
        id = self.id if hasattr(self, 'id') else None
        return f"Account(name: {name}, id: {id})"
    def __repr__(self):
        return f"Account({self.__dict__})"

class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []

    @staticmethod
    def account_validity(account: Account) -> bool:
        if not isinstance(account, Account):
            return False
        acc_attributes = dir(account)
        if len(acc_attributes) % 2 == 0 or \
            'name' not in acc_attributes or \
            'id' not in acc_attributes or \
            'value' not in acc_attributes or \
            len(list(filter(lambda att: att.startswith('b'), acc_attributes))) != 0 or \
            len(list(filter(lambda att: att.startswith('zip'), acc_attributes))) == 0 or \
            len(list(filter(lambda att: att.startswith('addr'), acc_attributes))) == 0:
            return False
        return True

    def get_account(self, recipient) -> Account or None:
        if not isinstance(recipient, (int, str)):
            return None
        def check_id(acc: Account) -> bool:
            return (acc.id == recipient) if hasattr(acc, 'id') else False
        def check_name(acc: Account) -> bool:
            return (acc.name == recipient) if hasattr(acc, 'name') else False
        filter_check = check_id if isinstance(recipient, int) else check_name
        account = next(filter(filter_check, self.account), None)
        return account

    def add(self, account):
        if not isinstance(account, Account):
            return False
        self.account.append(account)

    def transfer(self, origin, dest, amount) -> bool:
        """
            @origin: int(id) or str(name) of the first account
            @dest:   int(id) or str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return  True if success, False if an error occured
        """
        if not isinstance(origin, (int, str)) or \
            not isinstance(dest, (int, str)) or \
            not isinstance(amount, float) or \
            amount < 0:
            False
        originAcc = self.get_account(origin)
        if self.account_validity(originAcc) is False or \
            originAcc.value < amount is False:
            return False
        destAcc = self.get_account(dest)
        if self.account_validity(destAcc) is False:
            return False
        originAcc.transfer(-amount)
        destAcc.transfer(amount)
        return True

    def fix_account(self, account) -> bool:
        """Fix the corrupted account
            @account: int(id) or str(name) of the account
            @return   True if success, False if an error occured
        """
        if not isinstance(account, (int, str)):
            return False
        acc = self.get_account(account)
        if not isinstance(acc, Account):
            return False
        if self.account_validity(acc) is True:
            return True
        acc_attributes = dir(acc)
        # Fix b* attribute
        b_attr = list(filter(lambda att: att.startswith('b'), acc_attributes))
        if len(b_attr) != 0:
            for attr_name in b_attr:
                delattr(acc, attr_name)
        # Fix zip attribute
        zip_attr = list(filter(lambda att: att.startswith('zip'), acc_attributes))
        if len(zip_attr) == 0:
            setattr(acc, 'zip', None)
        # Fix addr attribute
        addr_attr = list(filter(lambda att: att.startswith('addr'), acc_attributes))
        if len(addr_attr) == 0:
            setattr(acc, 'addr', None)
        if 'name' not in acc_attributes:
            setattr(acc, 'name', None)
        if 'id' not in acc_attributes:
            setattr(acc, 'id', None)
        if 'value' not in acc_attributes:
            setattr(acc, 'value', 0)
        # Fix even # of attr
        if len(dir(acc)) % 2 == 0:
            nb = 0
            while hasattr(acc, f'value{nb}'):
                nb += 1
            setattr(acc, f'value{nb}', None)
        return True

if __name__ == "__main__":
    def fix_account(bank: Bank, id: int or str) -> None:
        acc = bank.get_account(id)
        print(f'Fixing {acc}: ' + ('-' * 50), dir(acc), sep="\n")
        print('IS VALID?', bankA.account_validity(acc))
        print('FIX?', bankA.fix_account(id))
        print('IS VALID?', bankA.account_validity(acc))
        print(dir(acc), end="\n\n")

    empty_name_acc = Account("0")
    delattr(empty_name_acc, 'name')

    bankA = Bank()
    bankA.add(empty_name_acc)
    bankA.add(Account("A", zip=None, addr=None, value=10))
    bankA.add(Account("B", zip=None, addr=None, value=110))
    bankA.add(Account("C", zip=None, addr=None, value=100))
    bankA.add(Account("D", addrfoo="wow", value=0, value1="mdr", blol="sad", value0=None))
    bankA.add(Account("E", addrfoo="wow", value=0, value1="mdr", blol="sad", value0=None, value2=None, bwaw=None))

    fix_account(bankA, 1)
    fix_account(bankA, "A")
    fix_account(bankA, "D")
    fix_account(bankA, 6)
