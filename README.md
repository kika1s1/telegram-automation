# Telegram Automation Bot

This project automates the daily check-in and check-out process with a Telegram bot (e.g., [@A2SVBouncerBot](https://t.me/A2SVBouncerBot)) using Telegram's MTProto API via Telethon. The codebase follows Clean Architecture principles for improved maintainability and testability, and it is containerized using Docker for easy deployment.

## Table of Contents

- [Telegram Automation Bot](#telegram-automation-bot)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Folder Structure](#folder-structure)

## Overview

This repository implements an automation script for a Telegram bot that performs:
- **Check-In** at 1:00 PM (by sending `/checkin` and selecting an inline button, e.g., "ASTU In-person")
- **Check-Out** at 8:00 PM (by sending `/checkout`)

The project is built with a Clean Architecture approach to separate concerns and ease future enhancements.

## Features

- **Automated Scheduling:** Runs daily tasks at specified times.
- **Clean Architecture:** Organized into domains, use cases, gateways, and services.
- **Dockerized Deployment:** Easily build and run the application in a container.
- **Session Persistence:** Supports persistent sessions using volume mounts.
- **Secure Configuration:** Uses environment variables for API credentials and configuration.

## Prerequisites

- **Python 3.9+**
- **Docker** (for containerized deployment)
- Telegram API credentials:
  - `TELEGRAM_API_ID`
  - `TELEGRAM_API_HASH`
  - `BOT_USERNAME` (e.g., `A2SVBouncerBot`)

## Folder Structure

telegram-automation/
├── app/
│   ├── __init__.py
│   ├── main.py             # Entry point; bootstraps the app and scheduler
│   ├── config.py           # Configuration (loads environment variables)
│   │
│   ├── domain/             # Business models & entities (core rules)
│   │   ├── __init__.py
│   │   └── attendance.py   # e.g., domain models, status, or business rules
│   │
│   ├── usecases/           # Application logic (check-in and check-out workflows)
│   │   ├── __init__.py
│   │   └── telegram_tasks.py  # Implements actions like check-in and check-out
│   │
│   ├── gateways/           # External integrations (e.g., Telegram client)
│   │   ├── __init__.py
│   │   └── telegram_client.py  # Wraps Telethon functionality and API calls
│   │
│   └── services/           # Additional services (e.g., scheduler)
│       ├── __init__.py
│       └── scheduler.py  # Orchestrates timing for check-in/check-out
│
├── tests/                  # Unit and integration tests
│   └── test_telegram_tasks.py
│
├── requirements.txt        # Python dependencies (e.g., telethon)
├── Dockerfile              # Docker build instructions
└── README.md               # Project documentation and setup instructions
