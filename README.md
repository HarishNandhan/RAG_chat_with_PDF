# 📄 PDF Knowledge Extraction RAG Bot

A powerful Retrieval-Augmented Generation (RAG) chatbot that allows you to upload PDF documents and ask questions about their content. Built with Streamlit, FAISS for vector search, and EURI API for embeddings and chat completions.

## 🚀 Features

- **PDF Document Processing**: Upload and extract text from PDF files
- **Intelligent Text Chunking**: Smart text splitting with overlap for better context
- **Vector Search**: FAISS-based similarity search for relevant document sections
- **Conversation Memory**: Maintains context across multiple questions
- **Modern UI**: Clean Streamlit interface for easy interaction
- **Secure API Key Management**: Environment variables for API key security

## 🏗️ Architecture

### Core Components

1. **PDF Text Extraction**: Uses `pdfplumber` to extract text from uploaded PDFs
2. **Text Chunking**: Splits large documents into manageable chunks (5000 chars with 1000 char overlap)
3. **Vector Embeddings**: Converts text chunks into embeddings using EURI API
4. **Vector Database**: FAISS index for fast similarity search
5. **RAG Pipeline**: Retrieves relevant context and generates answers using EURI GPT-4.1-nano
6. **Conversation Memory**: Maintains chat history for contextual responses

### Data Flow

```
PDF Upload → Text Extraction → Chunking → Embeddings → FAISS Index
                                                           ↓
User Question → Embedding → Similarity Search → Context Retrieval → RAG Response
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8+
- EURI API key (get it from [Euroni](https://euron.one))

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
cd RAG_chat_with_PDF
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Environment Setup

1. Create a `.env` file in the project root:
```bash
touch .env
```

2. Add your EURI API key to the `.env` file:
```
EURI_API_KEY=your_euri_api_key_here
```

**⚠️ Important**: Never commit your `.env` file to version control. It's already included in `.gitignore`.

### Step 4: Run the Application

```bash
streamlit run pdf_rag_bot.py
```

The application will open in your default browser at `http://localhost:8501`.

## 📱 User Interface

![PDF RAG Bot Interface](https://github.com/HarishNandhan/RAG_chat_with_PDF/blob/main/screenshots/pdf_rag_bot.png)

### UI Components

1. **Title**: Clear identification of the application
2. **File Uploader**: Drag and drop or browse for PDF files
3. **Question Input**: Text field for asking questions about the document
4. **Status Messages**: Success notifications when PDF is processed
5. **Answer Display**: Formatted response area with the bot's answers

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `EURI_API_KEY` | Your EURI API key for embeddings and chat | Yes |

### API Endpoints

- **Embeddings**: `https://api.euron.one/api/v1/euri/alpha/embeddings`
- **Chat Completions**: `https://api.euron.one/api/v1/euri/alpha/chat/completions`

### Model Configuration

- **Embedding Model**: `text-embedding-3-small`
- **Chat Model**: `gpt-4.1-nano`
- **Temperature**: 0.3 (for consistent responses)

## 📚 Usage Guide

### 1. Upload a PDF

- Click "Browse files" or drag and drop a PDF into the upload area
- Supported format: PDF only
- The system will automatically process and index the document

### 2. Ask Questions

- Type your question in the text input field
- Questions can be about any content in the uploaded PDF
- Examples:
  - "What are the main topics discussed in this document?"
  - "Summarize the key findings"
  - "What does the document say about [specific topic]?"

### 3. Get Answers

- The system will:
  1. Convert your question to embeddings
  2. Find the most relevant text chunks from the PDF
  3. Generate a contextual answer using RAG
  4. Display the response with conversation memory

### 4. Continue Conversation

- Ask follow-up questions
- The system maintains conversation context
- Previous questions and answers are remembered

## 🧠 How RAG Works

### 1. Document Processing
```python
def extract_text_from_pdf(pdf_path):
    # Extracts all text from PDF pages
    # Returns concatenated text string
```

### 2. Text Chunking
```python
def split_text(text, chunk_size=5000, overlap=1000):
    # Splits text into overlapping chunks
    # Ensures context continuity between chunks
```

### 3. Vector Embeddings
```python
def get_euri_embeddings(texts):
    # Converts text chunks to numerical vectors
    # Uses EURI's text-embedding-3-small model
```

### 4. Similarity Search
```python
def retrieve_context(question, chunks, index, embeddings, top_k=3):
    # Finds most similar chunks to the question
    # Returns top-k relevant text sections
```

### 5. RAG Response Generation
```python
def ask_euri_with_context(question, context, memory=None):
    # Combines retrieved context with question
    # Generates answer using GPT-4.1-nano
    # Maintains conversation memory
```

## 🔒 Security Features

- **API Key Protection**: Stored in `.env` file (not in code)
- **Git Ignore**: `.env` file is excluded from version control
- **No Data Persistence**: Uploaded files are temporary
- **Secure API Calls**: HTTPS endpoints with proper authentication

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `streamlit` | Latest | Web interface framework |
| `pdfplumber` | Latest | PDF text extraction |
| `faiss-cpu` | Latest | Vector similarity search |
| `requests` | Latest | HTTP API calls |
| `numpy` | Latest | Numerical operations |
| `python-dotenv` | Latest | Environment variable management |

## 🚀 Performance Optimization

### Current Optimizations

- **Chunk Size**: 5000 characters with 1000 character overlap
- **Top-K Retrieval**: Retrieves top 3 most relevant chunks
- **FAISS Index**: Fast similarity search with L2 distance
- **Memory Management**: Temporary file handling

### Potential Improvements

- **Caching**: Cache embeddings for repeated documents
- **Batch Processing**: Process multiple documents
- **Advanced Chunking**: Semantic chunking based on content
- **Hybrid Search**: Combine keyword and semantic search

## 🐛 Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure `.env` file exists and contains `EURI_API_KEY`
   - Verify API key is valid and has sufficient credits

2. **PDF Processing Error**
   - Check if PDF is password-protected
   - Ensure PDF contains extractable text (not scanned images)

3. **Memory Issues**
   - Large PDFs may cause memory problems
   - Consider reducing chunk size for very large documents

4. **Streamlit Issues**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Check if port 8501 is available

### Error Messages

- `"API key not found"`: Check `.env` file configuration
- `"PDF extraction failed"`: Verify PDF format and content
- `"No relevant context found"`: Try rephrasing your question

## 🙏 Acknowledgments

- **EURI API**: For providing embeddings and chat completions
- **FAISS**: For efficient vector similarity search
- **Streamlit**: For the beautiful web interface
- **PDFPlumber**: For reliable PDF text extraction


**Happy Document Chatting! 📚✨** 