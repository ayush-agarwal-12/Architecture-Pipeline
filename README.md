# Requirements to Architecture Pipeline

## Project Overview
AI-powered automation tool that converts high-level business requirements into low-level technical specifications including modules, database schemas, pseudocode, and system architecture.

---

## Pipeline Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                     USER INPUT                                  │
│              (Business Requirement Text)                        │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                  ANALYSIS ENGINE                                │
│  ┌──────────────────────┐      ┌──────────────────────┐         │
│  │   Groq LLM (AI)      │      │  Rule-Based Parser   │         │
│  │  Llama 3.3 70B       │ OR   │  Pattern Matching    │         │
│  │  (Primary)           │      │  (Fallback)          │         │
│  └──────────────────────┘      └──────────────────────┘         │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│              MODULE & ENTITY DETECTION                          │
│  - Identifies system modules (auth, database, API, etc.)        │
│  - Extracts data entities (User, Product, Order, etc.)          │
│  - Detects relationships between entities                       │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│              DATABASE SCHEMA GENERATION                         │
│  - Creates table structures for each entity                     │
│  - Defines fields with appropriate data types                   │
│  - Adds constraints (PRIMARY KEY, FOREIGN KEY, NOT NULL)        │
│  - Establishes relationships between tables                     │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│              PSEUDOCODE GENERATION                              │
│  - Generates function-level logic for each module               │
│  - Includes error handling and validation                       │
│  - Provides API endpoint structures                             │
│  - Covers CRUD operations and business logic                    │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│              ARCHITECTURE DESIGN                                │
│  - Defines system layers (Frontend, Backend, Database)          │
│  - Recommends technology stack for each layer                   │
│  - Suggests architecture patterns                               │
│  - Provides security and scalability considerations             │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    OUTPUT DISPLAY                               │
│  - Modules & Entities (visual tags)                             │
│  - Database Schemas (tables with relationships)                 │
│  - Pseudocode (formatted code blocks)                           │
│  - Architecture Diagram (layers & technologies)                 │
│  - AI Insights (recommendations & considerations)               │
└─────────────────────────────────────────────────────────────────┘
```

---

## Tech Stack

### Backend
- **Framework**: Flask (Python)
- **AI Engine**: Groq API with Llama 3.3 70B Versatile model
- **Fallback**: Rule-based pattern matching system
- **API Protocol**: RESTful JSON API

### Frontend
- **Structure**: HTML5
- **Styling**: CSS3 (Custom, no frameworks)
- **Interactivity**: Vanilla JavaScript (ES6+)
- **Design Pattern**: Responsive, mobile-first

### AI & Processing
- **Primary**: Groq Cloud API (Lightning-fast LLM inference)
- **Model**: Llama 3.3 70B Versatile (70 billion parameters)
- **Speed**: 750+ tokens/second
- **Fallback**: Custom NLP with keyword extraction and pattern matching

### Development Tools
- **Language**: Python 3.7+
- **Package Manager**: pip
- **Environment**: Virtual environment (venv)
- **Dependencies**: 
  - `Flask==3.0.0` - Web framework
  - `groq==0.11.0` - Groq API client
  - `python-dotenv==1.0.0` - Environment variable management

### Architecture
- **Pattern**: Client-Server Architecture
- **Communication**: Asynchronous HTTP requests (Fetch API)
- **Data Format**: JSON
- **State Management**: Client-side (JavaScript variables)

---

## Pipeline Components Breakdown

### 1. Analysis Engine
- **Input**: Raw business requirement text
- **Processing**: Natural language understanding via LLM or rule-based parsing
- **Output**: Structured technical components

### 2. Module Detection
- **Input**: Analyzed requirement
- **Processing**: Identifies functional modules (authentication, storage, API, etc.)
- **Output**: List of system modules and entities

### 3. Schema Generation
- **Input**: Modules and entities
- **Processing**: Creates normalized database structure
- **Output**: SQL-like schemas with fields, types, and constraints

### 4. Pseudocode Generation
- **Input**: Modules and business logic requirements
- **Processing**: Generates algorithmic implementations
- **Output**: Function-level pseudocode with logic flow

### 5. Architecture Design
- **Input**: All detected components
- **Processing**: Maps to architectural patterns and tech stacks
- **Output**: Multi-layer architecture with technology recommendations

---

## Key Features

- **AI-Powered Analysis**: Uses state-of-the-art LLM for intelligent requirement parsing
- **Fallback System**: Works offline with rule-based analysis
- **Real-time Processing**: Results generated in 1-3 seconds
- **No Cost**: 100% free with Groq's generous API limits
- **Production-Ready**: Generates enterprise-grade technical specifications
