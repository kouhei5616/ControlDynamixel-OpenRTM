# ControlDynamixel-OpenRTM

Dynamixelを位置制御するOpenRTMコンポーネントです。

・ControlDynamixel<br>
　pythonで作成したDynamixelを制御するコンポーネント<br>
　入力：angle_input　位置制御の角度指令[deg]<br>
　出力：なし<br>
　パラメータ：<br>
　　DXL_ID　->　DynamixelのID<br>
　　ADDR_MX_TORQUE_ENABLE　->　TORQUE_ENABLEのアドレス<br>
　　ADDR_MX_GOAL_POSITION　->　GOAL_POSITIONのアドレス<br>
　　ADDR_MX_PRESENT_POSITION　->　PRESENT_POSITIONのアドレス<br>
　　BAUDRATE　->　ボーレート<br>
　　DEVICENAME　->　USB接続時の名前<br>
　　DXL_MOVING_STATUS_THRESHOLD　->　到達判定の閾値<br>

・Test<br>
　ControlDynamixelコンポーネントをテストする用のコンポーネント<br>
　入力：なし<br>
　出力：angle_output　位置制御の角度指令[deg]<br>
　パラメータ：なし<br>

