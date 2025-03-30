#!/bin/sh

run() {
  if ! pgrep -f "$1"; then
    "$@" &
  fi
}

run numlockx
run nitrogen --restore
xset s off -dpms
