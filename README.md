# Financial Statement Analysis Chatbot with RAG

A prototype chatbot for analyzing corporate financial statements using Retrieval-Augmented Generation (RAG).

## Project Overview

This project is a prototype of an AI chatbot that analyzes corporate financial information using RAG.

The current prototype focuses on retrieving relevant information from financial documents and generating analysis based on the retrieved context.

## Current Status

The current version is a RAG-based prototype.

The prototype consists of:

```prototype/
├── chatbot.py
├── main.py
└── rag.py

## Main Components
* main.py
  Entry point of the prototype.
* rag.py
  Handles document retrieval and RAG-related processing.
* chatbot.py
  Handles chatbot logic and generates responses based on retrieved information.

## Development Roadmap

The current prototype will be expanded step by step.

## Phase 1: RAG Prototype
* Implement a basic RAG pipeline
* Retrieve relevant information from financial documents
* Generate analysis based on retrieved context

## Phase 2: FastAPI
* Develop an API using FastAPI
* Provide an interface for submitting analysis requests
* Structure the application for practical use

## Phase 3: Logging
* Add application logging
* Record analysis processes and errors
* Improve monitoring and debugging

## Phase 4: Multi-Agent Analysis
* Divide financial analysis into multiple specialized agents
* Analyze different aspects of financial statements
* Combine the results into a comprehensive analysis

## Future Goal

The goal is to develop the prototype into a practical AI system for financial statement analysis.

The system will eventually combine:

```Financial Documents
        ↓
       RAG
        ↓
  Multi-Agent Analysis
        ↓
 Financial Analysis
        ↓
      API

This project is currently under development.