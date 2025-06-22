import torch

def save():

def trainnetwork(table):
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
    model = chargenet()
    lossfn = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr = 0.0005)
    
    history = extract.gettable(r"C:\Windows\System32\battery-report.html")

    X = torch.from_numpy(history.drop("SOURCE", axis = 1).astype("float32").values)
    Y = torch.from_numpy(history["SOURCE"].astype("int64").values)
