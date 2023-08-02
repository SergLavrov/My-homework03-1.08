# Создать класс User, у которого будут:
# Имя
# Фамилия
# Логин (не менее 5 символов)
# Пароль (не меньше 8 символов и должен содержать минимум 3 буквы).

# Все поля должны быть скрытыми.
# К каждому атрибуту написать по два метода.

# Для вывода пользователя метод str не использовать.

class User:

    def __init__(self, first_name, sur_name, login, password):

        self.__firstName = first_name
        self.__surName = sur_name

        if login != '' and len(login) >= 5:
            self.__loginUser = login
        else:
            print('Enter login once again: ')

        if password != '' and len(password) >= 8:
            cnt = 0
            for index in range(len(password)):
                if password[index].isalpha:
                    cnt += 1
                    if cnt >= 3:
                        self.__passwordUser = password
        else:
            print('Enter password once again: ')

    # def set_first_name(self, new_name):
    #     self.__firstName = new_name

    def get_name(self):
        return self.__firstName
    def get_surname(self):
        return self.__surName
    def get_login(self):
        return self.__loginUser
    def get_password(self):
        return self.__passwordUser


    def change_first_name(self, new_first_name):
        self.firstName = new_first_name

    def change_sur_name(self, new_sur_name):
        self.surName = new_sur_name

    def change_login(self, new_login):
        if new_login != '' and len(new_login) >= 5:
            self.loginUser = new_login
        else:
            print('Enter login once again: ')

    def change_password(self, new_password):
        self.passwordUser = new_password


user = User('Иван', 'Иванов', '6226ip', 'rta19805')

# user.set_first_name('Петр')

print(user.get_name())
print(user.get_surname())
print('------------')

print(user.get_login())
print(user.get_password())
print('------------')

user.change_first_name('Ivan')
user.change_sur_name('Ivanov')
# # print(user.firstName)
# # print(user.surName)
print(user.firstName + '\n' + user.surName)

print('------------')

user.change_login('5555tr')
user.change_password('uta77755')

print(user.loginUser + '\n' + user.passwordUser)











# Пример с прошлого занятия !!!

# Создать класс "Проект":
# - название,
# - дата начала,
# - дата dead-line,
# - список имён программистов, которые над ним работают.
# Дата (DateTime) начала должна браться автоматически при создании объекта проекта.
# Реализовать метод str(self)
# Список программистов на проекте тоже нужно обработать, чтобы он выводился красиво в str.
#
# Создать методы класса:
# 1. Изменение даты (DateTime) окончания проекта
# 2. Добавление программиста на проект
# 3. Метод увольнения программиста с проекта.


# import datetime
# class Project:
#     def __init__(self, name_project, deadline_date, programmers):
#         self.nameProject = name_project
#         self.firstDate = datetime.date.today()
#         self.deadlineDate = deadline_date
#         self.programmers = programmers
#
#     def add_programmer(self, programmer):
#         self.programmers.append(programmer)
#
#     def remove_programmer(self, programmer):
#         self.programmers.remove(programmer)
#
#
#     def change_date_end(self, new_date_end):
#         self.deadlineDate = new_date_end
#
#
#     def __str__(self):
#         listProgr = ''
#         for item in self.programmers:
#             listProgr += '\t' + item + '\n'
#         return (f'Название проекта: {self.nameProject}\n' \
#             f'Дата начала: {self.firstDate}\n' \
#             f'Дата окончания: {self.deadlineDate}\n' \
#             f'Список программистов: \n{listProgr}')
#
#
# listProgrammers = ['Tom', 'Ted', 'Mike']
# project = Project('Проект Космос', datetime.date(2023, 10, 25), listProgrammers)
# print(project)
#
# project.add_programmer('Stas')
# print(project)
#
# project.remove_programmer('Mike')
# print(project)
#
# project.change_date_end(datetime.date(2023, 11, 27))
# print(project)
