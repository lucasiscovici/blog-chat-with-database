from langchain.prompts import PromptTemplate


FACTS_PROMPT_STR = """
-- Here is the question of the user :
{question}
-- Here are the descriptions of the table schemas; please read them carefully to better understand the table:
{descriptions}
-- Here are the table schemas :
{schemas}
Review the tables, noting that some columns are for filtering ("Key Columns" or "Index Columns") and others contain specific values ("Data Columns" or "Value Columns").
-- Create a bulleted list identifying all implicit facts from a user’s question, focusing on implicit values in the 'Key' or 'Index Columns.'
Use common sense to infer only obvious values, include pertinent date information (months/years, ...), and especially specify all necessary calculations (e.g., using SQL SUM, MAX, or simple column selection).
Don't make hasty decisions; try to be factual and infer values only when truly necessary, using common sense.
Ensure your decisions are thoughtful and factual, and then, rephrase the user’s question based on these facts, indicating it's a potential rewrite.
Present your answer as a bulleted list:
- """
FACTS_PROMPT = PromptTemplate.from_template(FACTS_PROMPT_STR)


SQL_QUERY_PROMPT_TEXT="""-- Language : SQL
-- Dialect : SQLITE
-- Here are the descriptions of the table schemas; please read them carefully to better understand the table:
{descriptions}
-- Here are the table schemas :
{schemas}
-- Here are the interesting facts:
{facts}
-- A SQL query to return 1 and a SQL query for "{question}". Please only make a stand-alone query. DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.
SELECT 1;"""

SQL_QUERY_PROMPT = PromptTemplate.from_template(SQL_QUERY_PROMPT_TEXT)

RESPONSE_PROMPT_TEXT="""As a SQL specialist, I'll format the answer to your question and query response, ensuring a conversational, polite, formal, and factual presentation, while adhering to standard financial notation for numerical values.

The user's question : {question}.
The facts: {facts}.
The SQL query: {query}.
The query response : {response}.
The answer:"""

RESPONSE_PROMPT = PromptTemplate.from_template(RESPONSE_PROMPT_TEXT)

