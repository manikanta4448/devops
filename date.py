import webbrowser as wb

while True:
	print("enter u r choice:")
	ch = input()

	if "date" in ch:
		wb.open("http://192.168.8.172/cgi-bin/hi.py?x=date&p=")
	elif "cal" in ch:
		wb.open("http://192.168.8.172/cgi-bin/hi.py?x=cal&p=")
	elif "ls" in ch:
		wb.open("http://192.168.8.172/cgi-bin/hi.py?x=ls&p=")
	elif "exit" in ch:
		break
	else:
		print("dont understand")