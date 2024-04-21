@echo off
echo Installing app...
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
(
  echo @echo off
  echo echo Starting app
  echo .venv\Scripts\waitress-serve --host 127.0.0.1 app:app
) > start.bat