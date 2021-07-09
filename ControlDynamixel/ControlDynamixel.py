#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file ControlDynamixel.py
 @brief ControlDynamixel
 @date $Date$

 @author 大塩晃平

"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

# Import DynamixelSDK
from dynamixel_sdk import *
PROTOCOL_VERSION            = 1.0
TORQUE_ENABLE               = 1
TORQUE_DISABLE              = 0

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
controldynamixel_spec = ["implementation_id", "ControlDynamixel",
		 "type_name",         "ControlDynamixel",
		 "description",       "ControlDynamixel",
		 "version",           "1.0.0",
		 "vendor",            "OshioKohei",
		 "category",          "Actuator",
		 "activity_type",     "STATIC",
		 "max_instance",      "1",
		 "language",          "Python",
		 "lang_type",         "SCRIPT",
		 "conf.default.ADDR_MX_TORQUE_ENABLE", "64",
		 "conf.default.ADDR_MX_GOAL_POSITION", "116",
		 "conf.default.ADDR_MX_PRESENT_POSITION", "132",
		 "conf.default.DXL_ID", "1",
		 "conf.default.BAUDRATE", "57600",
		 "conf.default.DEVICENAME", "COM4",
		 "conf.default.DXL_MOVING_STATUS_THRESHOLD", "10",

		 "conf.__widget__.ADDR_MX_TORQUE_ENABLE", "text",
		 "conf.__widget__.ADDR_MX_GOAL_POSITION", "text",
		 "conf.__widget__.ADDR_MX_PRESENT_POSITION", "text",
		 "conf.__widget__.DXL_ID", "text",
		 "conf.__widget__.BAUDRATE", "text",
		 "conf.__widget__.DEVICENAME", "text",
		 "conf.__widget__.DXL_MOVING_STATUS_THRESHOLD", "text",

         "conf.__type__.ADDR_MX_TORQUE_ENABLE", "int",
         "conf.__type__.ADDR_MX_GOAL_POSITION", "int",
         "conf.__type__.ADDR_MX_PRESENT_POSITION", "int",
         "conf.__type__.DXL_ID", "int",
         "conf.__type__.BAUDRATE", "long",
         "conf.__type__.DEVICENAME", "string",
         "conf.__type__.DXL_MOVING_STATUS_THRESHOLD", "int",

		 ""]
# </rtc-template>

