import psycopg2

conn = psycopg2.connect(
    "postgres://bdyfetakcxtjem:18cfa4a4b4672a76b4eaaec4aff9bde1eb1303711fb74f85795577eda7bec83a@ec2-3-230-247-88"
    ".compute-1.amazonaws.com:5432/d1ccsc56pnpc4p")
cursor = conn.cursor()
nds = 20
nds += 100


class AbstractWastes:
    @staticmethod
    def create(purchase_name, purchase_time, purchase_type, purchase_amount):
        pass

    @staticmethod
    def read(find=None, find2=None):
        pass

    @staticmethod
    def update(what, to, find=None, find2=None):
        pass

    @staticmethod
    def delete(find=None, find2=None):
        pass


class Wastes(AbstractWastes):
    @staticmethod
    def create(purchase_name, purchase_time, purchase_type, purchase_amount):
        cursor.execute("""
        SELECT number FROM SPENDS
        """)
        r = cursor.fetchall()
        r = list(r)
        if not r:
            number = 1
        else:
            number = int(str(r[-1]).replace(",", "").replace("(", "").replace(")", ""))
            number += 1
        if purchase_type == "o":
            purchase_amount = purchase_amount / nds * 100
        cursor.execute(f"""INSERT INTO SPENDS VALUES(
        '{number}','{purchase_name}','{purchase_time}','{purchase_type}','{purchase_amount}'
        )""")
        conn.commit()
        return "Created new spend!"

    @staticmethod
    def read(find=None, find2=None):
        if find is not None and find2 is not None:
            cursor.execute(
                f"""SELECT number, name, time, type, amount FROM SPENDS WHERE time = '{find}' AND type = '{find2}'""")
            return cursor.fetchall()
        elif find is not None:
            cursor.execute(f"""SELECT number, name, time, type, amount FROM SPENDS WHERE time = '{find}'""")
            return cursor.fetchall()
        elif find2 is not None:
            cursor.execute(f"""SELECT number, name, time, type, amount FROM SPENDS WHERE type = '{find2}'""")
            return cursor.fetchall()

    @staticmethod
    def update(what, to, find=None, find2=None):
        if find is not None and find2 is not None:
            cursor.execute(
                f"""UPDATE USERS SET {what} = '{to}' FROM SPENDS WHERE time = '{find}' AND type = '{find2}'""")
            return cursor.fetchall()
        elif find is not None:
            cursor.execute(f"""UPDATE USERS SET {what} = '{to}' FROM SPENDS WHERE time = '{find}'""")
            return cursor.fetchall()
        elif find2 is not None:
            cursor.execute(f"""UPDATE USERS SET {what} = '{to}' FROM SPENDS WHERE type = '{find2}'""")
            return cursor.fetchall()
        return "Updated spend!"

    @staticmethod
    def delete(find=None, find2=None):
        if find is not None and find2 is not None:
            cursor.execute(f"""DELETE FROM SPENDS WHERE time = '{find}' AND type = '{find2}'""")
            return cursor.fetchall()
        elif find is not None:
            cursor.execute(f"""DELETE FROM SPENDS WHERE time = '{find}'""")
            return cursor.fetchall()
        elif find2 is not None:
            cursor.execute(f"""DELETE FROM SPENDS WHERE type = '{find2}'""")
            return cursor.fetchall()
        return "Deleted spend!"
