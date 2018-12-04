# Disentangling Shape and Appearance

## Outline

Part |  Name|  Pages | Wrote
--------|---|--------|------
1 | Intro | 5 | 1
2 | Basics | 10 | 2
3 | Literature | 20 | 3
4 | Method | 5 | 3
5 | Experiments | 20 | 3
6 | Conclusion | 5 | 0

## Contributions
**Hypothesis** *i)*: learning shape requires abstracting away appearance -> hence disentangling

**Hypothesis** *ii)*: learning disentanglement from data is fundamentally constrained. disentangling without supervision impossible from pure data and without explicit model, need to interact with the world, need to change, need to model physical reality -> image transformations, analyis-by-synthesis

- validate and evaluate method developed by Lorenz \etal\ 2018 for disentangling
- overview over state-of-the-art disentangling, analysis of future directions
- explain method in context to these
- evaluate unsupervised shape learning:
	-	 human faces, bodies (CelebA, Human3.6M)
	- animal faces, bodies (cats, dogs, birds)
	- composite objects (dancing pair)
- make own video dataset
	- for disentangling human pose and appearance (heidelbergpose)
	- for articulated animal video (dogs)
	- for composite object (pair dancing salsa)
- ablation study (reconstruction, equivariance loss, transformations)
- study: effect of image transformations
- qualitative comparison to non-disentangling composite shape learning (Zhang)
- evaluating disentanglement:
	- ReID
	- Pose

**Results**:

- SotA in unsupervised shape learning,
- (first) unsupervised disentangling of articulated shape and appearance

## Library

* Building Machines That Learn and Think Like People (Lake et. al. 2016) [[paper]](https://arxiv.org/abs/1604.00289)

* Theoretical Impediments to Machine Learning With Seven Sparks from the Causal Revolution (Pearl 2018) [[paper]](http://arxiv.org/abs/1801.04016)
