## 🧑‍🤖 `app/resume_ai.py`python
import openai
import os

openrouter.api_key = os.getenv("OPEN-ROUTER_API_KEY")

async def generate_letter(name, company, gender, job):
    prompt = f"""
    Rédige une lettre de motivation pour {name} destinée à l'entreprise {company},
    secteur: {job['sector']}, poste: {job['title']}. Le destinataire est un(e) {gender}.
    Respecte les en-têtes professionnels et adapte le ton.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
