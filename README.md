# Financial Statement Analysis Chatbot with RAG

A prototype chatbot for analyzing corporate financial statements using Retrieval-Augmented Generation (RAG).

## Project Overview

This project is a prototype of an AI chatbot that analyzes corporate financial information using RAG.

The current prototype provides a basic workflow for uploading financial documents, creating a FAISS vector database, retrieving relevant information, generating answers with Gemini, and saving chat logs as JSON.

## Current Status

The current version is a RAG-based chatbot prototype implemented with FastAPI.

The prototype consists of:

```
prototype/
├── api_router.py  
├── chatbot.py  
├── json_save.py  
├── logging_config.py  
├── main.py  
├── pdf_save.py  
└── rag.py
```

Generated files and directories such as the FAISS index, uploaded PDFs, logs, and JSON output are excluded from Git tracking.

## Main Components
* main.py  
  Entry point of the FastAPI application.
* api_router.py  
  Defines the API endpoints for PDF upload and chatbot queries.
* pdf_save.py  
  Handles PDF file validation and local storage.
* rag.py  
  Loads PDF documents, splits them into chunks, generates embeddings, and creates a FAISS vector database.
* chatbot.py  
  Retrieves relevant document chunks and generates responses using Gemini.
* json_save.py  
  Saves questions and generated answers as JSON chat logs.
* logging_config.py  
  Configures application logging to both a log file and the console.

## Technologies
* Python
* FastAPI
* LangChain
* FAISS
* Hugging Face Embeddings
* Google Gemini
* Pydantic

## Development Roadmap

The prototype will be expanded step by step.

## Phase 1: RAG Prototype — Completed
* Implement a basic RAG pipeline
* Retrieve relevant information from financial documents
* Generate analysis based on retrieved context
* Create a FAISS vector database

## Phase 2: FastAPI — Completed
* Develop an API using FastAPI
* Provide an interface for submitting analysis requests
* Structure the application for practical use

## Phase 3: Logging — Completed
* Add application logging
* Record analysis processes and errors
* Improve monitoring and debugging

## Phase 4: Multi-Agent Analysis — Planned
* Divide financial analysis into multiple specialized agents
* Analyze different aspects of financial statements
* Combine the results into a comprehensive analysis

## Future Goal

The goal is to develop the prototype into a practical AI system for financial statement analysis.

The system will eventually combine:

```
Financial Documents
        ↓
       RAG
        ↓
Multi-Agent Analysis
        ↓
Financial Analysis
        ↓
       API
```

This project is currently under development.
