# OmniEngage AI — LLM Pipeline for Healthcare Member Engagement

**Domain:** NLP / LLMs · Healthcare communications · **Platform:** Google Cloud Vertex AI

---

## Overview

I built OmniEngage AI to demonstrate production-grade LLM pipeline design for a regulated industry context. The system analyzes member call transcripts at scale, surfaces behavioral patterns, and generates optimized digital engagement messages — all within the safety and compliance constraints of healthcare communications.

This project reflects the Vertex AI pipeline work I do at CVS Health, where I build and deploy LLM-powered systems for Caremark member interactions across 60M+ member records.

---

## Business problem

Healthcare organizations generate millions of member interactions annually across calls, portal sessions, and app usage. Manual review of call transcripts and ad hoc message optimization don't scale and leave significant cost and engagement opportunities on the table. This project answers:

1. Can LLMs reliably extract intent, sentiment, and call drivers from healthcare call transcripts?
2. How do you engineer prompts for consistency, safety, and output quality in a regulated context?
3. What does a production-ready RAG workflow look like for member FAQ responses?
4. How can generative AI optimize digital engagement messages by member segment?

---

## System components

### 1. Transcript analysis pipeline
- Input: Anonymized synthetic call transcripts (1,000+ examples across 12 call reason categories)
- Processing: Vertex AI Gemini Pro via the Python SDK
- Output: Structured JSON per transcript — call reason, member sentiment, escalation flag, resolution status, recommended next action
- Prompt design: Chain-of-thought prompting with JSON schema enforcement; few-shot examples calibrated for edge cases and ambiguous intents

### 2. Topic modeling and NLP analysis
- BERTopic for unsupervised discovery of call driver clusters across the transcript corpus
- Sentence-level sentiment scoring using VADER and a fine-tuned DistilBERT classifier
- Comparison of LLM-extracted topics vs. BERTopic clusters to validate consistency
- t-SNE visualization of topic cluster separation

### 3. RAG-powered member FAQ system
- Document store: Synthetic plan benefit documents chunked and embedded via `text-embedding-004`
- Vector retrieval: FAISS cosine similarity search over benefit document embeddings
- Generation: Vertex AI Gemini with retrieved context; responses grounded to source documents
- Safety layer: Output filtering for PII, unsupported medical claims, and off-topic responses
- Evaluation: Faithfulness scoring to confirm responses don't hallucinate beyond source documents

### 4. Digital message optimization
- Prompt-based generation of SMS and email engagement messages by member segment
- Controlled variation across tone (warm vs. direct), reading level (6th vs. 10th grade), and call-to-action type
- Evaluation: BERTScore for semantic quality, Flesch-Kincaid for readability, human preference simulation

### 5. Prompt engineering library
Full documented prompt library showing:
- Zero-shot vs. few-shot performance comparison on transcript classification
- Structured output prompts with JSON schema enforcement
- Safety prompt patterns specific to healthcare context
- Iterative refinement log showing prompt version history and measurable output quality gains at each step

---

## Key results

| Component | Metric | Result |
|---|---|---|
| Transcript classification | Accuracy vs. human labels | 89% on 200-sample eval set |
| RAG FAQ system | Faithfulness score | 0.91 (no hallucination beyond source) |
| Topic modeling | Coherence score (C_v) | 0.64 (BERTopic) |
| Message optimization | BERTScore F1 | 0.87 vs. human-written baseline |

---

## File structure

```
OmniEngage_AI/
├── README.md
├── README1.md                          # Legacy file — superseded by this README
├── data/
│   └── synthetic_transcripts.jsonl
├── notebooks/
│   ├── 01_transcript_analysis_pipeline.ipynb
│   ├── 02_topic_modeling_bertopic.ipynb
│   ├── 03_rag_faq_system.ipynb
│   └── 04_message_optimization.ipynb
├── src/
│   ├── vertex_pipeline.py
│   ├── prompt_library.py
│   ├── rag_retriever.py
│   └── safety_filter.py
├── prompts/
│   └── prompt_versions.md
└── requirements.txt
```

---

## Running the project

```bash
pip install -r requirements.txt

# Set your Vertex AI project credentials
export GOOGLE_CLOUD_PROJECT=your-project-id

# Run notebooks in order, or explore individual components
jupyter notebook notebooks/01_transcript_analysis_pipeline.ipynb
```

A local demo mode using mock responses is available for running without Vertex AI credentials — see `src/vertex_pipeline.py` for the `--mock` flag.

---

## Skills demonstrated

`Vertex AI` · `Gemini Pro` · `prompt engineering` · `chain-of-thought prompting` · `RAG` · `FAISS` · `BERTopic` · `DistilBERT` · `sentence-transformers` · `LangChain` · `Python` · `safety filtering` · `NLP evaluation` · `BERTScore` · `healthcare AI`

---

*All data is synthetic. No real member information is used. Prompt patterns and pipeline architecture reflect production work at CVS Health with identifying details removed.*
