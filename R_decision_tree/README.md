# Decision Tree

## What is Decision Tree
<img style="margin : 10px auto 10px auto;" src="https://github.com/jackyhuynh/data_science-visualization-ML-DL-AI_notebook/blob/main/R_decision_tree/images/decision_tree.JPG">
- img is retrieved from Truc Huynh

# Summary pf “Outlier Detection: A Survey”, ACM Computing Surveys Vol.41, no. 3. 2009 by V. Chandola, A. Banerjee and V. Kumar
## Research Paper:
Full paper can be found at <a href="https://github.com/jackyhuynh/data_science-visualization-ML-DL-AI_notebook/blob/main/R_decision_tree/Decision_Tree_Paper.pdf">GitHub</a> by Truc Huynh

## Summarize three main outlier detection techniques
#### Supervised outlier detection techniques (2.2.1): 
- Assume the training dataset contains normal and outlier class.
- The normal approach is to build predictive models for both normal and abnormal classes; data will be compared with both models to see where it belongs.
- Pros: techniques can build accurate models.
- Cons: labeled training data might be prohibitively expensive to obtain since it requires a lot of human effort to obtain the labeled training data set.

#### Semi-supervised outlier detection techniques (2.2.2):
- Assume the availability of only one class. 
- The normal approach is to model only the available class and decare any test instance which does not fit this model to belong to the other class. 
- The reason is very hard to obtain all the possible outlying behaviors that can occur in the training dataset. 
- The techniques which model only the normal instances are very popular since they are easy to obtain. Also, normal behavior is easier to construct than abnormal.
- 
#### Unsupervised outlier detection techniques (2.2.3):
- These techniques in this category does not make any assumption about label training, and it focus on making assumption about the data.
- For examples, normal instances are far more frequent than outliers. 
- Thus a frequently occurring pattern is typically considered normal while a rare occurrence is an outlier.
- Unsupervised outlier detection techniques and semi-supervised outlier detection techniques are widely used than supervised outlier detection techniques. 

## Summarize different types of outliers
#### Type I outliers (2.3.1): 
- A data instance is an outlier due to its attribute values which are inconsistent with values taken by normal instances.
- Techniques that detect Type I outliers analyze the relation of an individual instance with respect to rest of the data instances.
#### Type II outliers (2.3.2): 
- These outliers are caused due to the occurrence of an individual data instance in a specific context in the given data.
- Type II outliers are defined with respect to a context. 
- In fact, a data instance may be a Type II outlier in a specific context (fall under some conditions); but its identical data instance (in terms of behavioral attributes) could be considered normal in a different context. 
- Mostly explored in time-series data, and spatial data. For example, a credit card user usually spends $ 20 at a gas station and $ 200 at a jewelry store. If he spends $ 200 at someday, it considers a type II outliers.
#### Type III outliers (2.3.3):
- When a subset of data instances is outlying with respect to the entire data set, it is considered type III outliers. 
- Its instance data is not outlying by itself, but their occurrences is the whole structure is anomalous. For example, normal shopping pattern of a credit card user is that the gas station, the grocery store, and the restaurant. Three of more purchase at a gas station on the same day (at different time or under more conditions) is potential card theft.
- This sequence of transactions is a Type III outlier. Type I outliers may be detected in any type of data. Type II and Type III outliers require the presence of sequential or spatial structure in the data. But the nature of outliers actually required to be detected by a particular outlier detection algorithm is determined by the specific problem formulation. 

## Summarize two strategies for evaluation of outlier detection techniques
#### Detecting outliers in a given data set (15.1):
A labeling type of outlier detection technique is typically evaluated using any of the evaluation techniques from 2-class classification literature. In the following steps:
- First, choose the dataset.
- Second, split the data set into training and test (if invoke training).
- Third, use the training dataset to train the predicted model.
- Fourth, applying the outlier detection techniques to the test dataset to detect the outliers and normal.
- Finally, Use the predicted label compare with the actual labels to construct a confusion matrix.
##### Conclusion: 
here are many evaluation metrics such as precision, recall, accuracy, false positive rate, false negative rate, detection rates, ROC-curve… have been applied in outlier detection literature. In fact, the choice of an evaluation data set depends on what type of data is the outlier detection technique targeted for. The UCI KDD archive contain many benchmark data sets that use to evaluate outlier algorithm. However, most of them are only available for Type I outlier detection techniques; some can be used for Type II; none for type III.

#### Evaluation in the application domain (15.2): 
- Outlier detection is a highly application domain-oriented concept, and there is no techniques can be applied for all possible setting. 
- One approach is to choose a dataset (sample) belong to the target application domain. 
- Evaluation measures the performance of the entire outlier detection setting (including the technique, the features chosen and other related parameters/assumptions). 
- It is also possible that evaluation technique that perform well in subsection, might not perform well in the application domain. But such evaluation is necessary to establish the usefulness of the technique in the target application domain. Challenges are benchmark data sets are not available publicly, and evaluation from application domain perspective is that labeled validation data is often not available at all.
