# Training Problem

## 1. Introduction

### Related Work

_Abstract 部分_

[url1](https://www.researchgate.net/publication/236463111_Sales_Prediction_with_Parametrized_Time_Series_Analysis)

### Model Overview

**在问题一中，我们用加法模式的时间序列模型模拟销售额变化。首先，通过时间-销售额图的初步分析判断，我们列举了可能的影响因素；其次，对每个因素分别选择加权移动平均法、季节趋势预测法、指数平滑法等适当的分析方法得到每个因素的参数；再次，通过线性回归模型拟合曲线，得到修正后的结果；最后，根据参数确定该因素与销售额的相关性，确定最终影响因素。**

**在问题二中，**

## 2. Assumptions and Notations

### Assumptions

```
>1.期间外界经济环境平稳没有动荡
>2.忽略付款方式及抹零的影响
>3.忽略季节因素的影响
>4.每个门店销售的水果种类一致且充足，打折优惠保持一致
```

## 3. Model Construction
