$server = "server.py"
$client = "client.py"

Start-Process powershell -ArgumentList "-NoExit", "-Command python `"$server`""

Start-Sleep -Seconds 1

for ($i=1; $i -le 3; $i++) {
    Start-Process powershell -ArgumentList "-NoExit", "-Command python `"$client`" node$i 127.0.0.1"
}