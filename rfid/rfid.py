import mfrc522
from os import uname
import struct

_NAMEREGISTER = 8
_LASTNAMEREGISTER = 9


if uname()[0] == 'WiPy':
	rdr = mfrc522.MFRC522("GP14", "GP16", "GP15", "GP22", "GP17")
elif uname()[0] == 'esp8266':
	rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)
elif uname()[0] == 'esp32':
	rdr = mfrc522.MFRC522(18, 23, 19, 22, 2)
else:
	raise RuntimeError("Unsupported platform")

def do_write(addr,name):

	if uname()[0] == 'WiPy':
		rdr = mfrc522.MFRC522("GP14", "GP16", "GP15", "GP22", "GP17")
	elif uname()[0] == 'esp8266':
		rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)
	elif uname()[0] == 'esp32':
		rdr = mfrc522.MFRC522(18, 23, 19, 22, 2)
	else:
		raise RuntimeError("Unsupported platform")

	for x in range(len(name),16):
		name = " " + name

	name1 = []

	for x in range(0,16):
		y = struct.unpack('B',str.encode(name[x]))
		name1 = name1 + [y[0]]

	# print(name)
	# print(name1)

	# print("")
	# print("Place card before reader to write")
	# print("")

	try:
		flag = 1
		while flag:

			(stat, tag_type) = rdr.request(rdr.REQIDL)

			if stat == rdr.OK:

				(stat, raw_uid) = rdr.anticoll()

				if stat == rdr.OK:
					# print("New card detected")
					# print("  - tag type: 0x%02x" % tag_type)
					# print("  - uid	 : 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
					# print("")

					if rdr.select_tag(raw_uid) == rdr.OK:

						key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
						if rdr.auth(rdr.AUTHENT1A, addr, key, raw_uid) == rdr.OK:
							stat = rdr.write(addr, name1)
							rdr.stop_crypto1()
							if stat == rdr.OK:
								print("Data written to card")
								flag = 0
							else:
								print("Failed to write data to card")
						else:
							print("Authentication error")
					else:
						print("Failed to select tag")

	except KeyboardInterrupt:
		print("Bye")

def do_read(addr):

	if uname()[0] == 'WiPy':
		rdr = mfrc522.MFRC522("GP14", "GP16", "GP15", "GP22", "GP17")
	elif uname()[0] == 'esp8266':
		rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)
	elif uname()[0] == 'esp32':
		rdr = mfrc522.MFRC522(18, 23, 19, 22, 2)
	else:
		raise RuntimeError("Unsupported platform")

	# print("")
	# print("Place card before reader to read")
	# print("")

	try:
		flag = 1
		while flag:

			(stat, tag_type) = rdr.request(rdr.REQIDL)

			if stat == rdr.OK:

				(stat, raw_uid) = rdr.anticoll()

				if stat == rdr.OK:
					# print("New card detected")
					# print("  - tag type: 0x%02x" % tag_type)
					# print("  - uid	 : 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
					# print("")

					if rdr.select_tag(raw_uid) == rdr.OK:

						key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

						if rdr.auth(rdr.AUTHENT1A, addr, key, raw_uid) == rdr.OK:
							info = rdr.read(addr)
							info1 = ""
							for x in info:
								info1 = info1 + chr(x)

							info1 = info1.split()

							#print("Address 8 data: %s" % info1[0])
							rdr.stop_crypto1()
							flag = 0
							return info1[0]
						else:
							print("Authentication error")
					else:
						print("Failed to select tag")

	except KeyboardInterrupt:
		print("Bye")

def read_name():

	return do_read(_NAMEREGISTER)

def read_lastname():

	return do_read(_LASTNAMEREGISTER)

def write_name(name):

	return do_write(_NAMEREGISTER,name)

def write_lastname(name):

	return do_write(_LASTNAMEREGISTER,name)

def wname(name,lastname):

	print("")
	print("Place card before reader to write")
	print("")

	write_name(name)
	write_lastname(lastname)
	print("ok")

def rname():

	print("")
	print("Place card before reader to read")
	print("")

	print(read_name(),read_lastname())