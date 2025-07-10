import torch, extract

# create the neural network class to learn the charging patterns
class chargenet(torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.net = torch.nn.Sequential(
                torch.nn.Linear(3, 16),
                torch.nn.ReLU(),
                torch.nn.Linear(16, 8),
                torch.nn.ReLU(),
                torch.nn.Linear(8, 2)
            )
        def forward(self, x):
            return self.net(x)

# save the torch network
def save(path, storeloc = "network.pth"):
    torch.save(trainNetwork(extract.getTable(path)).state_dict(), storeloc)

# load in and return the torch network
def load(accessloc):
    model = chargenet()
    state = torch.load(accessloc, weights_only = False)
    model.load_state_dict(state)
    model.eval()
    return model

# train the torch network using the optimizer and loss function
def trainNetwork(table):
    model = chargenet()
    lossfn = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr = 0.001)
    
    history = extract.getTable(r"C:\Windows\System32\battery-report.html")

    X = torch.from_numpy(history.drop("SOURCE", axis = 1).astype("float32").values)
    Y = torch.from_numpy(history["SOURCE"].astype("int64").values)

    for i in range(5000):
        model.train()
        optimizer.zero_grad()
        pred = model(X)
        loss = lossfn(pred, Y)
        loss.backward()
        optimizer.step()
    
    return model

# function that creates the input tensor that is used for our prediction of charging times
def makeWeeklyInput(charge_pct: float):
    cap = charge_pct / 100.0
    weekdays = torch.tensor([2,3,4,5,6,7,1], dtype=torch.float32) / 7.0
    hours    = torch.arange(24, dtype=torch.float32) * 3600.0 / 86400.0  # seconds/86400
    
    date_grid = weekdays.unsqueeze(1).repeat(1, 24)   # shape (7,24)
    time_grid = hours.unsqueeze(0).repeat(7, 1)       # shape (7,24)
    cap_grid  = torch.full((7,24), cap)               # shape (7,24)
    
    inp = torch.stack([cap_grid, date_grid, time_grid], dim=2)  # (7,24,3)
    return inp.view(-1, 3)  # (168,3)