import itertools
import statsmodels.api as sm
import pandas as pd

data = pd.read_excel('sml99.xlsx')


def calculateParam(item):
    # ARIMA 모델의 하이퍼파라미터 후보 값 정의
    p = q = range(0, 4)
    d = range(0, 3)

    # 가능한 하이퍼파라미터 조합 생성
    hyperparameters = list(itertools.product(p, d, q))

    # 최적의 모델 찾기
    best_aic = float("inf")
    best_params = None

    for param in hyperparameters:
        try:
            model = sm.tsa.ARIMA(endog=data[item], order=param)
            results = model.fit()
            aic = results.aic
            if aic < best_aic:
                best_aic = aic
                best_params = param
        except:
            continue

    return best_params
