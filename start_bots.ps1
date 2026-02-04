# Running all bots in parallel
Start-Process powershell -ArgumentList "-NoExit -Command `"cd '.\bots\weather-bot'; .venv\Scripts\activate; python main.py`""
Start-Process powershell -ArgumentList "-NoExit -Command `"cd '.\bots\news-bot'; .venv\Scripts\activate; python main.py`""

# Or via PM2 for Node.js (also works with Python)
npm install -g pm2
pm2 start ecosystem.config.js