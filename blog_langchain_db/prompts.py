from langchain.prompts import PromptTemplate

SQL_QUERY_PROMPT_TEXT="""-- Language : SQL
-- Dialect : SQLITE
-- Here are the table schemas :
{schemas}
-- A SQL query to return 1 and a SQL query for "{question}". Please only make a stand-alone query. DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.
SELECT 1;"""

SQL_QUERY_PROMPT = PromptTemplate.from_template(SQL_QUERY_PROMPT_TEXT)

RESPONSE_PROMPT_TEXT="""As a SQL specialist, I'll format the answer to your question and query response, ensuring a conversational, polite, formal, and factual presentation, while adhering to standard financial notation for numerical values.

The user's question : {question}.
The query response : {response}.
The answer:"""

RESPONSE_PROMPT = PromptTemplate.from_template(RESPONSE_PROMPT_TEXT)

