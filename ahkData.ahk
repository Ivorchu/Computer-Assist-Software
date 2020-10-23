FileRead, google, C:\Users\User\Desktop\Ethan\Programming\資通訊\Computer-Assist-Software\data.txt[1]
FileRead, googlePassword, C:\Users\User\Desktop\Ethan\Programming\資通訊\Computer-Assist-Software\data.txt[2]
FileRead, fb, C:\Users\User\Desktop\Ethan\Programming\資通訊\Computer-Assist-Software\data.txt[3]
FileRead, fbPassword, C:\Users\User\Desktop\Ethan\Programming\資通訊\Computer-Assist-Software\data.txt[4]

;按下Alt+g去gmail信箱
!g::
run, https//:www.gmail.com
sleep, 2000
send, %google% {enter}
sleep, 2000
send, %googlePassword% {enter}
return

;按下Alt+f去gmail信箱
!f::
run, https//:www.facebook.com
sleep, 2000
send, %fb% {enter}
sleep, 2000
send, %fbPassword% {enter}
return