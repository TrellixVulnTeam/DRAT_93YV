from scipy.stats import pearsonr, kendalltau
a = [ 0.12128739493459102, 0.08102652289396785, 0.0966451095210617, 0.06436231017687573, 0.0643510059074385, 0.054309384405308504, 0.07362902118574298, 0.07119558221951146, 0.08728150356695365, 0.10254903788275156, 0.06996882200217606, 0.06965315862402971, 0.06637234844646515, 0.05683645335525334, 0.04457036705471457, 0.05803981477187338]



b = [0.10955334420938145, 0.05135686822016755, 0.1166896807409743, 0.05209782443461531, 0.07748514911394734, 0.06448937460508182, 0.08017284452788533, 0.06109377002140316, 0.0781966847657254, 0.09085348206997652, 0.10422108462462876, 0.06569576396194282, 0.0729815504946879, 0.06749843217006264, 0.07494602640608797, 0.06614053236963209
     ]


print(pearsonr(a, b))
print(kendalltau(a, b))
import torch
data = torch.tensor([0.4])
print(torch.sigmoid(data))
