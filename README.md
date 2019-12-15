# 6.804 Computational Cognitive Science Final Project

## Evaluation

Since CORnet-\* output 1000 classes corresponding to the 1000 ImageNet classes,
whereas the Vehicle Occlusion dataset (source: ) is based on PASCAL3D+, we need
to map the 1000 classes to the corresponding six vehicle in the PASCAL3D+ dataset.

Using the 1000 class indices from ImageNet from https://gist.github.com/yrevar/942d3a0ac09ec9e5eb3a, we set the following mapping from PASCAL3D+ to ImageNet.

TODO: fill this in


## Full Results Table
[Google Spreadsheet](https://docs.google.com/spreadsheets/d/13VjbdYXUjUhV2AyOJgG_51JUfOKifh1TPOIDbGhOyrc/edit?usp=sharing)

## References

Original extreme occlusion paper:
* Robustness of Object Recognition under Extreme Occlusion in Humans and Computational Models
* https://arxiv.org/pdf/1905.04598.pdf

Importance of recurrence in occluded object recognition:
* Beyond core object recognition: Recurrent processes account for object recognition under occlusion.
* https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007001
