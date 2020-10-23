FileReadLine, account, 			C:\Users\User\Desktop\Ethan\Programming\資通訊\Computer-Assist-Software\data.txt, 1
FileReadLine, password, 		C:\Users\User\Desktop\Ethan\Programming\資通訊\Computer-Assist-Software\data.txt, 2

;FileReadLine, fb, 				C:\Users\User\Desktop\Ethan\Programming\資通訊\Computer-Assist-Software\data.txt, 4
;FileReadLine, fbPassword, 		C:\Users\User\Desktop\Ethan\Programming\資通訊\Computer-Assist-Software\data.txt, 5

;按下Alt+g去gmail信箱
!g::
run, "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" -incognito "https://gmail.com"
sleep, 2000
send, account {enter}
sleep, 2000
send, password {enter}
return

;按下Alt+f去fb
!f::
run, "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" -incognito "https://www.facebook.com" 
sleep, 2000
send, %account% {enter}
sleep, 2000
send, %password% {enter}
return