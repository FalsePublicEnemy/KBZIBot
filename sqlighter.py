import sqlite3

class SQLighter:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def subscriber_exists(self, user_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `subscribtions` WHERE `user_id` = ?', (user_id,)).fetchall()
            return bool(len(result))

    def add_subscriber(self, user_id):
        """Добавляем нового подписчика"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `subscribtions` (`user_id`) VALUES(?)", (user_id,))

    def group_one_SQL(self,user_id,group=11):
        """Добавляем подписчика с 11 группой(по умолчанию)"""
        with self.connection:
            return self.cursor.execute("UPDATE `subscribtions` SET `group` = ? WHERE `user_id` = ?", (group, user_id))

    def group_two_SQL(self,user_id,group=12):
        """Изменяем на группу номер 12 , если подписчик не в первой группе"""
        with self.connection:
            return self.cursor.execute("UPDATE `subscribtions` SET `group` = ? WHERE `user_id` = ?", (group, user_id))

    def group_one_BODY(self,user_id,group_body=1):
        with self.connection:
            return self.cursor.execute("UPDATE `subscribtions` SET `group_body` = ? WHERE `user_id` = ?",(group_body,user_id))

    def group_two_BODY(self,user_id,group_body=2):
        with self.connection:
            return self.cursor.execute("UPDATE `subscribtions` SET `group_body` = ? WHERE `user_id` = ?",(group_body,user_id))

    def check_group_head(self, user_id,):
        """Проверяем на наличие в head группе"""

        result = self.cursor.execute("SELECT `group` FROM `subscribtions` WHERE `user_id` = ?",(user_id,)).fetchall()
        for row in result:
            result_end = row[0]

        return (result_end)

    def check_group_body(self, user_id,):
        """Проверяем на наличие в body группе"""

        result = self.cursor.execute("SELECT `group_body` FROM `subscribtions` WHERE `user_id` = ?",(user_id,)).fetchall()
        for row in result:
            result_end = row[0]

        return (result_end)

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()