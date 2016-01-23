import requests
import json
from random import randint
import string
import names

customer_id = '56a33f7a957f400e00aa8eb8'
api_key = '963adb712062f1bd2057a6e4063a9c06'
account_number_length = 16

def get_account_details_by_account_type(account_type,api_key):
	url = 'http://api.reimaginebanking.com/accounts?type={}&key={}'.format(account_type,api_key)

	# Getting a Savings Account by account type
	response = requests.get(url)

	if response.status_code == 200:
		accounts = json.loads(response.content)
		i = 0
		for account in accounts:
			i +=1
			print "Account:{}".format(i)
			print("Id:"+account["_id"])
			print("type:"+account["type"])
			print("nickname :"+account["nickname"])
			print("customer_id :"+account["customer_id"])
			print("balance :"+str(account["balance"]))
			print("rewards :"+str(account["rewards"]))
			print("\n\n")
	else:
	    print('Account Does not exist for customer with id'+customer_id)
	
def get_account_details_by_customer_id(customer_id,api_key):
	url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customer_id,api_key)

	# Getting a Savings Account by customer id
	response = requests.get(url)
	
	if response.status_code == 200:
		accounts = json.loads(response.content)
		i = 0
		for account in accounts:
			i +=1
			print "Account:{}".format(i)
			print("Id:"+account["_id"])
			print("type:"+account["type"])
			print("nickname :"+account["nickname"])
			print("customer_id :"+account["customer_id"])
			print("balance :"+str(account["balance"]))
			print("rewards :"+str(account["rewards"]))
			print("\n\n")
	else:
	    print('Account Does not exist for customer with id '+customer_id)

	
def get_account_details_by_account_id(account_id,api_key):
	url = 'http://api.reimaginebanking.com/accounts/{}?key={}'.format(account_id,api_key)
	
	# Getting a Savings Account by account id
	response = requests.get(url)

	if response.status_code == 200:
		account = json.loads(response.content)
		print("type:"+account["type"])
		print("Id:"+account["_id"])
		print("nickname :"+account["nickname"])
		print("customer_id :"+account["customer_id"])
		print("balance :"+str(account["balance"]))
		print("rewards :"+str(account["rewards"]))
	else:
	    print('Account Does not exist for customer with id'+customer_id)


def create_account_by_customer_id(customer_id,api_key,nickname,account_number):
	url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customer_id,api_key)
	payload = {
	  "type": "Savings",
	  "nickname": nickname,
	  "rewards": 10000,
	  "balance": 10000,
	  "account_number":account_number
	}

	# Create a Savings Account
	response = requests.post( 
		url, 
		data=json.dumps(payload),
		headers={'content-type':'application/json'},
		)

	if response.status_code == 201:
		print('account created')
		account = json.loads(response.content)["objectCreated"]
		print("type:"+account["type"])
		print("Id:"+account["_id"])	
		print("nickname :"+account["nickname"])
		print("customer_id :"+account["customer_id"])
		print("balance :"+str(account["balance"]))
		print("rewards :"+str(account["rewards"]))
		print "account number:", account_number
	else:
	    print('Error in creating account')


def update_account_by_account_id(account_id,api_key,nickname,account_number):
	url = 'http://api.reimaginebanking.com/accounts?key={}'.format(account_id,api_key)
	payload = {
	  "nickname": nickname,
	  "account_number": account_number
	}

	# Update Account by account id
	response = requests.put( 
		url, 
		data=json.dumps(payload),
		headers={'content-type':'application/json'},
		)

	if response.status_code == 202:
		print('account created')
		account = json.loads(response.content)
		print("Message:"+account["message"])
	else:
	    print('Error in updating account')

def delete_account_by_account_id(account_id,api_key):
	url = 'http://api.reimaginebanking.com/accounts/{}?key={}'.format(account_id,api_key)
	
	# Delete Account by account id
	response = requests.delete(url)

	if response.status_code == 204:
		print("Account with Id "+str(account_id)+ " deleted Successfully")
	else:
	    print('Error Deleting the account with id '+account_id)


def generate_random_account_number(number_length):
	start_range = 10**(number_length-1)
	end_range = 10**number_length
	return randint(start_range,end_range)

def generate_random_name():
   return names.get_last_name()


def task_to_perform(option):
	if option==1:
		account_number = str(generate_random_account_number(account_number_length))
		nickname = generate_random_name()
		#customer_id = raw_input("Enter the customer id :")
		create_account_by_customer_id(customer_id,api_key,nickname,account_number)
	elif option==2:
		#customer_id = raw_input("Enter the customer id :")
		get_account_details_by_customer_id(customer_id,api_key)
	elif option==3:
		account_type = raw_input("Enter the account type :")
		get_account_details_by_account_type(account_type,api_key)
	elif option==4:
		account_id = raw_input("Enter the account id :")
		get_account_details_by_account_id(account_id,api_key)
	elif option==5:
		account_id = raw_input("Enter the account id :")
		nickname = generate_random_name()
		account_number = str(generate_random_account_number(account_number_length))
		update_account_by_account_id(account_id,api_key,nickname,account_number)
	elif option==6:
		account_id = raw_input("Enter the account id :")
		delete_account_by_account_id(account_id,api_key)
	else:
		print("Wrong input. Please try again!!")
		return
	#account_id = '56a33f9c957f400e00aa8eb9'
	#get_account_details_by_account_id(account_id,api_key)
	#get_account_details_by_customer_id(customer_id,api_key)
	# account_number = str(generate_random_account_number(account_number_length))
	# nickname = generate_random_name()
	# create_account_by_customer_id(customer_id,api_key,"test5")
	# account_number = str(generate_random_account_number(account_number_length))
	# nickname = generate_random_name()
	# update_account_by_account_id(account_id,api_key,nickname,account_number)
	#account_id = '56a33f9c957f400e00aa8eb9'
	#delete_account_by_account_id(account_id,api_key)


### 1. Create a new account for the customer
### 2. Get All Account Details by Customer Id
### 3. Get All Account Details by Account Type
### 4. Get Account Details by Account Id
### 5. Update Account by Account Id
### 6. Delete Account by Account Id
if __name__ == '__main__':
	option = input("Enter the task you want to perform :")
	task_to_perform(option)