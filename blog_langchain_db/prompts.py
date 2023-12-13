from langchain.prompts import PromptTemplate


FACTS_PROMPT_STR = """
-- Here is the question of the user :
{question}
-- Here is the conversation with the user (the last is the most recent); Use it to better understand the question of the user :
{history}
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
-- Here is the conversation with the user (the last is the most recent). Don't use it to generate the SQL query, it's only used to understand the context.
{history}
-- A SQL query to return 1 and a SQL query for "{question}". Please only make a stand-alone query. DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.
Always include a WHERE condition to exclude NULL values. IMPORTANT: Whenever you use a SQL 'SUM' operation, always accompany it with a 'COUNT' operation for the NOT NULL values being summed.
SELECT 1;"""

SQL_QUERY_PROMPT = PromptTemplate.from_template(SQL_QUERY_PROMPT_TEXT)

RESPONSE_PROMPT_TEXT="""As a SQL specialist, I'll format the answer to your question and query response, ensuring a conversational, polite, formal, and factual presentation, while adhering to standard financial notation for numerical values.

The history of the conversation (the last is the most recent):
---------
{history}
---------
The user's question : {question}.
The facts: {facts}.
The SQL query: {query}.
The query response : {response}.
The answer (with clear, concise explanations to the user, not an SQL specialist, using facts, the SQL query, and response) :"""

RESPONSE_PROMPT = PromptTemplate.from_template(RESPONSE_PROMPT_TEXT)

SQL_FIXER_PROMPT_TEXT="""
You have to rewrite the sql query which causes the errors listed bellow. You must use the table descriptions and schemas to rewrite the sql query.

-- Here are the descriptions of the table schemas; please read them carefully to better understand the table:
{descriptions}
-- Here are the table schemas :
{schemas}
-- Here is the query to check:
{query}
-- Here are the query errors:
{errors}

Double check the SQLITE query above for common mistakes, including:
- Using NOT IN with NULL values
- Using UNION when UNION ALL should have been used
- Using BETWEEN for exclusive ranges
- Data type mismatch in predicates
- Properly quoting identifiers
- Using the correct number of arguments for functions
- Casting to the correct data type
- Using the proper columns for joins

Output the final SQL query only.

SQL Query: """

SQL_FIXER_PROMPT = PromptTemplate.from_template(SQL_FIXER_PROMPT_TEXT)
