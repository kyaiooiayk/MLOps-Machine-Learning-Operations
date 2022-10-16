# Model Serialisaiton
***

## What is model serialisation?
Serialisation is the process of translating a data structure or object state into a format that can be stored (for example, in a file or memory data buffer) or transmitted (for example, over a computer network) and reconstructed later (possibly in a different computer environment). In other words, serializing is a way to write a python object on the disk that can be transferred anywhere and later de-serialized (read) back by a python script.
***

## Available formats
- **Sklearn** recommends using the `joblib` package
- **Pytorch**'s load and save methods use python’s built-in `pickle` module, 
- **Keras** supports exporting in `hdf5` format. 
- There is also an alternative serialization package `dill` which generalizes pickle at the cost of performance.
***

## Guidelines
- Here are some guidelines for serialization.
  - Use `pickle` to serialize objects with an importable hierarchy.
  - Use `joblib` for objects which contain lots of data in numpy arrays
  - Use `dill` when pickle or joblib won’t work, or when you have custom functions that need to be serialized as part of the model. In general, dill will provide the most flexibility in terms of getting the model serialized and should be considered the path of least resistance when it comes to serializing ML models for production.
***

## Tutorials
- [How to save your Keras model.ipynb](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/blob/master/tutorials/Model_Serialisation/tutorials/GitHub_MD_rendering/How%20to%20save%20your%20Keras%20model.ipynb)
- [How to save your model with ONNX](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/blob/master/tutorials/Model_Serialisation/tutorials/GitHub_MD_rendering/How%20to%20save%20your%20model%20with%20ONNX.ipynb)
- [Model serialisation with dill](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/blob/master/tutorials/Model_Serialisation/tutorials/GitHub_MD_rendering/Model%20serialisation%20with%20dill.ipynb)
- [Save and load ML models](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/blob/master/tutorials/Model_Serialisation/tutorials/GitHub_MD_rendering/Save%20and%20load%20ML%20models.ipynb)
***

## References
- [Machine Learning Model Serialization](https://flynn.gg/blog/machine-learning-model-serialization/)
- [Serialization Wiki](https://en.wikipedia.org/wiki/Serialization)
- [How to easily deploy machine learning models using flask](https://towardsdatascience.com/how-to-easily-deploy-machine-learning-models-using-flask-b95af8fe34d4) 
