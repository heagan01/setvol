@echo off
setlocal enabledelayedexpansion
SoundVolumeView.exe /GetPercent Speakers
set /a _volume=%errorlevel% / 10
echo %_volume%
endlocal 