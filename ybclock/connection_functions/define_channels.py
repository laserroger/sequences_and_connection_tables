'''
Define the channels of all the NI DAC cards. They are seperated by device.
Hopefully, this will make learning the lab mechanism easier in the future.
'''
from labscript import AnalogOut, DigitalOut


def define_channels():
	blue_laser()
	red_laser()
	green_laser()
	magnetic_field()
	camera()
	photon_counter()

def blue_laser():
	AnalogOut(
		name         	= 'blue_power',
		parent_device	= ni_pci_6713_dev4,
		connection   	= 'ao0',
		limits       	= None
	)

	DigitalOut(
		name         	= 'blue_mot_aom_and_shutter',
		parent_device	= ni_pci_6284_dev6,
		connection   	= 'port0/line1'
	)

def red_laser():
	AnalogOut(
		name         	= 'red_power',
		parent_device	= ni_pci_6723_dev3,
		connection   	= 'ao0',
		limits       	= None
	)

def green_laser():
	AnalogOut(
		name         	= 'pump_aom_power',
		parent_device	= ni_pci_6713_dev5,
		connection   	= 'ao7',
	)

	AnalogOut(
		name         	= 'cooling_aom_power',
		parent_device	= ni_pci_6713_dev5,
		connection   	= 'ao6',
	)

	AnalogOut(
		name         	= 'green_power',
		parent_device	= ni_pci_6713_dev4,
		connection   	= 'ao4',
		limits       	= None
	)

	DigitalOut(
		name         	= 'green_mot_shutter',
		parent_device	= ni_pci_6284_dev6,
		connection   	= 'port0/line4'
	)

	DigitalOut(
		name         	= 'green_mot_aom',
		parent_device	= ni_pci_6284_dev6,
		connection   	= 'port0/line2'
	)

	DigitalOut(
		name         	= 'cooling_shutter',
		parent_device	= ni_pci_6284_dev6,
		connection   	= 'port0/line25'
	)

	DigitalOut(
		name         	= 'green_frequency_fpga_trigger',
		parent_device	= ni_pci_6284_dev6,
		connection   	= 'port0/line3'
	)


def magnetic_field():
	AnalogOut(
		name         	= 'x_bias_field',
		parent_device	= ni_pci_6713_dev4,
		connection   	= 'ao1',
		limits       	= None
	)

	AnalogOut(
		name         	= 'y_bias_field',
		parent_device	= ni_pci_6713_dev4,
		connection   	= 'ao2',
		limits       	= None
	)

	AnalogOut(
		name         	= 'z_bias_field',
		parent_device	= ni_pci_6713_dev4,
		connection   	= 'ao3',
		limits       	= None
	)

	#sets the voltage on the mot coil current controller.
	#for constant current mode, voltage needs to be larger than actual,
	#for constant voltage mode, current needs to be larger than actual.
	AnalogOut(
		name         	= 'mot_coil_current',
		parent_device	= ni_pci_6713_dev4,
		connection   	= 'ao5',
		limits       	= None
	)
	AnalogOut(
		name         	= 'mot_coil_voltage',
		parent_device	= ni_pci_6723_dev3,
		connection   	= 'ao3',
		limits       	= None
	)

def camera():
	'''
	The camera triggers are analog out's as they require 8V pulses to trigger.
	The channels will actually be defined in `define_hardware_cards.py`
	'''
	# AnalogOut(
	#	name         	= 'wide_range_camera_trigger',
	#	parent_device	= ni_pci_6713_dev5,
	#	connection   	= 'ao2',
	#	limits       	= (0, 8)
	# )

	# AnalogOut(
	#	name         	= 'one_to_one_camera_trigger',
	#	parent_device	= ni_pci_6713_dev5,
	#	connection   	= 'ao3',
	#	limits       	= (0,8)
	# )

def photon_counter():
	DigitalOut(
		name         	= 'p7888_start_trigger',
		parent_device	= ni_pci_6284_dev6,
		connection   	= 'port0/line11'
	)

	DigitalOut(
		name         	= 'p7888_flushing_trigger',
		parent_device	= ni_pci_6284_dev6,
		connection   	= 'port0/line15'
	)

