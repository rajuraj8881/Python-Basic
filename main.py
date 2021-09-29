# import matplotlib
# #check matplotlib version
# print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

# xpoint = np.array([0, 0])
# ypoint = np.array([0, 250])
#
# plt.plot(xpoint)
# plt.plot(ypoint)
# plt.show()

# xpoint = np.array([1, 8])
# ypoint = np.array([6, 6])
#
# apoint = np.array([4, 4])
# bpoint = np.array([3, 10])
#
# plt.plot(xpoint, ypoint, 'o')
# plt.plot(apoint, bpoint, 'o')
# plt.show()

# xpoint = np.array([1, 2, 6, 8])
# ypoint = np.array([3, 8, 1, 10])
# plt.plot(xpoint, ypoint)
# plt.show()

#Default X-Points
# ypoint = np.array([3, 8, 1, 10, 5, 7])
# plt.plot(ypoint)
# plt.show()

#Matplotlib Markers
ypoint = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoint, marker = 'o')
plt.show()
