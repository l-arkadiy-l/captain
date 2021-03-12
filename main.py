from data import db_session
from data.users import User


def add_user(surname, name, age, position, speciality, address, email):
    user = User()
    user.surname = surname
    user.name = name
    user.age = age
    user.position = position
    user.speciality = speciality
    user.address = address
    user.email = email

    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


def fill_base():
    temp_users = [("Scott", "Ridley", "21", "captain", "research engineer", "module_1", "scott_chief@mars.org")]
    for user in temp_users:
        add_user(*user)


if __name__ == "__main__":
    db_session.global_init("db/mars.db")
    fill_base()

