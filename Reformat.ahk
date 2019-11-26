#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

PATH = C:\Users\che\Documents\Authoring\Reformats

^Capslock::
Send, ^a
Send, ^c
RunWait, italicToNormal.py, %PATH%
Send, ^v
return

^1::
Send, ^c
RunWait, italicToNormal.py, %PATH%
Send, ^v
return

^2::
Send, ^c
RunWait, addToTags.py, %PATH%
Send, ^v
return

^`::
Send, ^c
RunWait, addTags.py, %PATH%
Send, ^v
return

^+Capslock::
Send, ^c
RunWait, replaceAnywhere.py, %PATH%
Send, ^v
return

^+x::
Send, ^c
RunWait, operandSpace.py, %PATH%
Send, ^v
return

^+s::
Send, ^c
RunWait, opSwitch.py, %PATH%
Send, ^v
return
				
