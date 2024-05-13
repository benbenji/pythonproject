"""
利用pytorch 同时训练两个神经网络
"""
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt

# 生成数据
x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)
y = x.pow(2) + 0.2 * torch.rand(x.size())

# 定义网络
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(1, 10)
        self.fc2 = nn.Linear(10, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

net1 = Net()
net2 = Net()

# 定义优化器
optimizer = optim.SGD(list(net1.parameters()) + list(net2.parameters()), lr=0.2)

# 定义损失函数
loss_func = nn.MSELoss()

# 训练网络
for epoch in range(100):
    prediction1 = net1(x)
    prediction2 = net2(x)

    loss1 = loss_func(prediction1, y)
    loss2 = loss_func(prediction2, y)

    optimizer.zero_grad()

    loss1.backward()
    loss2.backward()

    optimizer.step()

    if epoch % 10 == 0:
        plt.cla()
        plt.scatter(x.data.numpy(), y.data.numpy())
        plt.plot(x.data.numpy(), prediction1.data.numpy(), 'r-', lw=5)
        plt.plot(x.data.numpy(), prediction2.data.numpy(), 'g-', lw=5)
        plt.text(0.5, 0, 'Loss=%.4f' % loss1.item(), fontdict={'size': 20, 'color': 'red'})
        plt.text(0.5, 0.5, 'Loss=%.4f' % loss2.item(), fontdict={'size': 20, 'color': 'green'})
        plt.pause(0.1)