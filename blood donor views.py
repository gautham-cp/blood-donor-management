import mysql.connector
from mysql import connector
import datetime
class BloodDonorManager:
    def __init__(self):
        self.connection= connector.connect(
            host="localhost",
            user="root",
            password="Gau@123##",
            database="blood_db_b3"
        )
        print("connected successfully...!")

    def get_object(self, id=None):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from donor where id=%s"
            values = (id,)
            self.cursor.execute(query, values)
            records = self.cursor.fetchone()
            return records
        except Exception as e:
            return None

    def post(self,**kwargs):
        try:
            self.cursor = self.connection.cursor()
            query = "insert into donor (name, blood_group, phone, city, last_donation) values (%s,%s,%s,%s,%s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connection.commit()
            print("donor added successfully....!")
        except Exception as e:
            print(e)
    def get(self):
        try:
            self.cursor=self.connection.cursor()
            query= "select * from donor"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            for data in records:
                print(data)
        except Exception as e:
            print(e)

    def retrieve(self, id=None):
        try:
           records=self.get_object(id=id)
           if records==None:
               print("record not found...!")
           else:
               print(records)

        except Exception as e:
            print(e)

    def delete(self, id=None):
        try:
            records =self.get_object(id=id)
            values = (id,)
            if records != None:
                query="delete from donor where id=%s"
                self.cursor.execute(query, values)
                self.connection.commit()
                print("donor deleted successfully")
            else:
                print("donor not found")

        except Exception as e:
            print(e)

    def put(self,id=None,**kwargs):
        try:
            records=self.get_object(id=id)
            if records != None:  # if a record is found, then record willl not be none
                self.cursor = self.connection.cursor()
                placeholder = ""  # creates an emply string. this variables
                # to construct the set part of the sql query
                for k in kwargs.keys():
                    placeholder += k + "%s, "
                placeholder = placeholder.rsplit(", ")
                # this is necessary because we  dont want to comma
                query = f"update donor set {placeholder} where id=%s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query, values)
                self.connection.commit()
                print("donor details updated successfully....!")
            else:
                print("donor not found...!")
        except Exception as e:
            print("Error occurred....")







donor_instance=BloodDonorManager()  #create an object
#donor_instance.post(name="kiran",blood_group="B+",phone="9995987442",city="alapuzha",last_donation=datetime.datetime.today())
donor_instance.get()
print("-----details of one blood donor----")
donor_instance.retrieve(id=1)
print("---delete operation----")
donor_instance.delete(id=3)

donor_instance.get()
print("-----after updation----")
donor_instance.put(id=2,city="calicut")
donor_instance.get()