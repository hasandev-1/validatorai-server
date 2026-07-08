#!/bin/bash


# tts testing

curl -X 'POST' \
  'http://localhost:8000/tts/generate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Hello, this is a test.",
  "voice": "Kore"
}' --output audio.wav
