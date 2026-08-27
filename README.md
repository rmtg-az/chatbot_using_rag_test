# Financial Statement Analysis Chatbot with RAG

A RAG-based chatbot for analyzing corporate financial statements using Retrieval-Augmented Generation (RAG).

## Project Overview

This project demonstrates a basic AI chatbot for analyzing corporate financial information using RAG.

The system provides a workflow for uploading financial documents, creating a FAISS vector database, retrieving relevant information, generating responses with Google Gemini, and saving chat logs as JSON.

The project was developed as a learning and prototyping project to explore the practical implementation of RAG for financial document analysis.

## Current Status

This project is a completed RAG-based chatbot prototype implemented with FastAPI.

The application demonstrates the following workflow:

```
Financial Documents
        ↓
PDF Processing
        ↓
Text Chunking
        ↓
Embedding Generation
        ↓
FAISS Vector Database
        ↓
Relevant Information Retrieval
        ↓
Google Gemini
        ↓
Generated Response
        ↓
JSON Chat Log
```

Generated files and directories such as the FAISS index, uploaded PDFs, logs, and JSON output are excluded from Git tracking.

## Project Structure

```
app/
├── api_router.py  
├── chatbot.py  
├── json_save.py  
├── logging_config.py  
├── main.py  
├── pdf_save.py  
└── rag.py
```

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
  Retrieves relevant document chunks and generates responses using Google Gemini.
* json_save.py  
  Saves questions and generated answers as JSON chat logs.
* logging_config.py  
  Configures application logging to both a log file and the console.

## Implementation Highlights
* PDF document upload and validation
* Text extraction and document chunking
* Multilingual text embeddings using Hugging Face
* FAISS-based vector similarity search
* Retrieval-Augmented Generation (RAG)
* LLM-based financial document analysis
* REST API implementation with FastAPI
* Structured JSON chat log storage
* Application logging for monitoring and debugging

## Project Status

The RAG chatbot implementation is complete as a prototype.

This project is intended to demonstrate the implementation of a RAG pipeline for financial document analysis rather than serve as a production-ready financial analysis system.

Further development of this project is not currently planned. Future experiments with more advanced architectures, including multi-agent approaches for financial document analysis, will be developed as separate projects.

## Related Project

A separate project is planned to explore a multi-agent architecture for analyzing annual securities reports.

The new project will focus on dividing financial analysis into specialized agents and combining their results into a comprehensive analysis.

This project and the future multi-agent project are intentionally separated to demonstrate different approaches to applying LLMs to financial document analysis.
