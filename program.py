import requests
ID = input("ISBN: ")

url = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + ID

is_there_book = True

request = requests.get(url)

data = request.json()

vi = 'volumeInfo'
it = 'items'
default = 0

try:
	print(data[it][default][vi]['title'] + "\n")
except:
	is_there_book = False

if is_there_book:
	try:
		print(data[it][default][vi]['authors'])
	except:
		print('This book has no defined author \n')
	try:
		print(data[it][default][vi]['publishedDate'])
	except:
		print('This book has no defined date of publishing \n')
	try:
		print(data[it][default][vi]['categories'])
	except:
		print('This book has no defined categories \n')
	try:
		print(data[it][default][vi]['description'])
	except:
		print('Sorry, but there is no description for this book')
else:
	print("Sorry, either there is no book by the ISBN or the input is not valid")
