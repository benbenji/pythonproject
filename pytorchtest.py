'''
利用pytorch实现一个人脸识别的模型，加载标准数据集，训练模型，测试模型
'''
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import torch.utils.data as data
import torch.nn.functional as F
import os
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print("Using device:", device)
os.environ['KMP_DUPLICATE_LIB_OK']='TRUE'
# 1.加载数据集
# 数据集路径
data_path = 'data'
# 训练集
train_data = datasets.CIFAR10(data_path, train=True, transform=transforms.ToTensor(), download=True)
# 测试集
test_data = datasets.CIFAR10(data_path, train=False, transform=transforms.ToTensor(), download=True)
# 数据加载器
train_loader = data.DataLoader(train_data, batch_size=64, shuffle=True)
test_loader = data.DataLoader(test_data, batch_size=64, shuffle=False)

# 2.定义模型
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# 3.训练模型
# 创建模型
net = Net().to(device)
# 损失函数
criterion = nn.CrossEntropyLoss()
# 优化器
optimizer = optim.SGD(net.parameters(), lr=0.01, momentum=0.9)
# 训练模型
for epoch in range(10):
    running_loss = 0.0
    for i, data in enumerate(train_loader, 0):
        inputs, labels = data[0].to(device), data[1].to(device)
        optimizer.zero_grad()
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss =running_loss+loss.item()
    print('[%d, %5d] loss: %.3f' % (epoch + 1, i + 1, running_loss/i))
print('Finished Training')

# 4.测试模型
correct = 0
total = 0
with torch.no_grad():
    for data in test_loader:
        images, labels = data[0].to(device), data[1].to(device)
        outputs = net(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
print('Accuracy of the network on the 10000 test images: %d %%' % (100 * correct / total))
# 保存模型
torch.save(net.state_dict(), 'model.pth')
print('Model has been saved!')

# 5.加载模型
net = Net()
net.load_state_dict(torch.load('model.pth'))
print('Model has been loaded!')

# 6.使用模型
# 预测
dataiter = iter(test_loader)
images, labels = next(dataiter)
outputs = net(images)
_, predicted = torch.max(outputs, 1)
print('Predicted: ', ' '.join('%5s' % predicted[j].item() for j in range(4)))

# 7.查看数据    
# 查看数据
import matplotlib.pyplot as plt
import numpy as np
# functions to show an image
def imshow(img):
    img = img/2 + 0.5     # unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()

imshow(torchvision.utils.make_grid(images))
# print labels
print(' '.join('%5s' % labels[j].item() for j in range(4)))
