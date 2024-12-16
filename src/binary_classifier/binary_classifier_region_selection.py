import torch
import torch.nn as nn

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


class BinaryClassifierRegionSelection(nn.Module):
    def __init__(self):
        super().__init__()

        self.classifier = nn.Sequential(
            nn.Linear(in_features=1024, out_features=512),
            nn.ReLU(),
            nn.Linear(in_features=512, out_features=128),
            nn.ReLU(),
            nn.Linear(in_features=128, out_features=1)
        )

        pos_weight = torch.tensor([2.2], device=device)
        self.loss_fn = nn.BCEWithLogitsLoss(pos_weight=pos_weight)

    def forward(
        self,
        top_region_features,  # tensor of shape [batch_size x 29 x 1024]
        class_detected,  # boolean tensor of shape [batch_size x 29], indicates if the object detector has detected the region/class or not
        return_loss,  # boolean value that is True if we need the loss (necessary for training and evaluation)
        region_has_sentence=None  # boolean tensor of shape [batch_size x 29], indicates if a region has a sentence (True) or not (False) as the ground truth
    ):
        # logits of shape [batch_size x 29]
        logits = self.classifier(top_region_features).squeeze(dim=-1)

        # the loss is needed for training and evaluation
        if return_loss:
            # only compute loss for logits that correspond to a class that was detected
            detected_logits = logits[class_detected]
            detected_region_has_sentence = region_has_sentence[class_detected]

            loss = self.loss_fn(detected_logits, detected_region_has_sentence.type(torch.float32))

        if self.training:
            return loss
        else:
            selected_regions = logits > -1
            selected_regions[~class_detected] = False

            selected_region_features = top_region_features[selected_regions]

            # if in eval mode
            if return_loss:
                return loss, selected_regions, selected_region_features
            else:
                # if in inference mode
                return selected_regions, selected_region_features
