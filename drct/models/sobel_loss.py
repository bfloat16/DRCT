import torch
import torch.nn as nn
import torch.nn.functional as F


class SobelLoss(nn.Module):
    def __init__(self):
        super(SobelLoss, self).__init__()
        sobel_x = torch.tensor([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=torch.float32).unsqueeze(0).unsqueeze(0)
        sobel_y = torch.tensor([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=torch.float32).unsqueeze(0).unsqueeze(0)
        self.register_buffer('sobel_x', sobel_x)
        self.register_buffer('sobel_y', sobel_y)

    def forward(self, y_pred, y_true):
        # y: bchw 0-1 float
        # Convert to grayscale
        p_gray = (y_pred[:, 0] * 0.2989 + y_pred[:, 1] * 0.5870 + y_pred[:, 2] * 0.1140).unsqueeze(1)
        t_gray = (y_true[:, 0] * 0.2989 + y_true[:, 1] * 0.5870 + y_true[:, 2] * 0.1140).unsqueeze(1)

        # Apply Sobel filters
        sobel_p_x = F.conv2d(p_gray, self.sobel_x, padding=1)
        sobel_p_y = F.conv2d(p_gray, self.sobel_y, padding=1)
        sobel_t_x = F.conv2d(t_gray, self.sobel_x, padding=1)
        sobel_t_y = F.conv2d(t_gray, self.sobel_y, padding=1)
        sobel_p = sobel_p_x * 0.5 + sobel_p_y * 0.5
        sobel_t = sobel_t_x * 0.5 + sobel_t_y * 0.5

        sobel_diff = torch.abs(sobel_p - sobel_t)
        item_loss = torch.mean(sobel_diff)
        return item_loss