from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :
# def add_product(name, price, quality, quantity):
# 	product_object = Product(
# 		name= name,
# 		price= price,
# 		quality=quality,
# 		quantity=quantity)
# 	session.add(product_object)
# 	session.commit()

# add_product("lambo", 3, "awesome", 3)

def create_product(name, price, quality, quantity):
	product_object = Product(
		name= name,
		price= price,
		quality=quality,
		quantity=quantity)
	session.add(product_object)
	session.commit()

# create_product("lambo", 3, "awesome", 3)

  #TODO: complete the functions (you will need to change the function's inputs) 
def update_product(name, price):
	product_object=session.query(
		Product).filter_by(
		name=name).first()
	if price > 300:
		print("too high")
	else:
		product_object.price = price	
		session.commit()
update_product("kiki", 7)

  #TODO: complete the functions (you will need to change the function's inputs)

def delete_product(product_name):
	session.query(Product).filter_by(
		name=product_name).delete()
	session.commit()

delete_product("lambo")

def get_product(id):
  pass
