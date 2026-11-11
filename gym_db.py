from mysql import connector
import datetime


class Dbconnect():
    def get_connection(self):
        try:
            self.connection = connector.connect(
                host="localhost",
                user="root",
                password="ajiThh**#110",
                database="gym_db"
            )
            return self.connection
        except Exception as e:
            print(e)
            return None


class GymMemberManager(Dbconnect):

    def get_object(self, id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()

            query = "SELECT * FROM member WHERE id = %s"
            values = (id,)

            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            return record

        except Exception as e:
            print(e)

    def get(self):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()

            query = "SELECT * FROM member"
            self.cursor.execute(query)

            records = self.cursor.fetchall()
            print(records)

        except Exception as e:
            print(e)

    def post(self, **kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()

            query = """
                INSERT INTO member
                (name, place, mobile, plan, fee, joining_date)
                VALUES (%s, %s, %s, %s, %s, %s)
            """

            values = [v for v in kwargs.values()]

            self.cursor.execute(query, values)
            self.connect.commit()

            print("New member added successfully")

        except Exception as e:
            print(e)

    def retrieve(self, id=None):
        try:
            record = self.get_object(id=id)

            if record is None:
                print("Member not found..!")
            else:
                print(record)

        except Exception as e:
            print(e)

    def delete(self, id=None):
        try:
            record = self.get_object(id=id)

            if record is not None:
                self.cursor = self.connect.cursor()

                query = "DELETE FROM member WHERE id = %s"
                values = (id,)

                self.cursor.execute(query, values)
                self.connect.commit()

                print("Member deleted successfully..")
            else:
                print("Member not found..")

        except Exception as e:
            print(e)

    def put(self, id=None, **kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()

            query = "SELECT * FROM member WHERE id = %s"
            self.cursor.execute(query, (id,))
            record = self.cursor.fetchone()

            if record is None:
                print("Member not found..!")
                return

            query = """
                UPDATE member
                SET name = %s,
                    place = %s,
                    mobile = %s,
                    plan = %s,
                    fee = %s,
                    joining_date = %s
                WHERE id = %s
            """

            values = (
                kwargs["name"],
                kwargs["place"],
                kwargs["mobile"],
                kwargs["plan"],
                kwargs["fee"],
                kwargs["joining_date"],
                id
            )

            self.cursor.execute(query, values)
            self.connect.commit()

            print("Member updated successfully..")

        except Exception as e:
            print(e)


connection_instance = Dbconnect()
print(connection_instance.get_connection())

member_instance = GymMemberManager()

member_instance.get()

# member_instance.post(
#     name="ajith",
#     place="alatil",
#     mobile="9737383633",
#     plan="3 months",
#     fee="5000",
#     joining_date="2020-04-04"
# )

# member_instance.post(
#     name="joyal",
#     place="alatil",
#     mobile="9737359633",
#     plan="5 months",
#     fee="7000",
#     joining_date=datetime.datetime.today()
# )

print("_____________________")
member_instance.retrieve(2)
print("-------------")
member_instance.delete(1)
print("-------------")
member_instance.get()
print("-------------")
# member_instance.put(
#     2,
#     name="anto",
#     place="kannur",
#     mobile="9737449633",
#     plan="6 months",
#     fee="8000",
#     joining_date=datetime.datetime.today()
# )
member_instance.retrieve(2)