import base64
from user_exception import InvalidPassword, UserDoesNotExist, UserNotLoggedIn, PermissionExists, \
    InvalidPermission, UserNotPermitted, UserPermissionExists
from enum import Enum


class Permission(Enum):
    ADMIN = 1
    USER = 2
    CONTRACTOR = 3


class User:

    def __init__(self, name, password):
        self._name = name
        self._password = self._encrypted_password(password)

        self._is_logged_in = False

    @property
    def name(self):
        return self._name

    @property
    def password(self):
        return self._password

    def _encrypted_password(self, pwd):
        if pwd is not None and pwd != '':
            return base64.b64encode(pwd.encode('utf-8'))
        raise InvalidPassword('Password is not valid')

    def authenticate_user(self, pwd):
        if pwd is not None and pwd != '' and self.password == self.encrypted_password(pwd):
            self._is_logged_in = True
            return True
        raise InvalidPassword('Password not valid')

    def logout(self):
        if self._is_logged_in:
            self._is_logged_in = False
            return True
        raise UserNotLoggedIn('Cannot logout the user')

    def __repr__(self):
        return f"Name:\t{self.name}"


class Authenticator:

    def __init__(self):
        self._users = {}

    def add_user(self, user: User):
        if isinstance(user, User):
            self._users[user.name] = user

    def remove_user(self, name):
        if name in self._users:
            self._users.pop(name)
            return True
        raise UserDoesNotExist('User with this namne could not be find')

    def login(self, name, pwd):
        if name and pwd:
            if name in self._users:
                user = self._users[name]
                return user.authenticate_user(pwd)
            raise UserDoesNotExist('User could not be found')

    def logout(self, name):
        if name in self._users:
            return self._users[name].logout()


def decorate_user_perm(func):
    def inner(*args):
        self = args[0]
        if args[1] in self.authenticator._users:
            if args[2].name in self.permission:
                return func(*args)
            raise InvalidPermission('Permision does not exists')
        raise UserDoesNotExist('User does not exists')

    return inner


class Authorizer:

    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permission = {}

    def add_permission(self, perm):
        if not perm.name in self.permission:
            self.permission[perm.name] = []
            return True
        raise PermissionExists('Permission already exists')

    @decorate_user_perm
    def remove_user_permission(self, name, perm):
        if name in self.permission[perm]:
            self.permission[perm].remove(name)
            return True
        raise UserNotPermitted('User does not have permission')

    @decorate_user_perm
    def give_user_permission(self, name, perm):
        if name not in self.permission[perm.name]:
            self.permission[perm.name].append(name)
            return True
        raise UserPermissionExists('User already has permission')

    @decorate_user_perm
    def check_permission(self, name, perm):
        if name in self.permission[perm.name]:
            return True
        raise UserNotPermitted('User is not permitted')

    def list_user_permission(self, user):
        if self.authenticator._users.get(user, None):
            return self.authenticator._users.get(user)
        raise UserDoesNotExist('OK')


u1 = User('avi', 'avijatya')
u2 = User('Ravi', 'Ravikant')


auth = Authenticator()
auth.add_user(u1)
auth.add_user(u2)
auz = Authorizer(auth)
auz.add_permission(Permission.ADMIN)
auz.add_permission(Permission.CONTRACTOR)
auz.give_user_permission('avi', Permission.ADMIN)
#auz.check_permission('avi', Permission.CONTRACTOR)

# print(auz.list_user_permission('avi'), "\n", auz.permission)
