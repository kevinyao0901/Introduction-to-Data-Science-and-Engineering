import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import cv2

# 定义卷积神经网络模型
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(32, 64, 5)
        self.fc1 = nn.Linear(64 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(nn.functional.relu(self.conv1(x)))
        x = self.pool(nn.functional.relu(self.conv2(x)))
        x = x.view(-1, 64 * 5 * 5)
        x = nn.functional.relu(self.fc1(x))
        x = nn.functional.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# 超参数
batch_size = 4
learning_rate = 0.001
num_epochs = 2

# 数据预处理和加载
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
train_dataset = torchvision.datasets.CIFAR10(root='./data', train=True, transform=transform, download=True)
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

# 创建模型和优化器
net = Net()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=learning_rate, momentum=0.9)

# 训练模型
for epoch in range(num_epochs):
    running_loss = 0.0
    for i, data in enumerate(train_loader, 0):
        inputs, labels = data
        optimizer.zero_grad()
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
        if i % 2000 == 1999:  # 每2000批次打印一次
            print(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 2000:.3f}')
            running_loss = 0.0

print('Finished Training')

# 可视化卷积特征
dataiter = iter(train_loader)
images, labels = next(dataiter)  # 使用next()方法获取数据

def visualize_features(image,scale_factor=10.0):
    image = image.unsqueeze(0)
    activations = []
    
    def hook_fn(module, input, output):
        activations.append(output)
    
    hooks = []
    for layer in net.children():
        hook = layer.register_forward_hook(hook_fn)
        hooks.append(hook)

    with torch.no_grad():
        net(image)

    i = 1
    while i < 6:
        resized_image = cv2.resize(activations[i][0, 0].cpu().numpy(), None, fx=scale_factor, fy=scale_factor)
        cv2.imshow(f'Layer {i}', resized_image)
        cv2.waitKey(100000)  # 显示图像1秒钟
        cv2.destroyAllWindows()
        i += 1

# 可视化卷积特征
visualize_features(images[0], scale_factor=10.0)