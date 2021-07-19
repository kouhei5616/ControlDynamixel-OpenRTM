# ControlDynamixel-OpenRTM<br>

## 概要<br>
PCからDynamixelを拡張位置制御するOpenRTMコンポーネントです。<br>
pythonのserialモジュールと[dynamixel_sdk](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/overview/)モジュールを使用しています。（既にファイルの中に組み込まれています）<br>

## 必要なもの<br>
・Linux/Windows/MacOS搭載のPC<br>
・protocol 1.0に対応したDynamixel<br>
・バッテリ（使用するDynamixelの仕様に合わせる）<br>
・PCーDynamixel間のインタフェース（例：U2D2）<br>
・Dynamixel設定ソフト（例：[Dynamixel Wizard](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_wizard2/)）

## 使い方<br>
１．[ROBOTIS e-manual U2D2](https://emanual.robotis.com/docs/en/parts/interface/u2d2/)を参考にしてDynamixel、バッテリ、PCを接続する。<br>

２．Dynamixel Wizardを使用してDynamixelの設定を確認する。<br>
　　・IDを確認<br>
　　・Baud Rate (Bus)を確認<br>
　　・Operating ModeをExtended Position controlに設定<br>
　　・Protocol Typeを1.0に設定<br>
　　・Torque Enable Addressを確認<br>
　　・Goal Position Addressを確認<br>
　　・Present Position Addressを確認<br>

３．シリアルポートの名前を確認する。<br>
　　Windows：'COM1'など<br>
　　MacOS：'usbserial-123456'など<br>
　　Linux：'/dev/ttyUSB0'など<br>
  
４．Name Serverを起動する。<br>

５．ControlDynamixel.pyを起動する。<br>

６．OpenRTMでパラメータの設定・接続・アクティブ化する。<br>


## コンポーネントの説明<br>
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
　　DEVICENAME　->　シリアルポートの名前<br>
　　DXL_MOVING_STATUS_THRESHOLD　->　位置到達判定の閾値<br>

・Test<br>
　ControlDynamixelコンポーネントをテストする用のコンポーネント<br>
　入力：なし<br>
　出力：angle_output　位置制御の角度指令[deg]<br>
　パラメータ：なし<br>

