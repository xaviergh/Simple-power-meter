#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import sys, serial, time, os
from PySide import QtGui, QtCore
from PowerMeterMain_Ui import Ui_MainWindow

SERIALPORT = '/dev/ttyS0'
BAUDRATE = 38400
 
class SerialThread(QtCore.QThread):
	
	dataReady = QtCore.Signal(list)
	
	def __init__(self, serial_port = SERIALPORT, baud_rate = BAUDRATE):
		QtCore.QThread.__init__(self)
		self.uart = serial.Serial(serial_port,baud_rate,timeout=0)
		self.write = False
		self.wbuffer = ''
		self.rbuffer = []
		self.rpayload = 0
		self.busy = False

	def send(self, string):
		self.wbuffer = string
		self.write = True

	def run(self):
		while True:

			if not self.write:
				if self.uart.inWaiting() > 0:
					#print hex(ord(self.uart.read(1)))
					self.rbuffer.append(ord(self.uart.read(1)))
					
					if self.rbuffer[-1] is 0xAA:
						#print "Data Init"
						self.busy = True

					elif self.busy is True:
						if self.rbuffer[-2] is 0xAA:
							self.rpayload = self.rbuffer[-1]
							#print "Payload: %d" %self.rpayload
						elif(self.rpayload is 0):
							print self.rbuffer
							self.dataReady.emit(self.rbuffer)
							self.rbuffer = []
							self.busy = False
						else:
							self.rpayload -= 1

			else:
				self.uart.write(self.wbuffer)
				self.uart.flush() #wait for all data to be written
				self.wbuffer = ''
				self.write = False

class Main(QtGui.QMainWindow):

	startTxData = 0xA5
	deviceId = 0x00
	getPowerFactorA = [0x05,0xA0,0x02]
	getPhaseAngleA = [0x05,0xAC,0x02]
	getVoltageA = [0x05,0x10,0x04]
	getCurrentA = [0x05,0x04,0x04]
	getPowerA = [0x05,0x1C,0x04]
	global dataType #1: PF 2: Volt 3: Current 4: Power

	def __init__(self, parent=None):
		super(Main, self).__init__(parent)
		#QtGui.QDialog.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.uart = SerialThread()
		self.uart.start()

		self.uart.dataReady.connect(self.parseUart,QtCore.Qt.QueuedConnection)

		#Timed events
		self.timer = QtCore.QTimer(self)
		self.timer.timeout.connect(self.updateData) #update uart every 1s
		self.timer.start(1000)

		self.show()

	def updateData(self):
		global dataType
		dataType = 1
		self.sendData(self.startTxData,self.deviceId,self.getPowerFactorA)
		dataType = 2
		self.sendData(self.startTxData,self.deviceId,self.getVoltageA)
		dataType = 3
		self.sendData(self.startTxData,self.deviceId,self.getCurrentA)
		dataType = 4
		self.sendData(self.startTxData,self.deviceId,self.getPowerA)

	def calculateChecksum(self,data):

		chksum = sum(data)
		chksum = 256 - chksum%256
		#print "Checksum %d" %chksum
		return chksum

	def sendData(self,start,devId,data):
		
		global dataType

		dataPacket = []

		dataPacket.append(start)
		dataPacket.append(devId)
		dataPacket.append(len(data))
		dataPacket += data
		dataPacket.append(self.calculateChecksum(dataPacket))

		for i in dataPacket:
			self.sendUart(chr(i))

		while dataType is not 0:
			QtGui.QApplication.processEvents()

	def sendUart(self,data):
		while self.uart.busy or self.uart.write:
			pass
		self.uart.send(data)

	def make16(self,msb,lsb):

		return ((msb << 8) | lsb)

	def make32(self,msb,mid1,mid2,lsb):

		return ((msb << 24) | (mid1 << 16) | (mid2 << 8) | lsb)

	def parseUart(self,uartData):
		
		global dataType
		
		if dataType is 1: #powerfactor
			self.ui.lcdPowerFactorPhase1.display(self.make16(uartData[2],uartData[3])/1000.0)
			dataType = 0
		elif dataType is 2: #voltage
			self.ui.lcdVoltagePhase1.display(self.make32(uartData[2],uartData[3],uartData[4],uartData[5])/1000.0)
			dataType = 0
		elif dataType is 3: #current
			self.ui.lcdCurrentPhase1.display(self.make32(uartData[2],uartData[3],uartData[4],uartData[5])/1000.0)
			dataType = 0
		elif dataType is 4: #power
			self.ui.lcdPowerPhase1.display(self.make32(uartData[2],uartData[3],uartData[4],uartData[5])/10000000.0)
			self.ui.lcdPowerPhase12.display(self.make32(uartData[2],uartData[3],uartData[4],uartData[5])/10000000.0)
			dataType = 0
			
def main():
	app = QtGui.QApplication(sys.argv)
	m = Main()
	sys.exit(app.exec_())
 
if __name__ == '__main__':
	main()