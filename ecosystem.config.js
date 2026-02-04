module.exports = {
  apps: [
    {
      name: "weather-bot",
      script: "main.py",
      cwd: "./weather-bot",
      interpreter: "python",
      interpreter_args: "-u"
    },
    {
      name: "news-bot",
      script: "main.py", 
      cwd: "./news-bot",
      interpreter: "python",
      interpreter_args: "-u"
    }
  ]
}