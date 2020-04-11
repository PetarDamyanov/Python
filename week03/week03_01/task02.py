class Bill:
	def __init__(self,bill):
		if bill<1:
			raise ValueError("There is no zero or negative bills")
		self.bill=bill
	def __str__(self):
		return 'A {0}$ bill'.format(self.bill)
	def __repr__(self):
		return "{0} bill".format(self.bill)
	def __int__(self):
		return int(self.bill)
	def __eq__(self,other):
		return self.bill==other.bill
	def __hash__(self):
		return hash(self.bill)
	def __add__(self,other):
		return self.bill+other.bill
	def __iadd__(self,num):
		return self.bill+num

class BillBatch:
	def __init__(self,lst):
		self.lst=lst
	def __len__(self):
		return len(self.lst)
	def total(self):
		sum=0
		for x in self.lst:
			sum+=int(x)
		return sum
	def __getitem__(self,index):
		return self.lst[index]

class CashDesk:
	def __init__(self,lst=None):
		if lst!=None:
			self.lst=lst
		else:
			self.lst=[]
	def take_money(self,lst=None,n=None):
		if lst==None:
			self.lst.append(Bill(n))
		if n==None:
			for x in lst:
				self.lst.append(x)		
	def total(self):
		sum=0
		for x in self.lst:
			sum+=int(x)
		return sum
	def inspect(self):
		l_checked=[]
		for x in self.lst:
			if l_checked.count(int(x))==0:
				l_checked.append(int(x))
				print("{0}-{1}".format(str(x),self.lst.count(x)))
	def __getitem__(self,index):
		return self.lst[index]

if __name__ == '__main__':
	main()