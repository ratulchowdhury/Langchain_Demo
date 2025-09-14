# 🦜🔗 Langchain Demo

A comprehensive collection of LangChain examples demonstrating various AI model integrations and use cases.

## 📋 Overview

This repository contains practical examples of using LangChain with different AI providers:
- **OpenAI GPT Models** - Chat completions and embeddings
- **Google Gemini** - Google's latest AI model
- **Hugging Face Models** - Both API and local model usage
- **Embeddings** - Text embeddings and document processing

## 🚀 Features

### 1. Large Language Models (LLM)
- Basic LLM usage and prompt engineering
- Temperature and parameter tuning

### 2. Chat Models
- **OpenAI Integration** - GPT-3.5/4 chat completions
- **Google Gemini** - Advanced conversational AI
- **Hugging Face** - Both API and local model deployment
- Message types and conversation handling

### 3. Embeddings
- **OpenAI Embeddings** - Text-to-vector conversion
- **Hugging Face Embeddings** - Local embedding models
- **Document Processing** - Text chunking and similarity search

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- Git

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Langchain_Demo.git
   cd Langchain_Demo
   ```

2. **Create virtual environment**
   ```bash
   python -m venv langchain_env
   
   # Windows
   langchain_env\Scripts\activate
   
   # macOS/Linux
   source langchain_env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   ```bash
   cp .env.template .env
   ```
   
   Edit `.env` file with your API keys:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   GOOGLE_API_KEY=your_google_api_key_here
   HUGGINGFACE_API_TOKEN=your_huggingface_token_here
   ```

## 🎯 Usage Examples

### OpenAI Chat Model
```bash
cd 2.ChatModel
python chat_model_openai_demo.py
```

### Google Gemini
```bash
cd 2.ChatModel
python chat_model_gemini_demo.py
```

### Local Hugging Face Model
```bash
cd 2.ChatModel
python chat_model_hf_local_demo.py
```

### Text Embeddings
```bash
cd 3.Embeddings
python embedding_openai_demo.py
```

### Document Processing
```bash
cd 3.Embeddings
python document_embeddings_demo.py
```

## 📁 Project Structure

```
Langchain_Demo/
├── 1.LLM/
│   └── llm_demo.py                    # Basic LLM usage
├── 2.ChatModel/
│   ├── chat_model_openai_demo.py      # OpenAI GPT integration
│   ├── chat_model_gemini_demo.py      # Google Gemini integration
│   ├── chat_model_hf_api_demo.py      # Hugging Face API
│   └── chat_model_hf_local_demo.py    # Local HF models
├── 3.Embeddings/
│   ├── embedding_openai_demo.py       # OpenAI embeddings
│   ├── embedding_hf_demo.py           # Hugging Face embeddings
│   └── document_embeddings_demo.py    # Document processing
├── requirements.txt                    # Dependencies
├── .env.template                      # Environment template
├── .gitignore                         # Git ignore rules
└── README.md                          # This file
```

## 🔑 API Keys Setup

### OpenAI
1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. Create an account and generate an API key
3. Add to `.env`: `OPENAI_API_KEY=sk-...`

### Google Gemini
1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Generate an API key
3. Add to `.env`: `GOOGLE_API_KEY=AIza...`

### Hugging Face
1. Visit [Hugging Face Tokens](https://huggingface.co/settings/tokens)
2. Create a new token
3. Add to `.env`: `HUGGINGFACE_API_TOKEN=hf_...`

## 🐛 Troubleshooting

### Common Issues

**1. Module Not Found Error**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**2. API Key Errors**
- Verify your API keys in `.env` file
- Check API key permissions and quotas

**3. Local Model Download Issues**
- Ensure sufficient disk space (models can be 1GB+)
- Check internet connection for first-time downloads

**4. Memory Issues with Local Models**
- Try smaller models like `distilgpt2`
- Close other applications to free up RAM

## 🎨 Customization

### Adding New Models
1. Create new demo file in appropriate directory
2. Follow existing patterns for error handling
3. Update requirements.txt if new dependencies needed

### Extending Functionality
- Add new embedding models
- Implement RAG (Retrieval Augmented Generation)
- Create custom prompt templates

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain) - The framework that makes this possible
- [OpenAI](https://openai.com/) - GPT models and embeddings
- [Google](https://ai.google.dev/) - Gemini AI models
- [Hugging Face](https://huggingface.co/) - Open-source model hub

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section
2. Review existing GitHub issues
3. Create a new issue with detailed description

---

**Happy coding with LangChain! 🦜🔗**
