import serial  # 引用pySerial模組

COM_PORT = 'COM6'    # 指定通訊埠名稱
BAUD_RATES = 9600    # 設定傳輸速率

try:
    with serial.Serial(COM_PORT, BAUD_RATES, timeout=1) as ser: # 初始化序列通訊埠
        print(f"Connected to {ser.name}")
        
        while True:
            while ser.in_waiting:          # 若收到序列資料…
                data_raw = ser.readline()  # 讀取一行
                data = data_raw.decode('utf-8').strip()   # 用預設的UTF-8解碼
                print('接收到的原始資料：', data_raw)
                print('接收到的資料：', data)

except KeyboardInterrupt:
    print('再見！')
except serial.SerialException as e:
    print(f"Error opening or communicating with the serial port: {e}")
finally:
    ser.close()    # 清除序列通訊物件
