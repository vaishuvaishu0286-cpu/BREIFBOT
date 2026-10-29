import re
from collections import Counter

import streamlit as st

APP_NAME = "BriefBot (No API Key)"

st.set_page_config(page_title=APP_NAME, page_icon="📝", layout="centered")

STOPWORDS = set("""
a about above after again all also am an and any are as at be because been before being below between both but by
can could did do does doing down during each few for from further had has have having he her here hers him his how
i if in into is it its itself just me more most my no nor not now of off on once only or other our out over own same
she should so some such than that the their theirs them then there these they this those through to too under until
up very was we were what when where which while who whom why will with would you your yours
""".split())


def split_sentences(text: str):
    text = re.sub(r"\s+", " ", text.strip())
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"'(])", text)
    return [p.strip() for p in parts if len(p.strip()) > 20]


def tokenize(text: str):
    return [w for w in re.findall(r"[a-zA-Z']+", text.lower()) if w not in STOPWORDS and len(w) > 2]


def summarize(text: str, length: str):
    sentences = split_sentences(text)
    if not sentences:
        return [], []

    freq = Counter(tokenize(text))
    if not freq:
        return sentences[:3], []
    top = max(freq.values())
    norm = {w: c / top for w, c in freq.items()}

    scores = []
    for i, s in enumerate(sentences):
        words = tokenize(s)
        if not words:
            scores.append(0)
            continue
        score = sum(norm.get(w, 0) for w in words) / (len(words) ** 0.6)
        if i == 0:
            score *= 1.2  # first sentence usually introduces the topic
        scores.append(score)

    n = len(sentences)
    if length == "Short":
        k = min(3, n)
    elif length == "Balanced":
        k = max(4, round(n * 0.25))
    else:
        k = max(6, round(n * 0.45))
    k = min(k, n)

    best = sorted(sorted(range(n), key=lambda i: scores[i], reverse=True)[:k])  # keep original order
    keywords = [w for w, _ in freq.most_common(8)]
    return [sentences[i] for i in best], keywords


def format_output(sents, keywords, fmt):
    if fmt == "Paragraph":
        return " ".join(sents)
    if fmt == "Bullet points":
        return "\n".join(f"- {s}" for s in sents)
    notes = "## Key Points\n" + "\n".join(f"- {s}" for s in sents)
    if keywords:
        notes += "\n\n## Key Terms\n" + ", ".join(f"**{k}**" for k in keywords)
    return notes


# ---------- UI ----------
st.title(f"📝 {APP_NAME}")
st.caption("Works offline. No API key needed.")

col1, col2 = st.columns(2)
length = col1.selectbox("Summary length", ["Short", "Balanced", "Detailed"], index=1)
fmt = col2.selectbox("Output format", ["Paragraph", "Bullet points", "Study notes"])

uploaded = st.file_uploader("Upload a text file (.txt or .md)", type=["txt", "md"])
text = st.text_area("...or paste your text here", height=250)

if uploaded is not None:
    text = uploaded.read().decode("utf-8", errors="ignore")
    st.info(f"Loaded file: {uploaded.name}")

if text:
    st.caption(f"Words: {len(text.split())}  |  Characters: {len(text)}")

if st.button("Summarize", type="primary", use_container_width=True):
    if not text.strip():
        st.warning("Please paste some text or upload a file first.")
    else:
        sents, keywords = summarize(text, length)
        if not sents:
            st.warning("Text is too short to summarize. Add a few full sentences.")
        else:
            result = format_output(sents, keywords, fmt)
            st.subheader("Summary")
            st.markdown(result)
            st.download_button("⬇️ Download summary", data=result, file_name="summary.txt", mime="text/plain")

st.divider()
st.caption("This version picks the most important sentences from your text. It does not rewrite them like an AI model.")