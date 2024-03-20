import torch
from torch import nn
from torchvision.transforms import ToTensor,Lambda
import matplotlib.pyplot as plt
import os
import pandas as pd

class NeuralNetwork(nn.Module):
    def __init__(self,data_len,class_num):
        super().__init__()
        self.flatten = nn.Flatten() # 차원 줄이기
        self.lstm1 = nn.LSTM(input_size=data_len, hidden_size=128) # 첫번째 레이어 input_size = 데이터 길이에 맞춰서, 히든은... 알아서 잘
        self.relu1 = nn.LeakyReLU()
        self.lstm2 = nn.LSTM(input_size=128, hidden_size=64) # 다음 레이어 input_size는 이전 레이어 히든 사이즈로
        self.relu2 = nn.LeakyReLU()
        self.lstm3 = nn.LSTM(input_size=64, hidden_size=class_num) # 마지막 레이어 히든사이즈는 출력이니까 내가 알고싶은 라벨링의 갯수로 설정
        

    def forward(self, x):
        x = self.flatten(x)
        x = x.unsqueeze(0)  # 배치 차원 및 시퀀스 길이 차원을 추가합니다. 내용이 1개만 있을때
        LSTM, _ = self.lstm1(x)
        LSTM = self.relu1(LSTM)
        LSTM, _ = self.lstm2(LSTM)
        LSTM = self.relu2(LSTM)
        LSTM, _ = self.lstm3(LSTM)
        return LSTM.squeeze(0)  # 배치 차원 및 시퀀스 길이 차원을 제거하고 반환합니다.
    
