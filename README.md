# llm-website-wizard
Scrape a website and tells summary and create a brochure.
This repo is based on the guideline by `Ed Donner's` [LLM Engineering repo](https://github.com/ed-donner/llm_engineering/tree/main/week1) which is used at his [Udemy AI Engineering Core Track](https://www.udemy.com/course/llm-engineering-master-ai-and-large-language-models/) course. 

# Getting Started
- Preapare the python environemnt by:
```
$ uv sync
```

- Add .env file with the `Gemini API Key`:
```
GEMINI_API_KEY=your_key
```

- Run the following for a website summary

```
$ uv run  website-summary.py   
```

- Run the following for a website brochure

```
$ uv run  website-brochure.py   
```

# Gradio Front
- To get the front page using gradio, use:

```
$ uv run front.py
```
