##### Data Starts #####

gmail = 
password = 
Address = 
Phone Number = 
Credit Card Number = 
ID Number = 

##### Data Ends #####

;按下Alt+g去gmail信箱
!g::
run, https://reurl.cc/X6XLOa
sleep, 2000
send, %gmail% {enter}
sleep, 2000
send, %password% {enter}
return
