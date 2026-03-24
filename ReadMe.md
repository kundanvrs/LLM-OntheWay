
# 🤖 KBA Automation with Local GenAI

This project provides two intelligent tools powered by local GenAI models to improve knowledge management and troubleshooting workflows using Jira tickets.

---

## 📌 Features

### 1️⃣ KBA_Generator

**Jira Ticket → Troubleshooting Article Generator**

* Converts Jira tickets into structured Knowledge Base Articles (KBAs)
* Helps teams document solutions automatically
* Reduces manual effort in writing troubleshooting guides

---

### 2️⃣ KBA_Search

**Jira Ticket → Retrieve Most Relevant Article**

* Finds the most probable existing KBA based on a Jira ticket
* Speeds up issue resolution
* Avoids duplication of knowledge

---

## ⚙️ Tech Stack

* Local GenAI (via Ollama)
* Open WebUI
* Python

---

## 🚀 Installation

### 🔹 Install Ollama

```bash
pip install ollama
```

---

## 🌐 Open WebUI Setup

### Option 1: Using Python (pip)

#### Install Open WebUI

```bash
pip install open-webui
```

#### Run Server

```bash
open-webui serve
```

#### Access UI

```
http://localhost:8080/
```

---

### Option 2: Using Docker

```bash
docker run -d -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
  --name open-webui \
  --restart always \
  ghcr.io/open-webui/open-webui:main
```

---

## 🧠 How It Works

1. Input a Jira ticket
2. Use:

   * **KBA_Generator** → Generates a troubleshooting article
   * **KBA_Search** → Finds similar existing KBAs
3. Review and refine output in Open WebUI


## 💡 Use Cases

* IT Support Automation
* DevOps Knowledge Management
* Incident Resolution Acceleration
* Internal Documentation Systems

---

## 📸 UI Access

Once running:

* Local UI → [http://localhost:8080/](http://localhost:8080/) (pip)
* Docker UI → [http://localhost:3000/](http://localhost:3000/)
* API usage examples
* sample prompts & outputs
* resume/portfolio version 🚀
