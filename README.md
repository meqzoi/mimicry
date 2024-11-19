# Mimicry

Mimicry is a Python-based CLI tool and server for creating and managing REST API mocks. 
It allows users to quickly mock HTTP endpoints and responses for testing purposes. 
The tool supports both CLI and HTTP API for managing mock responses.

## Features

- **Start/Stop Mock Server**: Run the server in the background or stop it gracefully.
- **Schedule Mock Endpoints**: Create custom HTTP endpoints with:
  - Status codes
  - Response headers
  - Response body
  - Response delays
- **View Server Status**: Check if the server is running.
- **Flexible CLI Interface**: Manage mocks easily from the command line.
- **HTTP API for Mock Scheduling**: Create mocks programmatically via the `/mocks/create` endpoint.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/meqzoi/mimicry.git
   cd mimicry
2. Install the application in editable mode:
   ```bash
    pip install -e .