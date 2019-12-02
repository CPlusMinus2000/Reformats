#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

PATH = C:\Users\che\Documents\Authoring\Reformats
COUNT = C:\Users\che\Documents\Authoring\reformatCounter.txt

^Capslock::
Send, ^a
Send, ^c
RunWait, italicToNormal.py, %PATH%
Send, ^v
FileAppend, format %A_NOW%`n, %COUNT%, utf-8
return

^1::
Send, ^c
RunWait, italicToNormal.py, %PATH%
Send, ^v
FileAppend, format-highlight %A_NOW%`n, %COUNT%, utf-8
return

^2::
Send, ^c
RunWait, addToTags.py, %PATH%
Send, ^v
FileAppend, addToTags %A_NOW%`n, %COUNT%, utf-8
return

^+x::
Send, ^a
Send, ^c
RunWait, Enmathenate.py, %PATH%
Send, ^v
FileAppend, Enmathenate %A_NOW%`n, %COUNT%, utf-8
return

^+c::
Send, ^c
RunWait, Enmathenate.py, %PATH%
Send, ^v
FileAppend, Enmathenate %A_NOW%`n, %COUNT%, utf-8
return

^`::
Send, ^c
RunWait, addTags.py, %PATH%
Send, ^v
FileAppend, addTags %A_NOW%`n, %COUNT%, utf-8
return

^+Capslock::
FileAppend, replaceAnywhere %A_NOW%`n, %COUNT%, utf-8
Send, ^c
clip = %Clipboard%
RunWait, replaceAnywhere.py, %PATH%
If (clip != Clipboard) {
	Send, ^v
}
return

^+d::
Send, ^c
RunWait, operandSpace.py, %PATH%
Send, ^v
FileAppend, operandSpace %A_NOW%`n, %COUNT%, utf-8
return

^+s::
Send, ^c
RunWait, opSwitch.py, %PATH%
Send, ^v
FileAppend, opSwitch %A_NOW%`n, %COUNT%, utf-8
return
				
