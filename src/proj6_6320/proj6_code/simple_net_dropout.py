import torch
import torch.nn as nn


class SimpleNetDropout(nn.Module):
  def __init__(self):
    '''
    Init function to define the layers and loss function

    Note: Use 'sum' reduction in the loss_criterion. Read Pytorch documention
    to understand what it means
    '''
    super().__init__()

    self.cnn_layers = nn.Sequential()
    self.fc_layers = nn.Sequential()
    
    self.loss_criterion = None

    ###########################################################################
    # Student code begin
    ###########################################################################
     
    self.cnn_layers = nn.Sequential(
      nn.Conv2d(in_channels=1, out_channels=10, kernel_size=5, stride=1, padding=0), # Conv: 5 x 5 kernel. 1@64x64 -> 10@60x60
      nn.BatchNorm2d(num_features=10),
      nn.MaxPool2d(kernel_size=3, stride=3), # Pool 3 x 3 kernel. 10@60x60 -> 10@20x20
      nn.Dropout(p=0.5),
      nn.ReLU(),
      nn.Conv2d(in_channels=10, out_channels=20, kernel_size=5, stride=1, padding=0), # Conv: 5 x 5 kernel. 10@20x20 -> 20@16x16
      nn.BatchNorm2d(num_features=20),
      nn.MaxPool2d(kernel_size=3, stride=3), # Pool 3 x 3 kernel. 20@16x16 -> 20@5x5
      nn.ReLU()                    
    )
    self.fc_layers = nn.Sequential(
      nn.Flatten(),
      nn.Linear(in_features=500, out_features=200),
      nn.ReLU(),
      nn.Linear(in_features=200, out_features=85),
      nn.ReLU(),
      nn.Linear(in_features=85, out_features=15)
    )
        
    self.loss_criterion = nn.CrossEntropyLoss(reduction='sum')

    ###########################################################################
    # Student code end
    ###########################################################################

  def forward(self, x: torch.tensor) -> torch.tensor:
    '''
    Perform the forward pass with the net

    Args:
    -   x: the input image [Dim: (N,C,H,W)]
    Returns:
    -   y: the output (raw scores) of the net [Dim: (N,15)]
    '''
    model_output = None
    ###########################################################################
    # Student code begin
    ###########################################################################

    cnn_out = self.cnn_layers(x)
    model_output = self.fc_layers(cnn_out)

    ###########################################################################
    # Student code end
    ###########################################################################
    return model_output
