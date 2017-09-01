from random import choice
import json

class Actor:
	def __init__(self,name="Foufoutos", sayings_list=["I am the mighty Foufoutos! Hear me roar!", "Raaaaah!", "GRAAAAAAH!", "Prepare to embrace your creators in the stygian haunts of hell!"]):
		self.name=name
		self.sayings=sayings_list
	def speak(self,criteria=True):
		return (choice(self.sayings))

def load_Actor(filename):
	#loads an actor from a json filename and returns an Actor instance initialized with the loaded one
	try:
	    with open(filename) as data_file:
		    actor_data=json.load(data_file)
	except: 
		print ("Error in reading "+filename)
		return None
	if 'name' not in actor_data or 'sayings_list' not in actor_data:
		print ("Wrong data file")
		return None
	else: return Actor(actor_data['name'],actor_data['sayings_list'])

def save_Actor(actor,filename):
	try:
		dump_dict={}
		dump_dict['name']=actor.name
		dump_dict['sayings_list']=actor.sayings
		with open(filename, 'w') as outfile:
			json.dump(dump_dict, outfile)
	except:
		print ("Could not save to "+ filename)
		return None
	
	
def main():
	#this is a test function to check and Demo actors functionality
	a=Actor()
	for i in range(10): print (a.speak())
	b=load_Actor('document.json')
	if not b: print ("Load Failed!")
	else: 
		print (b.name+" loaded!")
		for i in range(10): print(b.speak())
	save_Actor(a,'testme.json')
		
if __name__ == '__main__':
    main()
