#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file ControlDynamixelTest.py
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


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
controldynamixeltest_spec = ["implementation_id", "ControlDynamixelTest",
		 "type_name",         "ControlDynamixelTest",
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
# @class ControlDynamixelTest
# @brief ControlDynamixel
#
# サーボモータDynamixel(Protocol1.0)を動かすコンポーネントです。
#
# 角度[deg]を入力します。
#
#
class ControlDynamixelTest(OpenRTM_aist.DataFlowComponentBase):

	##
	# @brief constructor
	# @param manager Maneger Object
	#
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_angle_input = OpenRTM_aist.instantiateDataType(RTC.TimedDouble)
		"""
		"""
		self._angle_inputOut = OpenRTM_aist.OutPort("angle_input", self._d_angle_input)





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

		# Set OutPort buffers
		self.addOutPort("angle_input",self._angle_inputOut)

		# Set service provider to Ports

		# Set service consumers to Ports

		# Set CORBA Service Ports

		return RTC.RTC_OK

	#	##
	#	#
	#	# The finalize action (on ALIVE->END transition)
	#	# formaer rtc_exiting_entry()
	#	#
	#	# @return RTC::ReturnCode_t
	#
	#	#
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK

	#	##
	#	#
	#	# The startup action when ExecutionContext startup
	#	# former rtc_starting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK

	#	##
	#	#
	#	# The shutdown action when ExecutionContext stop
	#	# former rtc_stopping_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
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
	
		return RTC.RTC_OK

	#	##
	#	#
	#	# The aborting action when main logic error occurred.
	#	# former rtc_aborting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK

	#	##
	#	#
	#	# The error action in ERROR state
	#	# former rtc_error_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK

	#	##
	#	#
	#	# The reset action that is invoked resetting
	#	# This is same but different the former rtc_init_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK

	#	##
	#	#
	#	# The state update action that is invoked after onExecute() action
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#

	#	#
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK

	#	##
	#	#
	#	# The action that is invoked when execution context's rate is changed
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK




def ControlDynamixelTestInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=controldynamixeltest_spec)
    manager.registerFactory(profile,
                            ControlDynamixelTest,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    ControlDynamixelTestInit(manager)

    # Create a component
    comp = manager.createComponent("ControlDynamixelTest")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

