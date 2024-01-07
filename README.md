# ChatGPT Conversational Retrieval System

## Overview

Welcome to the ChatGPT Conversational Retrieval System repository! This project utilizes ChatGPT, an advanced language model developed by OpenAI, to provide a seamless command-line interface for interactive conversations. Users can ask questions and receive responses based on a pre-indexed dataset.

## Features

- Conversational interaction with ChatGPT.
- Dynamic loading of data from text files or directories.
- Support for persisting the index for repeated queries.
- Error handling for a seamless user experience.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- Pip (Python package installer)

Install the required packages by running:

```bash

pip install -r requirements.txt
```


## Set UP
git clone https://github.com/sik247/peronsalGPT.git
cd ChatGPT-Conversational-Retrieval

```bash
pip install langchain openai chromadb tiktoken unstructured
```

Modify constants.py.default to use your own OpenAI API key and rename it to constants.py.

Place your own data into data/data.txt.

Example Usage
Test Reading data/data.txt File
Run the following commands to test reading the data file:


```bash
python3 chatgpt.py "What is my name"
```
Expected Output: Harry

```bash
python3 chatgpt.py "How old is Harry?"
```
Expected Output: 28


Interactive Mode
Run the following command for interactive mode:
```bash
python3 chatgpt.py
'''

Notes
To exit the program at any time, type quit, q, or exit.
