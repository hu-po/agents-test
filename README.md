# agents-test

testing various agent frameworks, make sure to `export OPENAI_API_KEY=your-api-key`

### [BrowserUse](https://github.com/browser-use/browser-use)

```bash
conda create -n browser-use python=3.11
conda activate browser-use
pip install browser-use pytest-playwright
playwright install
python test_browseruse.py
```

### [Pydanticai](https://ai.pydantic.dev/agents/)

```bash
conda create -n pydanticai python=3.10
conda activate pydanticai
pip install pydantic-ai
python test_pydanticai.py
```

### [DSPy](https://dspy.ai/#__tabbed_3_1)

```bash
conda create -n dspy python=3.10
conda activate dspy
pip install dspy
python test_dspy.py
```

### [LangGraph](https://langchain-ai.github.io/langgraph/tutorials/introduction/)

```bash
conda create -n langgraph python=3.10
conda activate langgraph
pip install -U langchain langgraph langsmith langchain_openai
python test_langgraph.py
```

### [smolagents](https://huggingface.co/docs/smolagents/index)

```bash
conda create -n smolagents python=3.11
conda activate smolagents
pip install smolagents
python test_smolagents.py
```