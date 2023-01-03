while true; do
  if ! ps aux | grep -q gdbserver; then
    kill -9 $(pgrep "httpd")
    gdbserver :5000 --attach $(pgrep httpd)
  fi
  sleep 60
done