import matplotlib
import matplotlib.pyplot as plt
from matplotlib import figure
import numpy as np
import pandas as pd
stockdata = pd.read_csv("dow_jones_index.data", parse_dates=['date'], index_col=['date'], nrows=100)
stockdata_new = pd.DataFrame(stockdata, columns = ["stock","open","high","low","close","volume"])
stockdata_new.open = pd.to_numeric(stockdata_new.open.str.replace('$', ""))
stockdata_new.close = pd.to_numeric(stockdata_new.close.str.replace('$', ""))
(stockdata_new.close - stockdata_new.open).infer_objects()
stockdata_new["newopen"] = stockdata_new.open.apply(lambda x: 0.8*x)

stockCSCO = stockdata_new.query('stock=="CSCO"')
stockAA = stockdata_new.query('stock=="AA"')
# print(stockCSCO.head())

# plt.figure()
# plt.scatter(stockdata_new.index.date,stockdata_new.volume)
# plt.xlabel('day')
# plt.ylabel('stock close value')
# plt.title('title')
# plt.savefig("matplot1.jpg")

# plt.subplot(2, 2, 1)
# plt.plot(stockAA.index.weekofyear, stockAA.open, 'r--')
# plt.subplot(2, 2, 2)
# plt.plot(stockCSCO.index.weekofyear, stockCSCO.open, 'g-*')
# plt.subplot(2, 2, 3)
# plt.plot(stockAA.index.weekofyear, stockAA.open, 'g--')
# plt.subplot(2, 2, 4)
# plt.plot(stockCSCO.index.weekofyear, stockCSCO.open, 'r-*')

# plt.savefig("matplot2.png")

# fig = plt.figure()
# ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# ax.plot(stockAA.index.weekofyear,stockAA.open,label="AA")
# ax.plot(stockAA.index.weekofyear,stockCSCO.open,label="CSCO")
# ax.set_xlabel('weekofyear')
# ax.set_ylabel('stock value')
# ax.set_title('Weekly change in stock price')
# ax.legend(loc=2)
# plt.savefig("matplot3.jpg")
plt.scatter(stockAA.index.weekofyear,stockAA.open)
plt.savefig("matplot4.jpg")
plt.close()