##
# @class ControlDynamixel
# @brief ControlDynamixel
#
# サーボモータDynamixel(Protocol1.0)を動かすコンポーネントです。
#
# 角度[deg]を入力します。
#
#
class ControlDynamixel(OpenRTM_aist.DataFlowComponentBase):

	##
	# @brief constructor
	# @param manager Maneger Object
	#
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_angle_input = OpenRTM_aist.instantiateDataType(RTC.TimedDouble)
		"""
		"""
		self._angle_inputIn = OpenRTM_aist.InPort("angle_input", self._d_angle_input)



		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		"""
		
		 - Name:  ADDR_MX_TORQUE_ENABLE
		 - DefaultValue: 64
		"""
		self._ADDR_MX_TORQUE_ENABLE = [64]
		"""
		
		 - Name:  ADDR_MX_GOAL_POSITION
		 - DefaultValue: 116
		"""
		self._ADDR_MX_GOAL_POSITION = [116]
		"""
		
		 - Name:  ADDR_MX_PRESENT_POSITION
		 - DefaultValue: 132
		"""
		self._ADDR_MX_PRESENT_POSITION = [132]
		"""
		
		 - Name:  DXL_ID
		 - DefaultValue: 1
		"""
		self._DXL_ID = [1]
		"""
		
		 - Name:  BAUDRATE
		 - DefaultValue: 57600
		"""
		self._BAUDRATE = [57600]
		"""
		
		 - Name:  DEVICENAME
		 - DefaultValue: COM4
		"""
		self._DEVICENAME = ['COM4']
		"""
		
		 - Name:  DXL_MOVING_STATUS_THRESHOLD
		 - DefaultValue: 10
		"""
		self._DXL_MOVING_STATUS_THRESHOLD = [10]

		self._portHandler = None
		self._packetHandler = None

		# </rtc-template>



	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry()
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		self.bindParameter("ADDR_MX_TORQUE_ENABLE", self._ADDR_MX_TORQUE_ENABLE, "64")
		self.bindParameter("ADDR_MX_GOAL_POSITION", self._ADDR_MX_GOAL_POSITION, "116")
		self.bindParameter("ADDR_MX_PRESENT_POSITION", self._ADDR_MX_PRESENT_POSITION, "132")
		self.bindParameter("DXL_ID", self._DXL_ID, "1")
		self.bindParameter("BAUDRATE", self._BAUDRATE, "57600")
		self.bindParameter("DEVICENAME", self._DEVICENAME, "COM4")
		self.bindParameter("DXL_MOVING_STATUS_THRESHOLD", self._DXL_MOVING_STATUS_THRESHOLD, "10")

		# Set InPort buffers
		self.addInPort("angle_input",self._angle_inputIn)

		# Set OutPort buffers

		# Set service provider to Ports

		# Set service consumers to Ports

		# Set CORBA Service Ports

		return RTC.RTC_OK

	###
	##
	## The finalize action (on ALIVE->END transition)
	## formaer rtc_exiting_entry()
	##
	## @return RTC::ReturnCode_t
	#
	##
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK

	###
	##
	## The startup action when ExecutionContext startup
	## former rtc_starting_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The shutdown action when ExecutionContext stop
	## former rtc_stopping_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK

	##
	#
	# The activated action (Active state entry action)
	# former rtc_active_entry()
	#
	# @param ec_id target ExecutionContext Id
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onActivated(self, ec_id):

		print('Activate')
		# PortHandler初期化
		self._portHandler = PortHandler(self._DEVICENAME[0])
		# PacketHandler初期化
		self._packetHandler = PacketHandler(PROTOCOL_VERSION)
		# ポートオープン
		if self._portHandler.openPort():
			print('Succeeded to open the port')
		else:
			print("Failed to open the port")
                # Baudrate設定
		if self._portHandler.setBaudRate(self._BAUDRATE[0]):
			print("Succeeded to change the baudrate")
		else:
			print("Failed to change the baudrate")
                # トルクON
		dxl_comm_result, dxl_error = self._packetHandler.write1ByteTxRx(self._portHandler, self._DXL_ID[0], self._ADDR_MX_TORQUE_ENABLE[0], TORQUE_ENABLE)
		if dxl_comm_result != COMM_SUCCESS:
			print("%s" % self._packetHandler.getTxRxResult(dxl_comm_result))
		elif dxl_error != 0:
			print("%s" % self._packetHandler.getRxPacketError(dxl_error))
		else:
			print("Dynamixel has been successfully connected")
		return RTC.RTC_OK

	##
	#
	# The deactivated action (Active state exit action)
	# former rtc_active_exit()
	#
	# @param ec_id target ExecutionContext Id
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onDeactivated(self, ec_id):
		print('Deativate')

		return RTC.RTC_OK

	##
	#
	# The execution action that is invoked periodically
	# former rtc_active_do()
	#
	# @param ec_id target ExecutionContext Id
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onExecute(self, ec_id):
		if self._angle_inputIn.isNew() is True:
			dxl_goal_position = int(self._angle_inputIn.read().data * 1024.0 / 90.0)
			dxl_present_position, dxl_comm_result, dxl_error = self._packetHandler.read2ByteTxRx(self._portHandler, self._DXL_ID[0], self._ADDR_MX_PRESENT_POSITION[0])
			if dxl_comm_result != COMM_SUCCESS:
				print("%s" % self._packetHandler.getTxRxResult(dxl_comm_result))
			elif dxl_error != 0:
				print("%s" % self._packetHandler.getRxPacketError(dxl_error))
			# print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (self._DXL_ID[0], dxl_goal_position, dxl_present_position))
			if dxl_present_position==65535:
				dxl_present_position=0
			if abs(dxl_goal_position - dxl_present_position) > self._DXL_MOVING_STATUS_THRESHOLD[0]:
				dxl_comm_result, dxl_error = self._packetHandler.write4ByteTxRx(self._portHandler, self._DXL_ID[0], self._ADDR_MX_GOAL_POSITION[0], dxl_goal_position)
		return RTC.RTC_OK

	###
	##
	## The aborting action when main logic error occurred.
	## former rtc_aborting_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The error action in ERROR state
	## former rtc_error_do()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The reset action that is invoked resetting
	## This is same but different the former rtc_init_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The state update action that is invoked after onExecute() action
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##

	##
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The action that is invoked when execution context's rate is changed
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK




def ControlDynamixelInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=controldynamixel_spec)
    manager.registerFactory(profile,
                            ControlDynamixel,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    ControlDynamixelInit(manager)

    # Create a component
    comp = manager.createComponent("ControlDynamixel")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

