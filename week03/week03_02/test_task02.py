import unittest
from task02 import Song,Playlist
class TestSongCls(unittest.TestCase):
	"""docstring for TestSongCls"""
	def test_str_of_song_cls(self):
		t1=Song("Odin", "Manowar", "The Sons of Odin", "3:44")
		te="Manowar-Odin from The Sons of Odin-3:44"
		self.assertEqual(str(t1),te)
	
	def test_str_of_song_cls_len_bigger_hour(self):
		t1=Song("Odin", "Manowar", "The Sons of Odin", "1:3:44")
		te="Manowar-Odin from The Sons of Odin-1:3:44"
		self.assertEqual(str(t1),te)
	def test_eq_song_cls_true(self):
		t1=Song("Odin", "Manowar", "The Sons of Odin", "1:3:44")
		t2=Song("Odin", "Manowar", "The Sons of Odin", "1:3:44")
		
		self.assertTrue(t1==t2)
	def test_eq_song_cls_false(self):
		t1=Song("Odin", "Manowar", "The Sons of Odin", "1:3:44")
		t2=Song("Odin1", "Manowar", "The Sons of Odin", "1:3:44")
		
		self.assertFalse(t1==t2)
	def test_hash_song_cls(self):
		t1=Song("Odin", "Manowar", "The Sons of Odin", "1:3:44")
		self.assertTrue(hash(t1)==hash('1:3:44'))
	def test_time_song_cls_full_len_seconds(self):
		t1=Song("Odin", "Manowar", "The Sons of Odin", "1:3:44")
		self.assertEqual(t1.length2(seconds=True),'44s')
	def test_time_song_cls_full_len_minutes(self):
		t1=Song("Odin", "Manowar", "The Sons of Odin", "1:3:44")
		self.assertEqual(t1.length2(minutes=True),'3m')
	def test_time_song_cls_full_len_hours(self):
		t1=Song("Odin", "Manowar", "The Sons of Odin", "1:3:44")
		self.assertEqual(t1.length2(hours=True),'1h')
	def test_time_song_cls_noHOur_len_hours(self):
		t1=Song("Odin", "Manowar", "The Sons of Odin", "3:44")
		self.assertEqual(t1.length2(hours=True),'no hours')
	def test_time_song_cls_no_hour_len_min(self):
		t1=Song("Odin", "Manowar", "The Sons of Odin", "3:44")
		self.assertEqual(t1.length2(minutes=True),'3m')



class TestPlayList(unittest.TestCase):
	def test_playlist_cls_add_one_song(self):
		pl=Playlist("te")
		ts1=Song("Odin12", "Manowar31", "The Sons123 of Odin", "3:44")
		# t2=Song("Odin", "Manowar", "The Sons of Odin", "3:44")
		try:
			pl.add_song(ts1)
			# pl.add_song(t2)
		except Exception as e:
			raise e
		# print(len(pl1))
		# print(len(pl))
		self.assertTrue(len(pl)==1)
	def test_playlist_cls_remove_one_song(self):
		pl2=Playlist("test21")
		tsr1=Song("Odin", "Manowar", "The Sons of Odin", "3:44")
		# t2=Song("Odin", "Manowar", "The Sons of Odin", "3:44")
		try:
			pl2.add_song(tsr1)
			pl2.remove_song(tsr1)
			# pl.add_song(t2)
		except Exception as e:
			raise e
		print(len(pl2))
		self.assertTrue(len(pl2)==0)
	def test_playlist_cls_add_list_songs(self):
		pl3=Playlist("test3")
		t1=Song("Odin1", "Manowar1", "The Sons of Odin1", "23:24")
		t2=Song("Odin2", "Manowar2", "The Sons of Odin2", "13:44")
		t3=Song("Odin3", "Manowar3", "The Sons of Odin3", "23:44")
		try:
			# pl.add_song(t1)
			pl3.add_songs([t1,t2,t3])
			# pl.add_song(t2)
		except Exception as e:
			raise e
		self.assertTrue(len(pl3)==3)



	def test_playlist_cls_legnth_total(self):
		pl=Playlist("test3")
		t1=Song("Odin1", "Manowar1", "The Sons of Odin1", "23:24")
		t2=Song("Odin2", "Manowar2", "The Sons of Odin2", "13:44")
		t3=Song("Odin3", "Manowar3", "The Sons of Odin3", "23:44")
		try:
			pl.add_songs([t1,t2,t3])
		except Exception as e:
			raise e
		self.assertTrue(pl.total_lenght()=="1:0:52")

	def test_playlist_cls_add_list_songs(self):
		pl3=Playlist("test3")
		t1=Song("Odin1", "Manowar", "The Sons of Odin1", "23:24")
		t2=Song("Odin2", "Manowar", "The Sons of Odin2", "13:44")
		t3=Song("Odin3", "Manowar3", "The Sons of Odin3", "23:44")
		try:
			pl3.add_songs([t1,t2,t3])
		except Exception as e:
			raise e
		# pl3.artists()
		# self.assertTrue(len(pl3)==3)
	def test_playlist_cls_next_song_no_stuff(self):
		pl=Playlist("test3")
		t1=Song("Odin1", "Manowar", "The Sons of Odin1", "23:24")
		t2=Song("Odin2", "Manowar", "The Sons of Odin2", "13:44")
		t3=Song("Odin3", "Manowar3", "The Sons of Odin3", "23:44")
		s=t2
		try:
			pl.add_songs([t1,t2,t3])
		except Exception as e:
			raise e
		try:
			h=pl.next_song()
		except Exception as e:
			raise e
		self.assertEqual(str(h),str(s))
			# self.assertTrue(len(pl3)==3)
	def test_playlist_cls_next_song_repeat(self):
		pl=Playlist("test3",repeat=True)
		t1=Song("Odin1", "Manowar", "The Sons of Odin1", "23:24")
		t2=Song("Odin2", "Manowar", "The Sons of Odin2", "13:44")
		t3=Song("Odin3", "Manowar3", "The Sons of Odin3", "23:44")
		s=t1
		try:
			pl.add_songs([t1,t2,t3])
		except Exception as e:
			raise e
		try:
			pl.next_song()
			h=pl.next_song()
			# pl.next_song()
			# for x in range(1,6):
			# 	print(pl.next_song())
		except Exception as e:
			raise e
		self.assertEqual(str(h),str(s))
			# self.assertTrue(len(pl3)==3)
	def test_playlist_cls_next_song_shuffle(self):
		pl=Playlist("test3",shuffle=True)
		t1=Song("Odin1", "Manowar", "The Sons of Odin1", "23:24")
		t2=Song("Odin2", "Manowar", "The Sons of Odin2", "13:44")
		t3=Song("Odin3", "Manowar3", "The Sons of Odin3", "23:44")
		s=t2
		try:
			pl.add_songs([t1,t2,t3])
		except Exception as e:
			raise e
		try:
			h=pl.next_song()
		except Exception as e:
			raise e
		self.assertEqual(str(h),str(s))

if __name__ == '__main__':
	unittest.main()