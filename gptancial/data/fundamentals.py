"""Fundamentals Data."""
import datetime
from .parser import fmp_json_parser
from .format import transform_multiple_lines_by_date
from .format import transform_one_line_by_date
from .format import try_to_float

def get_financial_ratios(symbol: str) -> str:
    data = fmp_json_parser(path=f"/ratios-ttm/{symbol}", api_version="v3")
    map_names = {
        'dividendYieldTTM': 'Dividend Yield',
        'quickRatioTTM': 'Quick Ratio',
        'cashRatioTTM': 'Cash Ratio',
        'grossProfitMarginTTM': 'Gross Profit Margin',
        'operatingProfitMarginTTM': 'Operating Profit Margin',
        'pretaxProfitMarginTTM': 'Pretax Profit Margin',
        'netProfitMarginTTM': 'Net Profit Margin',
        'effectiveTaxRateTTM': 'Effective Tax Rate',
        'returnOnAssetsTTM': 'Return On Assets',
        'returnOnEquityTTM': 'Return On Equity',
        'returnOnCapitalEmployedTTM': 'Return On Capital Employed',
        'netIncomePerEBTTTM': 'Net Income Per EBT',
        'ebitPerRevenueTTM': 'EBIT Per Revenue',
        'debtRatioTTM': 'Debt Ratio',
        'debtEquityRatioTTM': 'Debt Equity Ratio',
        'longTermDebtToCapitalizationTTM': 'Long Term Debt To Capitalization',
        'totalDebtToCapitalizationTTM': 'Total Debt To Capitalization',
        'interestCoverageTTM': 'Interest Coverage',
        'cashFlowToDebtRatioTTM': 'Cash Flow To Debt Ratio',
        'companyEquityMultiplierTTM': 'Company Equity Multiplier',
        'operatingCashFlowPerShareTTM': 'Operating Cash Flow Per Share',
        'freeCashFlowPerShareTTM': 'Free Cash Flow Per Share',
        'cashPerShareTTM': 'Cash Per Share',
        'operatingCashFlowSalesRatioTTM': 'Operating Cash Flow Sales Ratio',
        'freeCashFlowOperatingCashFlowRatioTTM': 'Free Cash Flow Operating Cash Flow Ratio',
        'cashFlowCoverageRatiosTTM': 'Cash Flow Coverage Ratios',
        'shortTermCoverageRatiosTTM': 'Short Term Coverage Ratios',
        'capitalExpenditureCoverageRatioTTM': 'Capital Expenditure Coverage Ratio',
        'dividendPaidAndCapexCoverageRatioTTM': 'Dividend Paid And Capex Coverage Ratio',
        'priceBookValueRatioTTM': 'Price Book Value Ratio',
        'priceToBookRatioTTM': 'Price To Book Ratio',
        'priceToSalesRatioTTM': 'Price To Sales Ratio',
        'priceEarningsRatioTTM': 'Price Earnings Ratio',
        'priceToFreeCashFlowsRatioTTM': 'Price To Free Cash Flows Ratio',
        'priceToOperatingCashFlowsRatioTTM': 'Price To Operating Cash Flows Ratio',
        'priceCashFlowRatioTTM': 'Price Cash Flow Ratio',
        'priceEarningsToGrowthRatioTTM': 'Price Earnings To Growth Ratio',
        'priceSalesRatioTTM': 'Price Sales Ratio',
        'enterpriseValueMultipleTTM': 'Enterprise Value Multiple',
        'priceFairValueTTM': 'Price Fair Value',
        'dividendPerShareTTM': 'Dividend Per Share',
    }
    data_str = "\n".join([f"{map_names.get(k)}={try_to_float(v)}" for k, v in data[0].items() if k in map_names])
    return "Financial Ratios TTM:\n" + data_str


def get_stock_financial_scores(symbol: str) -> str:
    data = fmp_json_parser(path=f"/score?symbol={symbol}", api_version="v4")
    map_names = {
        "altmanZScore": "Altman Z Score",
        "piotroskiScore": "Piotroski Score",
        "workingCapital": "Working Capital",
        "totalAssets": "Total Assets",
        "retainedEarnings": "Retained Earnings",
        "ebit": "EBIT",
        "marketCap": "Market Cap",
        "totalLiabilities": "Total Liabilities",
        "revenue": "Revenue",
    }
    data_str = "\n".join([f"{map_names.get(k)}={try_to_float(v)}" for k, v in data[0].items() if k in map_names])
    return "Stock Financial Scores:\n" + data_str


def get_company_enterprise_value(symbol: str, records: int = 4) -> str:
    data = fmp_json_parser(path=f"/enterprise-values/{symbol}?period=quarter&limit={records}", api_version="v3")
    map_names = {
        "stockPrice": "Stock Price",
        "numberOfShares": "Number of Shares",
        "marketCapitalization": "Market Capitalization",
        "minusCashAndCashEquivalents": "Minus Cash and Cash Equivalents",
        "addTotalDebt": "Add Total Debt",
        "enterpriseValue": "Enterprise Value",
    }
    return transform_multiple_lines_by_date(data=data, map_names=map_names, records=records, title="Enterprise Values")


