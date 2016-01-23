import requests
import json
from random import randint
import string
from faker import Faker

account_id = '56a369fd957f400e00aa8ec6'
api_key = '963adb712062f1bd2057a6e4063a9c06'

def get_all_customers(api_key):
	url = 'http://api.reimaginebanking.com/customers?key={}'.format(api_key)

	# Getting a Savings Account by AccountType
	response = requests.get(url)

	if response.status_code == 200:
		customers = json.loads(response.content)
		i = 0
		for customer in customers:
			i +=1
			print "Customer:{}".format(i)
			print("id:"+customer["_id"])
			print("first_name :"+customer["first_name"])
			print("last_name :"+customer["last_name"])
			print("street_number :"+customer["address"]["street_number"])
			print("street_name :"+customer["address"]["street_name"])
			print("city :"+customer["address"]["city"])
			print("state :"+customer["address"]["state"])
			print("zip :"+customer["address"]["zip"])
			print("\n\n")
	else:
	    print('Customers do not exist for api_key')

def get_customer_details_by_customer_id(customer_id,api_key):
	url = 'http://api.reimaginebanking.com/customers/?key={}'.format(customer_id,api_key)

	response = requests.get(url)

	if response.status_code == 200:
		customer = json.loads(response.content)
		print("id:"+customer["_id"])
		print("first_name :"+customer["first_name"])
		print("last_name :"+customer["last_name"])
		print("street_number :"+customer["address"]["street_number"])
		print("street_name :"+customer["address"]["street_name"])
		print("city :"+customer["address"]["city"])
		print("state :"+customer["address"]["state"])
		print("zip :"+customer["address"]["zip"])
		print("\n\n")
	else:
	    print('Customers do not exist for api_key')

	
def get_customer_details_by_account_id(account_id,api_key):
	url = 'http://api.reimaginebanking.com/accounts/{}/customer?key={}'.format(account_id,api_key)

	response = requests.get(url)

	if response.status_code == 200:
		customer = json.loads(response.content)
		print("id:"+customer["_id"])
		print("first_name :"+customer["first_name"])
		print("last_name :"+customer["last_name"])
		print("street_number :"+customer["address"]["street_number"])
		print("street_name :"+customer["address"]["street_name"])
		print("city :"+customer["address"]["city"])
		print("state :"+customer["address"]["state"])
		print("zip :"+customer["address"]["zip"])
	else:
	    print('Customer does not exist for this account with id '+account_id)


def create_customer(api_key,first_name,last_name,address):
	url = 'http://api.reimaginebanking.com/customers?key={}'.format(api_key)
	payload ={
	  "first_name": first_name,
	  "last_name": last_name,
	  "address": {
	    "street_number": address["street_number"],
	    "street_name": address["street_name"],
	    "city": address["city"],
	    "state": address["state"],
	    "zip": address["zip"]
	  }
	}
	# Create a customer
	response = requests.post( 
		url, 
		data=json.dumps(payload),
		headers={'content-type':'application/json'},
		)
	if response.status_code == 201:
		print('Customer created')
		customer = json.loads(response.content)["objectCreated"]
		print("id:"+customer["_id"])
		print("first_name :"+customer["first_name"])
		print("last_name :"+customer["last_name"])
		print("street_number :"+customer["address"]["street_number"])
		print("street_name :"+customer["address"]["street_name"])
		print("city :"+customer["address"]["city"])
		print("state :"+customer["address"]["state"])
		print("zip :"+customer["address"]["zip"])
	else:
	    print('Error in creating customer')


def update_customer_by_customer_id(account_id,api_key,address):
	url = 'http://api.reimaginebanking.com/customers?key={}'.format(account_id,api_key)
	payload = {
	  "address": {
	    "street_number": address["street_number"],
	    "street_name": address["street_name"],
	    "city": address["city"],
	    "state": address["state"],
	    "zip": address["zip"]
	  }
	}

	response = requests.put( 
		url, 
		data=json.dumps(payload),
		headers={'content-type':'application/json'},
		)

	if response.status_code == 202:
		customer = json.loads(response.content)
		print("Message :"+customer["message"])
	else:
	    print('Error in updating account')

def get_random_address():
	fake = Faker()
	address = {}
	address["street_number"] = str(fake.building_number())
	address["street_name"] = str(fake.street_name())
	address["city"] = str(fake.city())
	address["state"] = str(fake.state_abbr())
	address["zip"] = str(fake.zipcode())
	return address

def get_random_first_name():
	fake = Faker()
	return str(fake.first_name())

def get_random_last_name():
	fake = Faker()
	return str(fake.last_name())

def task_to_perform(option):
	if option==1:
		first_name = get_random_first_name()
		last_name = get_random_last_name()
		address = get_random_address()
		create_customer(api_key,first_name,last_name,address)
	elif option==2:
		#account_id = raw_input("Enter the account id :")
		get_customer_details_by_account_id(account_id,api_key)
	elif option==3:
		customer_id = raw_input("Enter the customer id :")
		get_customer_details_by_customer_id(customer_id,api_key)
	elif option==4:
		get_all_customers(api_key)
	elif option==5:
		customer_id = raw_input("Enter the customer id :")
		address = get_random_address()
		update_customer_by_customer_id(customer_id,api_key,address)
	else:
		print("Wrong input. Please try again!!")
		return

### 1. Create a new customer
### 2. Get A customer by account Id
### 3. Get A customer by customer Id
### 4. Get All customers
### 5. Update customer by customer Id

if __name__ == '__main__':
	option = input("Enter the task you want to perform :")
	task_to_perform(option)