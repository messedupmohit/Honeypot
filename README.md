# Honeypot

## Overview

Honeypot is a simple multi-service server implemented in Python using the `socket` and `threading` libraries. The server simulates multiple services such as HTTP, FTP, and TELNET, each running on different ports. It listens for incoming connections and responds with a basic message depending on the service type. This setup can be used to attract potential attackers and monitor their activities, acting as a honeypot.

## Features

- **Multi-Service Handling**: The server can simultaneously handle multiple services like HTTP, FTP, and TELNET.
- **Concurrent Client Handling**: Each incoming client connection is handled in a separate thread, allowing multiple clients to be served concurrently.
- **Basic HTTP Response**: For HTTP requests, the server responds with a simple HTML page.
- **Honeypot Simulation**: Acts as a decoy to detect unauthorized access or attacks on the server.

## Requirements

- Python 3.x

## Installation

1. **Clone the repository** or download the project files:
   ```bash
   git clone https://github.com/messedupmohit/Honeypot.git
   cd honeypot
