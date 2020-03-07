
InputBox, OutputVar, 請輸入您的Gmail帳戶。

InputBox, OutputVarP, 請輸入您的Gmail密碼。

;按下Alt+g去gmail信箱
!g::
run, https://reurl.cc/X6XLOa
sleep, 2000
send, %OutputVar% {enter}
sleep, 2000
send, %OutputVarP% {enter}
return
