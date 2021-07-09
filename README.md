# ControlDynamixel-OpenRTM

Dynamixelを位置制御するOpenRTMコンポーネントです。

・ControlDynamixel
　pythonで作成したDynamixelを制御するコンポーネント
　入力：angle_input　位置制御の角度指令[deg]
　出力：なし
　パラメータ：
 　　DXL_ID　->　DynamixelのID
   　ADDR_MX_TORQUE_ENABLE　->　TORQUE_ENABLEのアドレス
   　ADDR_MX_GOAL_POSITION　->　GOAL_POSITIONのアドレス
     ADDR_MX_PRESENT_POSITION　->　PRESENT_POSITIONのアドレス
     BAUDRATE　->　ボーレート
     DEVICENAME　->　USB接続時の名前
     DXL_MOVING_STATUS_THRESHOLD　->　到達判定の閾値

・Test：
　ControlDynamixelコンポーネントをテストする用のコンポーネント
　入力：なし
　出力：angle_output　位置制御の角度指令[deg]
　パラメータ：なし

