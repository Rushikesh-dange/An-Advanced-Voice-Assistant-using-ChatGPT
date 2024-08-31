# VoiceGPT: A Voice-Enabled Chatbot Using ChatGPT

VoiceGPT is a project that transforms OpenAI's ChatGPT into a voice assistant, allowing you to have a conversation with it just like you would with Siri, Google Assistant, or Alexa. By leveraging Natural Language Processing (NLP) and speech recognition, VoiceGPT can understand your voice queries and respond to you with synthesized speech.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Introduction

VoiceGPT combines the power of ChatGPT with voice recognition and speech synthesis to create an interactive voice assistant. This project is ideal for anyone looking to experiment with voice-enabled AI and explore how to integrate ChatGPT with NLP technologies.

## Features

- **Voice Recognition**: Captures user voice input using Google NLP or OpenAI's Whisper.
- **ChatGPT Integration**: Sends the recognized voice query to ChatGPT and processes the response.
- **Speech Synthesis**: Converts ChatGPT's text response into human-like speech.
- **Customizable**: Choose from different GPT models like Ada, Davinci, or Babbage.

## Requirements

- Python 3.x
- Raspberry Pi (optional, but recommended)
- USB Microphone (if not using a laptop's inbuilt microphone)
- [OpenAI API Key](https://platform.openai.com/signup)
- Internet connection for API access

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/VoiceGPT.git
cd VoiceGPT
