---
title: "Learning"
description: "Brief takes on density functional theory and machine learning."
date: 2023-09-15
tags: [learning, DFT, machine-learning]
layout: layouts/post.njk
eleventyNavigation:
  key: "Learning"
  order: 2
---

[Skip to content](#content)

[Rishi Gurnani's Website](https://rishigurnani.wordpress.com/)

# Learning

*Below are my brief takes on density functional theory and machine learning, accompanied by helpful resources.*

My work leverages computational tools to study porous materials. These tools include **Density Functional Theory (DFT)** and **Machine Learning (ML)**. At a high level, DFT allows us to set up several quantum‐mechanical equations. By solving them, we can learn about the electronic properties of a set of atoms with an accuracy that matches experimental measurements. To learn more about DFT, check out [Rasoul Khaledialidusti](https://www.youtube.com/channel/UCPtZ0t9Fn2cVETnHqJECW2w)’s four-part [series](https://www.youtube.com/playlist?list=PLvZcfmZeLsvrq5kmsBcyFFIozKZR6mJ-s). A great complement to this series is a [set of lectures](https://www.youtube.com/playlist?list=PLT-GNiCGT-NRk1nD8fZqZcn0zuCEJ6E0_) by my PhD advisor, Dr. Ramprasad, on Electronic Structure Theory.

In addition to the electronic properties, we sometimes wish to understand a material’s **phononic properties**—that is, the coordinated movement of its atoms. These are uncovered by obtaining the *Dynamical Matrix*. To learn more, I recommend this easy-to-digest [paper](https://www.neutron-sciences.org/articles/sfn/pdf/2011/01/sfn201112007.pdf) by M.T. Dove. In short, the Dynamical Matrix reveals how displacing one atom affects the forces on the others. (G J Ackland also wrote a nice review of these methods, available [here](https://iopscience.iop.org/article/10.1088/0953-8984/14/11/311/pdf).)

Although DFT is incredibly powerful, it can be slow for systems with many atoms. **Machine Learning (ML)** offers a speedy alternative. An incredible introduction to ML is available in Andrew Ng’s lecture series [here](https://www.youtube.com/watch?v=PPLop4L2eGk&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN). In simple terms, ML is a way to approximate *maps*—that is, a set of relationships between inputs and outputs. For example, consider the relationship between numbers and letters as shown in the diagram below:

![](https://rishigurnani.wordpress.com/wp-content/uploads/2020/08/map.png?w=240)

There are many flavors of ML algorithms, each uniquely using data to approximate the underlying map. Perhaps the most popular is the *neural network*. With just five minutes and a little Python knowledge, you can create your very own neural network using the Keras API. Check out [this tutorial](https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/) for a quick start (remember to set up your environment first). While Keras is easy to get started with, more advanced networks (such as Variational Autoencoders) require a deeper dive. Stanford’s free [lectures](http://web.stanford.edu/class/cs20si/syllabus.html) on TensorFlow are an excellent resource, and you can also view [my lecture](https://www.youtube.com/watch?v=TFWYoZoezrY) on debugging neural networks.

Another ML method I frequently use is *Gaussian Process Regression (GPR)*. A gentle introduction to GPR is available [here](https://towardsdatascience.com/quick-start-to-gaussian-process-regression-36d838810319) (a basic understanding of probability notation helps).

### Share this:

- [Twitter](https://rishigurnani.wordpress.com/learning/?share=twitter "Click to share on Twitter")
- [Facebook](https://rishigurnani.wordpress.com/learning/?share=facebook "Click to share on Facebook")
