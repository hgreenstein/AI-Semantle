import torch.nn as nn
import torch

class RNN(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, num_hidden_layers):
        super(RNN, self).__init__()
        self.U_same = nn.ModuleList([nn.Linear(hidden_dim, hidden_dim) for i in range(num_hidden_layers)])
        self.U_transition = nn.ModuleList([nn.Linear(hidden_dim, hidden_dim) for i in range(num_hidden_layers)])
        self.V = nn.Linear(hidden_dim, output_dim)
        self.W = nn.Linear(input_dim, hidden_dim)

        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.relu = nn.ReLU()
        self.softmax = nn.LogSoftmax(dim=-1)
        self.loss = nn.L1Loss()
        self.num_hidden_layers = num_hidden_layers

    def compute_loss(self, predicted_vector, correct_vector):
        return self.loss(predicted_vector, correct_vector)
    
    def forward(self, inputs):
      batch_size = inputs.size(0)
      seq_len = inputs.size(1)
      output = torch.zeros(batch_size, self.output_dim)
      all_h = torch.zeros(self.num_hidden_layers, batch_size, self.hidden_dim)

      for i in range(seq_len):
          entry = inputs[:, i]
          h_0 = all_h[0].clone()

          z_1 = self.W(entry) + self.U_same[0](h_0)
          next_h = self.relu(z_1)
          all_h[0] = next_h.clone()

          for j in range(1, self.num_hidden_layers):
              h_ij = all_h[j].clone()
              z_j = self.U_same[j](h_ij) + self.U_transition[j](next_h)

              next_h = self.relu(z_j)
              all_h[j] = next_h.clone()

          y_i = self.V(next_h)
          output = y_i.squeeze()
      return output

    # Taken from CS 4740, Project 2
    def load_model(self, save_path, is_state_dict=False):
      if not is_state_dict:
        saved_model = torch.load(save_path)
        self.load_state_dict(saved_model.state_dict())
      else:
        self.load_state_dict(torch.load(save_path))

    # Taken from CS 4740, Project 2
    def save_model(self, save_path, is_state_dict=False):
      if is_state_dict:
        torch.save(self.state_dict(), save_path)
      else:
        torch.save(self, save_path)