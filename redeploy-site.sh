#!/bin/bash

tmux kill-server
cd ./cyber-sapiens
git fetch && git reset origin/main --hard
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
tmux new-session -d -s "server"
tmux  send-keys -t "server" "flask run --host=0.0.0.0" Enter
echo "testing"
