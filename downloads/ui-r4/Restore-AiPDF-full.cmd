@echo off
cd /d "%~dp0"
copy /b "AiPDF-v0.0008-ui-r4-full.zip.001"+"AiPDF-v0.0008-ui-r4-full.zip.002"+"AiPDF-v0.0008-ui-r4-full.zip.003" "AiPDF-v0.0008-ui-r4-full.zip"
if errorlevel 1 exit /b 1
echo Reassembled AiPDF-v0.0008-ui-r4-full.zip
