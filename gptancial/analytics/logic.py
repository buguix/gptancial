"""Logic."""
from typing import Optional
from typing import Tuple

from gptancial.data import get_financial_ratios
from gptancial.data import get_financial_growth
from gptancial.data import get_stock_financial_scores
from gptancial.data import get_company_enterprise_value
from gptancial.data import get_company_key_metrics
from gptancial.data import get_rating_recommendations
from gptancial.data import get_estimtes
from gptancial.data import get_esg_score
from gptancial.data import get_social_sentiment
from gptancial.data import get_last_price_data

from .openai import generate_completion
from .openai import generate_chat


def _get_symbol_data_prompt(symbol: str) -> str:
    fr = get_financial_ratios(symbol=symbol)
    fs = get_stock_financial_scores(symbol=symbol)
    fg = get_financial_growth(symbol=symbol, records=1)
    ev = get_company_enterprise_value(symbol=symbol)
    km = get_company_key_metrics(symbol=symbol)
    rec = get_rating_recommendations(symbol=symbol, records=5)
    est = get_estimtes(symbol=symbol)
    esg = get_esg_score(symbol=symbol)
    sent = get_social_sentiment(symbol=symbol)
    price = get_last_price_data(symbol=symbol)

    return "\n\n".join([fr, fs, fg, ev, km, rec, est, esg, sent, price])


def generate_analysis(
    symbol: str,
    engine: str = "text-davinci-002",
    max_tokens: int = 256,
    n_completitons: int = 1,
    temperature: float = 0.5,
) -> Tuple[str, str]:
    prompt_data = _get_symbol_data_prompt(symbol=symbol)
    res_data = generate_completion(
        symbol=symbol,
        engine=engine,
        data_input=prompt_data,
        max_tokens=max_tokens,
        n_completitons=n_completitons,
        temperature=temperature,
    )

    return prompt_data, "\n\n".join(res_data)


def handle_user_question(
    symbol: str,
    user_question: str,
    prompt_data: Optional[str] = None,
    model: str = "gpt-3.5-turbo",
) -> str:
    return generate_chat(
        symbol=symbol,
        model=model,
        data_input=prompt_data or _get_symbol_data_prompt(symbol=symbol),
        user_question=user_question,
    )
