# ChatGPT Conversational Retrieval System

## Overview

This repository contains a Conversational Retrieval System powered by ChatGPT, a language model developed by OpenAI. The system allows users to interact with the model through a command-line interface, asking questions and receiving responses based on a pre-indexed dataset.

## Features

- Conversational interaction with ChatGPT.
- Dynamic loading of data from text files or directories.
- Support for persisting the index for repeated queries.
- Error handling for a seamless user experience.

## Prerequisites

pip install -r requirements.txt


Before running the code, make sure you have the following installed:

- Python 3.x
- Pip (Python package installer)

## Setup

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/sik247/peronsalGPT.git
   cd ChatGPT-Conversational-Retrieval


## Installation

Install [Langchain](https://github.com/hwchase17/langchain) and other required packages.
```
pip install langchain openai chromadb tiktoken unstructured
```
Modify `constants.py.default` to use your own [OpenAI API key](https://platform.openai.com/account/api-keys), and rename it to `constants.py`.

Place your own data into `data/data.txt`.

## Example usage
Test reading `data/data.txt` file.
```
python3 chatgpt.py "What is my name"
> Harry
Python3 chatgpt3.py "How old is Harry?"
> 2


```
python3 chatgpt.py
