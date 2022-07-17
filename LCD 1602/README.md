### 1602采用标准的16脚接口

VSS: GND为电源地

VDD: VCC接5V电源正极

V0: 为液晶显示器对比度调整端，接正电源时对比度最弱，接地电源时对比度最（对比度过高时会 产生“鬼影”，使用时可以通过一个10K的电位器调整对比度）

RS: 为寄存器选择，高电平1时选择数据寄存器、低电平0时选择指令寄存器

RW: 为读写信号线，高电平(1)时进行读操作，低电平(0)时进行写操作

E: E(或EN)端为使能(enable)端,高电平（1）时读取信息，负跳变时执行指令

第7～14引脚：D0～D7为8位双向数据端

A: 背光正极，可接一个10—47欧的限流电阻到VDD

K: 背光负极

### Raspberry - GPIO and the 40-pin Header
[offical link: ](https://www.raspberrypi.com/documentation/computers/os.html#gpio-and-the-40-pin-header)
![GPIO-Pinout-Diagram-2](https://user-images.githubusercontent.com/45325777/179383047-ac59e4c7-304e-40dd-86b1-4a7db9ef4d43.png)
