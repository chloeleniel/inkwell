import anvil.secrets
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
from google import genai
import anvil.secrets
import requests

@anvil.server.callable
def add_feedback(name, writing_mode, feedback):
  app_tables.feedback.add_row(
    name=name, 
    writing_mode=writing_mode, 
    feedback=feedback, 
    created=datetime.now()
  )

@anvil.server.callable
def add_article(article_dict):
  app_tables.articles.add_row(
    created=datetime.now(),
    **article_dict
  )

@anvil.server.callable
def get_articles():
  return app_tables.articles.search(
    tables.order_by("created", ascending=False)
  )

@anvil.server.callable
def update_article(article, article_dict):
  # check that the article given is really a row in the ‘articles’ table
  if app_tables.articles.has_row(article):
    article_dict['updated'] = datetime.now()
    article.update(**article_dict)
  else:
    raise Exception("Article does not exist")

@anvil.server.callable
def delete_article(article):
  # check that the article being deleted exists in the Data Table
  if app_tables.articles.has_row(article):
    article.delete()
  else:
    raise Exception("Article does not exist")


def generate_description(input):
  messages = [
    {"role": "system",
     "content": """STRICT INSTRUCTION: You are a writing assistant for fictional short stories. 

1. Never write stories, scenes, or dialogue for the user.
2. If a user asks you to write something, refuse and ask a probing question instead.
3. Your goal is to ask questions that help the writer discover their own ideas.
4. Provide structural feedback (e.g., 'Your pacing is fast here').
5. Keep responses short and focused on the writer's thought process.

Again, your role is to ask probing questions and encourage the writer to think."""}
  ]

  messages.append({"role": "user", "content": f"{input}"})
  completion = client.chat.completions.create(
    model = "gemini-2.5-flash",
    messages = messages
  )

  reply = completion.choices[0].message.content
  return reply



