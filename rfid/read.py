import mfrc522
from os import uname


def do_read(addr):

	if uname()[0] == 'WiPy':
		rdr = mfrc522.MFRC522("GP14", "GP16", "GP15", "GP22", "GP17")
	elif uname()[0] == 'esp8266':
		rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)
	elif uname()[0] == 'esp32':
		rdr = mfrc522.MFRC522(18, 23, 19, 22, 2)
	else:
		raise RuntimeError("Unsupported platform")

	print("")
	print("Place card before reader to read from address 0x08")
	print("")

	try:
		flag = 1
		while flag:

			(stat, tag_type) = rdr.request(rdr.REQIDL)

			if stat == rdr.OK:

				(stat, raw_uid) = rdr.anticoll()

				if stat == rdr.OK:
					print("New card detected")
					print("  - tag type: 0x%02x" % tag_type)
					print("  - uid	 : 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
					print("")

					if rdr.select_tag(raw_uid) == rdr.OK:

						key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

						if rdr.auth(rdr.AUTHENT1A, addr, key, raw_uid) == rdr.OK:
							info = rdr.read(addr)
							info1 = ""
							for x in info:
								info1 = info1 + chr(x)

							info1 = info1.split()

							print("Address 8 data: %s" % info1[0])
							rdr.stop_crypto1()
							flag = 0
							return info1[0]
						else:
							print("Authentication error")
					else:
						print("Failed to select tag")

	except KeyboardInterrupt:
		print("Bye")