def get_company_key_metrics(symbol: str, records: int = 4) -> str:
    data = fmp_json_parser(path=f"/key-metrics/{symbol}?period=quarter&limit={records}", api_version="v3")
    map_names = {
        'period': 'Period',
        'revenuePerShare': 'Revenue Per Share',
        'netIncomePerShare': 'Net Income Per Share',
        'operatingCashFlowPerShare': 'Operating Cash Flow Per Share',
        'freeCashFlowPerShare': 'Free Cash Flow Per Share',
        'cashPerShare': 'Cash Per Share',
        'bookValuePerShare': 'Book Value Per Share',
        'shareholdersEquityPerShare': 'Shareholders Equity Per Share',
        'interestDebtPerShare': 'Interest Debt Per Share',
        'marketCap': 'Market Cap',
        'enterpriseValue': 'Enterprise Value',
        'peRatio': 'PE Ratio',
        'priceToSalesRatio': 'Price To Sales Ratio',
        'pbRatio': 'PB Ratio',
        'earningsYield': 'Earnings Yield',
        'freeCashFlowYield': 'Free Cash Flow Yield',
        'debtToEquity': 'Debt To Equity',
        'debtToAssets': 'Debt To Assets',
        'netDebtToEBITDA': 'Net Debt To EBITDA',
        'currentRatio': 'Current Ratio',
        'interestCoverage': 'Interest Coverage',
        'incomeQuality': 'Income Quality',
        'dividendYield': 'Dividend Yield',
        'payoutRatio': 'Payout Ratio',
        'salesGeneralAndAdministrativeToRevenue': 'Sales General And Administrative To Revenue',
        'researchAndDdevelopementToRevenue': 'Research And Developement To Revenue',
        'intangiblesToTotalAssets': 'Intangibles To Total Assets',
        'capexToOperatingCashFlow': 'Capex To Operating Cash Flow',
        'capexToRevenue': 'Capex To Revenue',
        'capexToDepreciation': 'Capex To Depreciation',
        'roic': 'ROIC',
        'returnOnTangibleAssets': 'Return On Tangible Assets',
        'workingCapital': 'Working Capital',
        'tangibleAssetValue': 'Tangible Asset Value',
        'netCurrentAssetValue': 'Net Current Asset Value',
        'investedCapital': 'Invested Capital',
        'averageReceivables': 'Average Receivables',
        'averagePayables': 'Average Payables',
        'averageInventory': 'Average Inventory',
        'roe': 'ROE',
        'capexPerShare': 'Capex Per Share',
    }
    return transform_multiple_lines_by_date(data=data, map_names=map_names, records=records, title="Company Key Metrics")


def get_financial_growth(symbol: str, records: int = 1) -> str:
    data = fmp_json_parser(path=f"/financial-growth/{symbol}?period=quarter&limit={records}", api_version="v3")
    map_names = {
        'period': 'Period',
        'revenueGrowth': 'Revenue Growth',
        'grossProfitGrowth': 'Gross Profit Growth',
        'ebitgrowth': 'Ebitgrowth',
        'operatingIncomeGrowth': 'Operating Income Growth',
        'netIncomeGrowth': 'Net Income Growth',
        'epsgrowth': 'Epsgrowth',
        'weightedAverageSharesGrowth': 'Weighted Average Shares Growth',
        'dividendsperShareGrowth': 'Dividends per Share Growth',
        'operatingCashFlowGrowth': 'Operating Cash Flow Growth',
        'freeCashFlowGrowth': 'Free Cash Flow Growth',
        'threeYRevenueGrowthPerShare': 'Three Y Revenue Growth Per Share',
        'threeYOperatingCFGrowthPerShare': 'Three Y Operating CF Growth Per Share',
        'threeYNetIncomeGrowthPerShare': 'Three Y Net Income Growth Per Share',
        'threeYShareholdersEquityGrowthPerShare': 'Three Y Shareholders Equity Growth Per Share',
        'threeYDividendperShareGrowthPerShare': 'Three Y Dividend per Share Growth Per Share',
        'receivablesGrowth': 'Receivables Growth',
        'inventoryGrowth': 'Inventory Growth',
        'assetGrowth': 'Asset Growth',
        'bookValueperShareGrowth': 'Book Value per Share Growth',
        'debtGrowth': 'Debt Growth',
        'rdexpenseGrowth': 'R&D Expense Growth',
        'sgaexpensesGrowth': 'SGA Expenses Growth',
    }
    return transform_multiple_lines_by_date(data=data, map_names=map_names, records=records, title="Financial Growth")


def get_rating_recommendations(symbol: str, records: int = 10) -> str:
    data = fmp_json_parser(path=f"/historical-rating/{symbol}", api_version="v3")
    map_names = {
        'ratingRecommendation': 'Generic',
        'ratingDetailsDERecommendation': 'Debt to Equity Ratio',
        'ratingDetailsPERecommendation': 'Price to Earnings Ratio',
        'ratingDetailsPBRecommendation': 'Price to Book Ratio'
    }
    return transform_multiple_lines_by_date(data=data, map_names=map_names, records=records, title="Ratings")


def get_estimtes(symbol: str) -> str:
    data = fmp_json_parser(path=f"/analyst-estimates/{symbol}?period=quarter", api_version="v3")
    map_names = {
        "estimatedRevenueAvg": "Estimated Revenue Avg",
        "estimatedEbitdaAvg": "Estimated EBITDA Avg",
        "estimatedEbitAvg": "Estimated EBIT Avg",
        "estimatedNetIncomeAvg": "Estimated Net Income Avg",
        "estimatedSgaExpenseAvg": "Estimated SGA Expense Avg",
        "estimatedEpsAvg": "Estimated EPS Avg",
    }
    current_date = str(datetime.datetime.now())[0:10]
    index_current = [i for i in range(len(data)) if data[i].get("date") >= current_date]
    if len(index_current) > 0:
        current_data_idx = index_current[0]
        if current_data_idx > 0:
            data = [data[current_data_idx - 1], data[current_data_idx]]
        else:
            data = [data[current_data_idx]]
        return transform_multiple_lines_by_date(data=data, map_names=map_names, records=len(data), title="Estimates")
    return ""
