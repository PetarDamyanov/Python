from random import randint
class Song(object):
	title="Unknown"
	artist="Unknown"
	album="Unknown"
	length="Undefiend"
	def __init__(self, name,artist,album,length):
		self.title=name
		self.artist=artist
		self.album=album
		if len(length.split(':'))>=2:
			self.length=length
		else:
			raise Exception('Invalid song length')
	def __str__(self):
		return "{0}-{1} from {2}-{3}".format(self.artist,self.title,self.album,self.length)
	def __eq__(self,other):
		return self.length==other.length and self.title==other.title and self.artist==other.artist
	def __hash__(self):
		return hash(self.length)
	def length2(self,seconds=False,minutes=False,hours=False):
		h=s=m=0
		if len(self.length.split(':'))>2:
			h=int(self.length.split(':')[0])
			m=int(self.length.split(':')[1])
			s=int(self.length.split(':')[2])
		else:
			s=int(self.length.split(':')[1])
			m=int(self.length.split(':')[0])
		if seconds==True:
			return '{0}s'.format(s)
		if minutes== True:
			return '{0}m'.format(m)
		if hours==True and h!=0:
			return '{0}h'.format(h)
		elif h==0:
			return 'no hours'
		if h:
			return "{0}:{1}:{2}".format(h,m,s)
		else:
			return "{0}:{1}".format(m,s)

class Playlist:
	name="No name"
	lst=[]
	repeat=False
	shuffle=False
	counter=0
	played=[]
	def __init__(self, name,repeat=False,shuffle=False):
		self.name=name
		if repeat==True:
			self.repeat=True
		if shuffle==True:
			self.shuffle=True
		self.lst=[]
	def add_song(self,song):
		if self.lst.count(song)==0:
			self.lst.append(song)
		else:
			print("song is in playlist")
	def remove_song(self,song):
		if self.lst.count(song)==1:
			self.lst.remove(song)
		else:
			print("Song not found in pl")
	def add_songs(self,lst):
		for x in lst:
			self.add_song(x)	
	def total_lenght(self):
		s=m=h=0
		for x in self.lst:
			if len(x.length.split(':'))>2:
				s+=int(x.length.split(':')[2])
				m+=int(x.length.split(':')[1])
				h+=int(x.length.split(':')[0])
			else:
				s+=int(x.length.split(':')[1])
				m+=int(x.length.split(':')[0])
		while s>59:
			s-=60
			m+=1
		while m>59:
			m-=60
			h+=1
		return "{0}:{1}:{2}".format(h,m,s)
	
	def __getittem__(self,index):
		return self.lst[index]

	def artists(self):
		l_cheked=[]
		for x in self.lst:
			if l_cheked.count(x.artist)==0:
				print("{0}->{1}".format(x.artist,self.lst.count(x)))

				print(x.artist)
				l_cheked.append(x.artist)
	
	def next_song(self):
		# played=[]
		if self.repeat==True:
			self.counter+=1
			if self.counter==len(self.lst)-1:
				self.counter=0
			return self.lst[self.counter]
		if self.shuffle==True:
			self.counter+=1
			if self.counter==len(self.lst)-1:
				self.counter=0
				self.played=[]
			n=randint(0,len(self.lst)-1)
			for x in self.played:
				while self.played.count(self.lst[n])==0:
					n=randint(0,len(self.lst))

			self.played.append(self.lst[n])
			return self.lst[n]
		if self.counter<len(self.lst):
			self.counter+=1
		return self.lst[self.counter]
					
	def __len__(self):
		return len(self.lst)
