# 📝 BriefBot — AI Text Summarizer

**Long text in, clear summary out.**

BriefBot is a web app that turns long, complex text into short, clear summaries. It comes in two versions:

- **AI version (`app.py`)**: uses Google's Gemini AI to write summaries in fresh, simple language.
- **No-API-key version (`app_nokey.py`)**: works fully offline by picking the most important sentences from your text. No API key or internet needed.

---

## Features

- **Multiple summary lengths**: short, balanced, or detailed
- **Flexible output formats**: paragraph, bullet points, or study notes
- **Text input**: paste text directly into the app
- **File upload**: upload `.txt` or `.md` files
- **Word and character count** for your input
- **Live output** while the summary is generated (AI version)
- **Key terms** in study notes (no-key version)
- **Download** the summary as a text file
- **Clean, simple interface** built with Streamlit

---

## Technologies Used

- Python
- Streamlit
- Google Gemini API (AI version)
- Google Gen AI Python SDK (`google-genai`)
- python-dotenv

---
https://breifbot-hi4nd8h9swnoht7wgfemkj.streamlit.app/

## Project Structure

```
BREIFBOT/
├── app.py              # AI version (Gemini)
├── app_nokey.py        # Offline version (no API key)
├── requirements.txt
├── .env.example        # Example of the environment file
├── .gitignore
└── README.md
```

---

## Installation and Setup

### 1. Clone the repository

```
git clone https://github.com/vaishuvaishu0286-cpu/BREIFBOT.git
cd BREIFBOT
```

### 2. Create a virtual environment (recommended)

```
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac / Linux
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## Running the App

### Option A: AI version (needs a Gemini API key)

1. Get a free API key from [Google AI Studio](https://aistudio.google.com/apikey).
2. Create a file named `.env` in the project folder with one line:

   ```
   GEMINI_API_KEY=your_gemini_api_key
   ```

   Use the key only, with no quotes and no spaces around `=`.

3. Run:

   ```
   streamlit run app.py
   ```

### Option B: No-API-key version

No setup needed. Just run:

```
streamlit run app_nokey.py
```

The app opens in your default browser.

---

## How the Two Versions Differ

| | AI version (`app.py`) | No-key version (`app_nokey.py`) |
|---|---|---|
| Summary style | Rewrites in new, simple sentences | Selects key sentences from the original |
| API key | Required | Not required |
| Internet | Required | Not required |
| Best for | Highest-quality summaries | Quick, private, offline use |

The no-key version scores each sentence by how often its important words appear in the text, then keeps the top sentences in their original order.

---

## Deployment (Streamlit Community Cloud)

1. Push the project files to this GitHub repository.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/) and connect the repository.
3. Select `app.py` (or `app_nokey.py`) as the main file.
4. For the AI version, add your key under **Settings → Secrets**:

   ```
   GEMINI_API_KEY = "your_gemini_api_key"
   ```

5. Deploy the app.

---

## Use Cases

- Summarizing academic notes and study materials
- Understanding lengthy articles and documents
- Preparing quick revision notes
- Extracting key points from large amounts of text

---

## Future Enhancements

- Support for PDF and DOCX files
- Multilingual summarization
- Summary history
- Keyword highlighting
- Additional output formats

---

