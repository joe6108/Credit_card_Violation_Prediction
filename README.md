# 睡眠品質之預測

## Introtuce
無論何時，睡覺都是一件非常重要的事情，但常常睡著了之後又會因為睡眠品質不佳，睡的不好，那又該如何提升睡覺品質?
本次訓練結果打算偏重於從易得的，且公平的資訊如入寢時間，起床時間，步數等等，去簡單預測睡眠品質的好壞。

## Environment
1. VScode
2. python 3.8
3. MiniConda
## Request module -> conda
1. `conda install pandas -y`
2. `conda install scikit-learn -y`
# Name - sleepdata.csv
- Start(入睡時間)
```
以農曆時間為基準。
```
- End(起床時間)
```
以農曆時間為基準。
```
- Sleep quality	(睡眠品質)
```
以0%(Low)~100%(High)為基底，越高就擁有越好的睡眠品質。
```
- Time in bed(睡覺時間)
```
起床時間 - 入睡時間
```
- Wake up(起床時的心情) --> delete
```
起床時的心情指數。
由於這項數值缺少了太多項，決定廢棄。
```
- Sleep Notes (睡前筆記)
```
代表此人睡前做了些甚麼，數據如下
'Stressful day' : 有壓力的一天 -2
'Drank coffee' : 喝咖啡 -2
'Drank tea' 喝茶 -1
'Ate late' 晚餐比較晚吃 -1
'Worked out' 鍛鍊身體 +2
```
- Heart rate(心率) --> delete
```
由於我判斷這項數值在睡前不易於取得，所以廢棄
```
- Activity (步數)
```
睡前一整天行走的步數
```
## 資料庫來源
- Kaggle 
```
https://www.kaggle.com/datasets/danagerous/sleep-data
```
