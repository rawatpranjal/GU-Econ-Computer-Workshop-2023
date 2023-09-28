import torch
import time

# Generate a larger dataset
X = torch.randn(100000, 2)  # Larger dataset
y = torch.randn(100000, 1)

# Move the data to the GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)
X = X.to(device)
y = y.to(device)

# Define a larger model
model = torch.nn.Sequential(
    torch.nn.Linear(2, 64),  # Larger model with more hidden units
    torch.nn.ReLU(),
    torch.nn.Linear(64, 1)
).to(device)

# Training loop with CUDA (GPU)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
start_time = time.time()
for epoch in range(100):
    predictions = model(X)
    loss = torch.nn.functional.mse_loss(predictions, y)
    loss.backward()
    optimizer.step()
end_time = time.time()
print("Training time with CUDA (GPU): {:.4f} seconds".format(end_time - start_time))

# Move the model and data back to CPU
model = model.to("cpu")
X = X.to("cpu")
y = y.to("cpu")

# Training loop without CUDA (CPU)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
start_time = time.time()
for epoch in range(100):
    predictions = model(X)
    loss = torch.nn.functional.mse_loss(predictions, y)
    loss.backward()
    optimizer.step()
end_time = time.time()
print("Training time without CUDA (CPU): {:.4f} seconds".format(end_time - start_time))
