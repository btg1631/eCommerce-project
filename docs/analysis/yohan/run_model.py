from LSTM_model import NeuralNetwork
import torch
from torch import nn

def run_model(input_data,data_len,class_num):
    
    # 사용 가능 장치 확인
    device = (
        "cuda"
        if torch.cuda.is_available()
        else "mps"
        if torch.backends.mps.is_available()
        else "cpu"
    )

    model = NeuralNetwork(data_len,class_num).to(device)
    print(model)

    X = input_data

    LSTM = model(X)
    pred_probab = nn.Softmax(dim=1)(LSTM)
    y_pred = pred_probab.argmax(1) # 행에서 최대값 찾기
    return y_pred

if __name__ == '__main__':
    class_num = 10
    data_len = 28
    input_data = torch.rand(1, 28, 28) # 여기가 데이터 들어가는 곳

    result = run_model(input_data,data_len,class_num)
    
    print(result)