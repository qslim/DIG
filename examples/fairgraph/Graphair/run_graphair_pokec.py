import sys
sys.path.append('../../..')
from dig.fairgraph.method import run
from dig.fairgraph.dataset import POKEC, NBA
import torch

# Load the dataset and split
pokec = POKEC(dataset_sample='pokec_z') # you may also choose 'pokec_n'
print(pokec.features.shape)

# # Train and evaluate
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# run_fairgraph = run()
# run_fairgraph.run(device,dataset=pokec,model='Graphair',epochs=2_000,
#             lr=1e-4,weight_decay=1e-5)