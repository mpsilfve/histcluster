The purpose of this experiment is to train a model capable of performing classification tasks for synonyms.

# Activating the virtual environment

For the creation of virtual environments (VE) anaconda is used. You can download anaconda via here: 
https://www.anaconda.com/distribution/

After installing anaconda into your system follow the steps bellow to work in a virtual environment.

Creation of the VE:
```
conda create python=3.7 --name nlp
```

Activating the VE:
```
conda activate nlp
```

Installing all the packages from the **requirements.txt** file to the virtual environment:
```
pip install -r requirements.txt
```

# Word embeddings 

This project relies heavily on the pre trained word embeddings that are available here: https://nlp.stanford.edu/projects/glove/. The embeddings are stored in a .txt file and the file should be saved in the **embeddings/** directory. 

# Usage 

The configurations can be adjusted in the **conf.yml** file. 


The main script is the **master.py** script. 

```
python master.py
```

# Overview of the pipeline

The steps in the pipeline are as follows:

**Text preprocesing** -> **Creating the tensors from text** -> **Training the model** -> **Making predictions**
