# agents-test

testing various agent frameworks

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
pip install -U langgraph langsmith langchain_anthropic
python test_langgraph.py
```

### [BrowserUse](https://github.com/browser-use/browser-use)

```bash
conda create -n browseruse python=3.10
conda activate browseruse
pip install browser-use
python test_browseruse.py
```

### [Pydanticai](https://github.com/pydantic/pydantic-ai)

```bash
conda create -n pydanticai python=3.10
conda activate pydanticai
pip install pydantic-ai
python test_pydanticai.py
```

### [smolagents](https://huggingface.co/docs/smolagents/index)

```bash
conda create -n smolagents python=3.10
conda activate smolagents
pip install smolagents
python test_smolagents.py
```