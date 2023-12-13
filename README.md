# Chat with your database using LangChain and GPT-4

## Project Overview
This repository is a step-by-step guide, corresponding to the ["Chat with Your Database using LangChain and GPT-4"](https://bit.ly/chat-database-langchain-gpt4) blog.
 Each branch represents a different stage in the tutorial, allowing users to progress through the content interactively.

## How to Use This Repository
Navigate through the branches to follow along with the blog. Each branch is a checkpoint in the tutorial, containing code relevant to that stage.

## Repository Branches

| Step | Branch | Description |
|------|--------|-------------|
| 1    | [Base Implementation - base-no-prepared](https://github.com/lucasiscovici/blog-chat-with-database/tree/base-no-prepared) | The initial setup with an untouched database and LangChain. |
| 2    | [Elevating Implementation - base-prepared](https://github.com/lucasiscovici/blog-chat-with-database/tree/base-prepared) | Enhances the setup by preparing meaningful tables and modalities in the database. |
| 3    | [Descriptive Implementation - description](https://github.com/lucasiscovici/blog-chat-with-database/tree/description) | Focuses on adding clear and concise column descriptions to improve SQL query generation accuracy. |
| 4    | [Fact-Based Implementation - facts](https://github.com/lucasiscovici/blog-chat-with-database/tree/facts) | Enhances user interaction by extracting facts from user inputs for more accurate and relevant SQL queries. |
| 5    | [Crafting Explainable Answers - explainable](https://github.com/lucasiscovici/blog-chat-with-database/tree/explainable) | Aims to provide contextually rich and understandable answers to user queries. |
| Bonus 1 | [Memory Implementation - memory](https://github.com/lucasiscovici/blog-chat-with-database/tree/memory) | Introduces memory features for conversational continuity in the chatbot. |
| Bonus 2 | [Summation Count Enhancement - count](https://github.com/lucasiscovici/blog-chat-with-database/tree/count) | Adds count metrics to summation queries for clearer, more comprehensive responses. |
| Bonus 3 | [SQL Syntax Safeguard - sql-check](https://github.com/lucasiscovici/blog-chat-with-database/tree/sql-check) | Implements checks to prevent SQL syntax issues during data retrieval. |
| Bonus 4 | [Early Stop and Clarification - early-stop](https://github.com/lucasiscovici/blog-chat-with-database/tree/early-stop) | Enhances the chatbot's accuracy by adding clarification requests for complex or incomplete user questions. |

## Installation Instructions

To set up your environment and install all necessary dependencies for this project, follow these steps:

1. **Install Poetry**: If you don't have Poetry installed, you can install it following the instructions on the [Poetry website](https://python-poetry.org/docs/#installation).

2. **Install Dependencies**: Once Poetry is installed, run the following command in your terminal in the project's root directory:

    ```bash
    poetry install
    ```

    This command will install all the dependencies listed in the `pyproject.toml` file, ensuring that your project has all the required packages and is ready to run.

## Usage

### Prerequisites:
- **OpenAI API Key**: You must have an OpenAI API key to use this code. You can obtain it from OpenAI's website.
- **GPT-4 Access**: Ensure you have access to GPT-4, which may require a payment method and prior payment for usage.

### Setting Up Your Environment
Before running the code, you need to set up your environment:

1. **Create a .env File**:
   In the root directory of the project, create a file named `.env`. This file will store your OpenAI API key securely.

2. **Add Your OpenAI API Key**:
   Open the `.env` file in a text editor and add the following line:

   ```
   OPENAI_API_KEY=sk-XXXXXXX
   ```

### Warning: Cost of Usage
Using OpenAI's GPT-4 incurs charges. The total cost for completing the tutorial as described in the blog is approximately €1. This is an estimate and actual costs may vary based on your usage.

### Running the Code
To execute the code, use the following command in your terminal:

```bash
poetry run main
```