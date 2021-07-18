class ParkingLot:
    def __init__(self):
        self.totalSlots = 0
        self.totalOccupiedSlots = 0

    # Create a parking lot
    def createParkingSlots(self, totalSlots):
        if totalSlots > 0:
            self.totalSlots = totalSlots
            self.slots = [-1] * totalSlots
        return totalSlots

    # Get the next available slot to park a car
    def getNextSlot(self):
        for i in range(self.totalSlots):
            if self.slots[i] == -1:
                return i

    # Park a car in the next available slot
    def park(self, regNo, age):
        if self.totalOccupiedSlots < self.totalSlots:
            nextSlot = self.getNextSlot()
            self.slots[nextSlot] = {
                "regNo" : regNo,
                "age" : age
            }
            self.totalOccupiedSlots += 1
            return nextSlot + 1
        else:
            return -1
    
    # Get parking slots according to the driver's age
    def getSlotsFromDriverAge(self, age):
        slotNos = []
        for i in range(self.totalSlots):
            if self.slots[i] == -1:
                continue
            if self.slots[i]['age'] == age:
                slotNos.append(str(i+1))
        return slotNos
    
    # Get parking slot according to the vehicle register number
    def getSlotFromRegNo(self, regNo):
        for i in range(self.totalSlots):
            if self.slots[i] == -1:
                continue
            
            if self.slots[i]['regNo'] == regNo:
                return i+1
        return -1

    # Get vehicle register numbers according to the driver's age
    def getRegNosFromDriverAge(self, age):
        regNos = []
        for slot in self.slots:
            if slot == -1:
                continue
            if slot['age'] == age:
                regNos.append(slot['regNo'])
        return regNos

    # Leave a car from the parking lot
    def leave(self, slot):
        vehicle = {}
        if self.slots[slot-1] != -1:
            vehicle = self.slots[slot-1]
            self.slots[slot-1] = -1
            self.totalOccupiedSlots -= 1
        return vehicle

    # Display Outputs w.r.to input commands
    def parking(self, command):
        if command.startswith('Create_parking_lot'):
            totalSlots = int(command.split(' ')[1])
            res = self.createParkingSlots(totalSlots)
            if res > 0:
                print('Created parking of '+str(res)+' slot(s)')
            else:
                print('No parking lot found')
                exit(0)

        elif command.startswith('Park'):
            inputs = command.split(' ')
            regNo, age = inputs[1], inputs[3]
            res = self.park(regNo, age)
            if res != -1:
                print('Car with vehicle registration number "' + str(regNo) + '" has been parked at slot number ' + str(res))
            else:
                print("Sorry, parking lot is full")

        elif command.startswith('Slot_numbers_for_driver_of_age'):
            age = command.split(' ')[1]
            slotNos = self.getSlotsFromDriverAge(age)
            if len(slotNos):
                print(','.join(slotNos))
            else:
                print('No parked car matches the query')
        
        elif command.startswith('Vehicle_registration_number_for_driver_of_age'):
            age = command.split(' ')[1]
            regNos = self.getRegNosFromDriverAge(age)
            if len(regNos):
                print(','.join(regNos))
            else:
                print('No parked car matches the query')
        
        elif command.startswith('Slot_number_for_car_with_number'):
            regNo = command.split(' ')[1]
            slotNo = self.getSlotFromRegNo(regNo)
            if slotNo > 0:
                print(slotNo)
            else:
                print('No parked car matches the query')
        
        elif command.startswith('Leave'):
            slotNo = int(command.split(' ')[1])
            if slotNo > self.totalSlots:
                print('Invalid slot')
            else:
                vehicle = self.leave(slotNo)
                if 'regNo' in vehicle:
                    print('Slot number ' + str(slotNo) + ' vacated, the car with vehicle registration number "'+vehicle['regNo']+'" left the space, the driver of the car was of age '+vehicle['age'])
                else:
                    print('No parked car in slot ' + str(slotNo))
        
        else:
            print("Invalid command")
            
def main():
    filePath = 'input.txt' # Provided test cases
    # filePath = 'test_input.txt' # Manual test cases with edge cases 
    parkinglot = ParkingLot()
    with open(filePath) as inputFile:
        for command in inputFile:
            command = command.rstrip('\n')
            parkinglot.parking(command)

if __name__ == '__main__':
    main()