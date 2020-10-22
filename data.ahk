##### Data Starts #####

Gmail = 
Password = 
Address = 
Phone Number = 
Credit Card Number = 
ID Number = 

##### Data Ends #####

autohotkey(){
	;按下Alt+g去gmail信箱
	!g::
	run, https://reurl.cc/X6XLOa
	sleep, 2000
	send, %Gmail% {enter}
	sleep, 2000
	send, %Password% {enter}
	return
}

