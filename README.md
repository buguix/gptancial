# GPTancial

Using GPT for financial analysis of a stock

## Installation

Using docker:

```bash
cd gptancial
docker build -t gptancial .
docker run --name gptancial \
    -e FMP_API_KEY=insert-fmp-api-key-here \
    -e OPEN_AI_API_KEY=insert-open-api-key-here \
    -p 8080:8080 \
    -d gptancial
```

Using poetry:

```bash
export FLASK_APP=gptancial
export FMP_API_KEY=insert-fmp-api-key-here
export OPEN_AI_API_KEY=insert-open-api-key-here
poetry install
poetry run flask run -h 0.0.0.0 -p 8080
```

## Usage

Open your browser in this location: [localhost:8080](http://localhost:8080)

## Repository Code

```bash
.
|__ analytics/      # methods for getting preparing the financial data and generate the open ai responses
|__ data/           # methods for fetching data from financial model preparation library
|__ templates/      # html files that serve the app
```

### analytics
The analytics folder contains one file (logic.py) that is responsible for fetching the required data to serve as input for the models. The other file (openai.py) exposes the methods to call Open AI API. If the engine/models need to be changed, this is the file that needs to be changed.

### data
The data is being fetched from [Financial Modelling Preparation](https://site.financialmodelingprep.com/developer/docs/) API. You'll need an API key to use it. The data module exposes the methods to fetch the data, select the indicators and transform it to text to be used in the Open AI models.
