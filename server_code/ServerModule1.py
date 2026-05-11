import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
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

def verify_user_articles(article):
  current_user = anvil.users.get_user()
  if current_user is not None:
    if app_tables.articles.has_row(article) and article['user'] == current_user:
      return True

def verify_user_chat(responses):
  current_user = anvil.users.get_user()
  if current_user is not None:
    if app_tables.responselog.has_row(responses) and responses['user'] == current_user:
      return True

def verify_user_ref(user_references):
  current_user = anvil.users.get_user()
  if current_user is not None:
    if app_tables.articles.has_row(user_references) and user_references['user'] == current_user:
      return True

@anvil.server.callable
def add_article(article_dict):
  current_user = anvil.users.get_user()

  if current_user is not None:
    app_tables.articles.add_row(
      created=datetime.now(),
      user=current_user,
      **article_dict
    )

@anvil.server.callable
def get_articles():
  current_user = anvil.users.get_user()

  if current_user is not None:
    return app_tables.articles.search(
     tables.order_by("created", ascending=False),
      user=current_user
    )

@anvil.server.callable
def update_article(article, article_dict):

  if verify_user_articles(article):
      article_dict['updated'] = datetime.now()
      article.update(**article_dict)
  else:
    raise Exception("Article does not exist or does not belong to this user")

  
@anvil.server.callable
def delete_article(article):
  if verify_user_articles(article):
    article.delete()
  else:
    raise Exception("Article does not exist or does not belong to this user")

@anvil.server.callable
def generate_questions(input):
  current_user = anvil.users.get_user()
  if anvil.server.context.client.type is None:
    context = "Obfuscated"
  else:
    context = anvil.server.context.client.type

  if current_user:
    client = genai.Client(api_key=anvil.secrets.get_secret('gemini_api_key'))
  
    system_prompt = """STRICT INSTRUCTION: You are a writing assistant for fictional short stories. 
  
  1. Never write stories, scenes, or dialogue for the user.
  2. If a user asks you to write something, refuse and ask a probing question instead.
  3. Your goal is to ask questions that help the writer discover their own ideas.
  4. Provide structural feedback (e.g., 'Your pacing is fast here').
  5. Keep responses short and focused on the writer's thought process.
  
  Again, your role is to ask probing questions and encourage the writer to think."""
  
    chat_history = app_tables.responselog.search(user=current_user)
    context_string = ""
    for row in chat_history:
      context_string += f"User: {row['user_prompts']}\nAssistant: {row['responses']}\n"
  
    full_prompt = f"{system_prompt}\n\nPast Conversation:\n{context_string}\n\nNew User Input: {input}"
  
    response = client.models.generate_content(
      model = "gemini-3.1-flash-lite-preview",
      contents=full_prompt
    )
  
    app_tables.responselog.add_row(
      user=current_user,
      user_prompts=input,
      responses=response.text,
      context=context)
    return response.text
  else:
    return []


@anvil.server.callable
def summarize_chat():
  current_user = anvil.users.get_user()
  logs = app_tables.responselog.search(user=current_user)
  if not logs:
    return "No history to summarize."

  history_text = "\n".join([f"User: {r['user_prompts']} AI: {r['responses']}" for r in logs])

  client = genai.Client(api_key=anvil.secrets.get_secret('gemini_api_key'))
  summary_response = client.models.generate_content(
    model="gemini-3.1-flash-lite-preview",
    contents=f"Summarize the key story ideas and decisions from this chat into bullet points:\n{history_text}"
  )
  summary = summary_response.text

  if anvil.server.context.client.type is None:
    context = "Obfuscated"
  else:
    context = anvil.server.context.client.type

  app_tables.references.add_row(
    user_references=summary,
    created=datetime.now(),
    user=current_user,
    context=context)

  for row in logs:
    row.delete()
    
  return summary
  
@anvil.server.callable
def add_ref(new_ref):
  current_user = anvil.user.get_user()

  if current_user is not None:
    app_tables.references.add_row(
    user_references=new_ref,
    created=datetime.now(),
    user=current_user
    )
  else:
    raise Exception("Article does not exist or does not belong to this user")

@anvil.server.callable
def show_ref():
  current_user = anvil.users.get_user()
  items = app_tables.references.search(
    user=current_user
    )
  return items
