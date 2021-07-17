import unittest
from ParkingLot import ParkingLot

class TestParkingLot(unittest.TestCase):

	def test_create_parking_lot(self):
		parkingLot = ParkingLot()
		res = parkingLot.createParkingSlots(6)
		self.assertEqual(6,res)

	def test_park(self):
		parkingLot = ParkingLot()
		res = parkingLot.createParkingSlots(6)
		res = parkingLot.park("KA-01-HH-1234", 21)
		self.assertNotEqual(-1, res)

	def test_leave(self):
		parkingLot = ParkingLot()
		res = parkingLot.createParkingSlots(6)
		res = parkingLot.park("KA-01-HH-1234", 21)
		res = parkingLot.leave(1)
		self.assertEqual("KA-01-HH-1234", res['regNo'])

	def test_getRegNosFromDriverAge(self):
		parkingLot = ParkingLot()
		res = parkingLot.createParkingSlots(6)
		res = parkingLot.park("KA-01-HH-1234", 21)
		res = parkingLot.park("PB-01-TG-2341", 21)
		regnos = parkingLot.getRegNosFromDriverAge( 21)
		self.assertIn("KA-01-HH-1234",regnos)
		self.assertIn("PB-01-TG-2341",regnos)

	def test_getSlotFromRegNo(self):
		parkingLot = ParkingLot()
		res = parkingLot.createParkingSlots(6)
		res = parkingLot.park("KA-01-HH-1234", 21)
		res = parkingLot.park("PB-01-TG-2341", 21)
		slotno = parkingLot.getSlotFromRegNo("PB-01-TG-2341")
		self.assertEqual(2,slotno)

		slotno = parkingLot.getSlotFromRegNo("PB-01-TG-2341")
		self.assertEqual(2,slotno)

	def test_getSlotsFromDriverAge(self):
		parkingLot = ParkingLot()
		res = parkingLot.createParkingSlots(6)
		res = parkingLot.park("KA-01-HH-1234", 21)
		res = parkingLot.park("PB-01-TG-2341", 21)
		slotnos = parkingLot.getSlotsFromDriverAge( 21)
		self.assertIn("1",slotnos)
		self.assertIn("2",slotnos)

	# Fail Cases

	def test_park_fail(self):
		parkingLot = ParkingLot()
		res = parkingLot.createParkingSlots(1)
		res = parkingLot.park("KA-01-HH-1234", 21)
		res = parkingLot.park("KL-03-MH-3333", 21)
		self.assertEqual(-1, res)

	def test_getSlotFromRegNo_fail(self):
		parkingLot = ParkingLot()
		res = parkingLot.createParkingSlots(6)
		res = parkingLot.park("KA-01-HH-1234", 21)
		res = parkingLot.park("PB-01-TG-2341", 21)
		slotno = parkingLot.getSlotFromRegNo("PB-01-TG-2340")
		self.assertEqual(-1,slotno)

if __name__ == '__main__':
    unittest.main()