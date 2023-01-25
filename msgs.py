
cvs = ["7","vision","7 - computervision","computervision","cv"]
cv_menu ="""
- definition : what is computer vision\n
- work : computer vision work\n
- examples : Computer vision examples\n
- opencv : cv2
"""

w_cv = """
Computer vision is a field of artificial intelligence (AI) that enables computers and systems to derive meaningful information from digital images, videos and other visual inputs — and take actions or make recommendations based on that information. If AI enables computers to think, computer vision enables them to see, observe and understand.

Computer vision works much the same as human vision, except humans have a head start. Human sight has the advantage of lifetimes of context to train how to tell objects apart, how far away they are, whether they are moving and whether there is something wrong in an image.

Computer vision trains machines to perform these functions, but it has to do it in much less time with cameras, data and algorithms rather than retinas, optic nerves and a visual cortex. Because a system trained to inspect products or watch a production asset can analyze thousands of products or processes a minute, noticing imperceptible defects or issues, it can quickly surpass human capabilities.

Computer vision is used in industries ranging from energy and utilities to manufacturing and automotive – and the market is continuing to grow. It reached USD 48.6 billion by 2022.
"""
cv_w= """
Computer vision needs lots of data. It runs analyses of data over and over until it discerns distinctions and ultimately recognize images. For example, to train a computer to recognize automobile tires, it needs to be fed vast quantities of tire images and tire-related items to learn the differences and recognize a tire, especially one with no defects.

Two essential technologies are used to accomplish this: a type of machine learning called deep learning and a convolutional neural network (CNN).

Machine learning uses algorithmic models that enable a computer to teach itself about the context of visual data. If enough data is fed through the model, the computer will “look” at the data and teach itself to tell one image from another. Algorithms enable the machine to learn by itself, rather than someone programming it to recognize an image.

A CNN helps a machine learning or deep learning model “look” by breaking images down into pixels that are given tags or labels. It uses the labels to perform convolutions (a mathematical operation on two functions to produce a third function) and makes predictions about what it is “seeing.” The neural network runs convolutions and checks the accuracy of its predictions in a series of iterations until the predictions start to come true. It is then recognizing or seeing images in a way similar to humans.

Much like a human making out an image at a distance, a CNN first discerns hard edges and simple shapes, then fills in information as it runs iterations of its predictions. A CNN is used to understand single images. A recurrent neural network (RNN) is used in a similar way for video applications to help computers understand how pictures in a series of frames are related to one another.
"""
exmp = """
Here are a few examples of established computer vision tasks:

- Image classification sees an image and can classify it (a dog, an apple, a person’s face). More precisely, it is able to accurately predict that a given image belongs to a certain class. For example, a social media company might want to use it to automatically identify and segregate objectionable images uploaded by users.
- Object detection can use image classification to identify a certain class of image and then detect and tabulate their appearance in an image or video. Examples include detecting damages on an assembly line or identifying machinery that requires maintenance.
- Object tracking follows or tracks an object once it is detected. This task is often executed with images captured in sequence or real-time video feeds. Autonomous vehicles, for example, need to not only classify and detect objects such as pedestrians, other cars and road infrastructure, they need to track them in motion to avoid collisions and obey traffic laws.(7)
- Content-based image retrieval uses computer vision to browse, search and retrieve images from large data stores, based on the content of the images rather than metadata tags associated with them. This task can incorporate automatic image annotation that replaces manual image tagging. These tasks can be used for digital asset management systems and can increase the accuracy of search and retrieval.
"""

ocv = """
OpenCV stands for Open-Source Computer Vision (Library). It is the most common and popularly used, well-documented Computer Vision library. OpenCV is an open-source library that incorporates numerous computer vision algorithms. OpenCV increases computational efficiency and assists with real-time applications. One of the major goals of OpenCV is to provide an accessible and easy-to-use computer vision infrastructure that helps people build sophisticated computer vision applications quickly.
"""

me = """
to see a real exempl, i'm built-in by a computer vision algorithm with opencv and mediapipe libraries, i have a fonctionality of finding hands in images, so, you can send me pictures, that contain hands, and i will detecte them by drawing landmarks.
go ahead!
"""

hi = ["hello","hi","hey","salut","salam","bonjour"]

info = ["infos","1","info","1 - infos"]
infos = "In full evolution, the field of artificial intelligence, known as AI, will require in the future many professionals with the technical skills and sufficient knowledge to master the different methods of AI, while being aware of the ethical and symbolic issues that this sector of activity represents. "

subjects = ["subjects","2","subject","2 - Subjects"]
s1="""
algorithms
computer structure
DataBases
Math
Applied mathematics
Python
Operating systems
Frensh
English
Arabic
Entrepreneurship & Economics
    """

ecole = ["kindi","kendi","kendy","kindy","3","al-kindy","3 - al-kindy","ecole","school"]
kindy = """Al-Kindi, is considered one of the greatest Arab "Hellenizing" philosophers, being nicknamed "the philosopher of the Arabs".
Lycée général et technologique Al Kindy is a general charter high school located in hay el matar, Casablanca, Morocco.
location : https://goo.gl/maps/kRD7So8hLmBVk9bx7"""

coor = ["coordinateur","cordinator","coordinator","4 - coordinator","4"]
coordinator = """Mr. Younes Belarabi
LinkedIn: www.linkedin.com/in/younes-belarabi-052ab453/
"""

creators = ["creators","5 - Creators","5","créateurs","creator"]
creator = """Mr. Youness ATIF
LinkedIn: www.linkedin.com/in/ynstf/
"""

hlp = """help ! \n
        1 - Infos       :  Intelligence Artificielle Formation\n
        2 - Subjects    :  Formation Content\n
        3 - Al-Kindy    :  Definition\n
        4 - Coordinator :  Organization\n
        5 - Creators    :  botBrothers\n
        6 - Interviews\n
        7 - cv : computer vision
        """

inters = ["interviews","interview","6 - interviews","inter","6"]
interview1 = """
What is supervised machine learning? 👶

	Supervised learning is a type of machine learning in which our algorithms are trained
using well-labeled training data, and machines predict the output based on that data.
Labeled data indicates that the input data has already been tagged with the
appropriate output. Basically, it is the task of learning a function that maps the input set
and returns an output. Some of its examples are: Linear Regression, Logistic Regression,
KNN, etc.

*************************************************

What is regression? Which models can you use to solve a regression problem? 👶

Regression is a part of supervised ML. Regression models investigate the relationship
between a dependent (target) and independent variable (s) (predictor). Here are some
common regression models.

-Linear Regression establishes a linear relationship between target and predictor (s).
It predicts a numeric value and has a shape of a straight line.
-Polynomial Regression has a regression equation with the power of independent
variable more than 1. It is a curve that fits into the data points.
-Ridge Regression helps when predictors are highly correlated (multicollinearity
problem). It penalizes the squares of regression coefficients but doesn’t allow the
coefficients to reach zeros (uses L2 regularization).
-Lasso Regression penalizes the absolute values of regression coefficients and allows
some of the coefficients to reach absolute zero (thereby allowing feature selection).

*************************************************

What is linear regression? When do we use it? 👶

Linear regression is a model that assumes a linear relationship between the input
variables (X) and the single output variable (y).

With a simple equation:
y = B0 + B1*x1 + ... + Bn * xN

B is regression coefficients, x values are the independent (explanatory) variables and y is
dependent variable.

The case of one explanatory variable is called simple linear regression. For more than
one explanatory variable, the process is called multiple linear regression.

Simple linear regression:
y = B0 + B1*x1

Multiple linear regression:
y = B0 + B1*x1 + ... + Bn * xN

*************************************************

"""
interview2 = """
What are the main assumptions of linear regression? ⭐
There are several assumptions of linear regression. If any of them is violated, model
predictions and interpretation may be worthless or misleading.

1. Linear relationship between features and target variable.

2. Additivity means that the effect of changes in one of the features on the target
variable does not depend on values of other features. For example, a model for
predicting revenue of a company have of two features - the number of items a
sold and the number of items b sold. When company sells more items a the
revenue increases and this is independent of the number of items b sold. But, if
customers who buy a stop buying b, the additivity assumption is violated.

3. Features are not correlated (no collinearity) since it can be difficult to separate out
the individual effects of collinear features on the target variable.

4. Errors are independently and identically normally distributed (y = B0 + B1*x1 + ...+ error ):
	i. No correlation between errors (consecutive errors in the case of time series data).
	ii. Constant variance of errors - homoscedasticity. For example, in case of time series, seasonal patterns can increase errors in seasons with higher activity.
	iii. Errors are normally distributed, otherwise some features will have more influence on the target variable than to others. If the error distribution is significantly non-normal, confidence intervals may be too wide or too narrow.

*************************************************

How do we check if a variable follows the normal distribution? ⭐️

1. Plot a histogram out of the sampled data. If you can fit the bell-shaped "normal"
curve to the histogram, then the hypothesis that the underlying random variable
follows the normal distribution can not be rejected.

2. Check Skewness and Kurtosis of the sampled data. Skewness = 0 and kurtosis = 3
are typical for a normal distribution, so the farther away they are from these values,
the more non-normal the distribution.

3. Use Kolmogorov-Smirnov or/and Shapiro-Wilk tests for normality. They take into
account both Skewness and Kurtosis simultaneously.

4. Check for Quantile-Quantile plot. It is a scatterplot created by plotting two sets of
quantiles against one another. Normal Q-Q plot place the data points in a roughly
straight line.

*************************************************

What if we want to build a model for predicting prices? Are prices distributed normally? Do we need to do any pre-processing for prices? ⭐️

Data is not normal. Specially, real-world datasets or uncleaned datasets always have
certain skewness. Same goes for the price prediction. Price of houses or any other thing
under consideration depends on a number of factors. So, there's a great chance of
presence of some skewed values i.e outliers if we talk in data science terms.
Yes, you may need to do pre-processing. Most probably, you will need to remove the
outliers to make your distribution near-to-normal.

*************************************************"""

interview3 = """

What is gradient descent? How does it work? ⭐️

Gradient descent is an algorithm that uses calculus concept of gradient to try and reach
local or global minima. It works by taking the negative of the gradient in a point of a
given function, and updating that point repeatedly using the calculated negative
gradient, until the algorithm reaches a local or global minimum, which will cause future
iterations of the algorithm to return values that are equal or too close to the current
point. It is widely used in machine learning applications.

*************************************************

What is the normal equation? ⭐️
Normal equations are equations obtained by setting equal to zero the partial
derivatives of the sum of squared errors (least squares); normal equations allow one to
estimate the parameters of a multiple linear regression.

*************************************************

What is SGD stochastic gradient descent? What’s the difference with the usual gradient descent? ⭐

In both gradient descent (GD) and stochastic gradient descent (SGD), you update a set
of parameters in an iterative manner to minimize an error function.
While in GD, you have to run through ALL the samples in your training set to do a
single update for a parameter in a particular iteration, in SGD, on the other hand, you
use ONLY ONE or SUBSET of training sample from your training set to do the update
for a parameter in a particular iteration. If you use SUBSET, it is called Minibatch
Stochastic gradient Descent.

*************************************************

Which metrics for evaluating regression models do you know? 👶

1. Mean Squared Error(MSE)
2. Root Mean Squared Error(RMSE)
3. Mean Absolute Error(MAE)
4. R² or Coefficient of Determination
5. Adjusted R²

*************************************************"""

interview4 = """

What are MSE and RMSE? 👶

MSE stands for Mean Square Error while RMSE stands for Root Mean Square Error.
They are metrics with which we can evaluate models.

*************************************************

What is the bias-variance trade-off? 👶

Bias is the error introduced by approximating the true underlying function, which can
be quite complex, by a simpler model. Variance is a model sensitivity to changes in the
training dataset.

Bias-variance trade-off is a relationship between the expected test error and the
variance and the bias - both contribute to the level of the test error and ideally should
be as small as possible:
ExpectedTestError = Variance + Bias² + IrreducibleError

But as a model complexity increases, the bias decreases and the variance increases
which leads to overfitting. And vice versa, model simplification helps to decrease the
variance but it increases the bias which leads to underfitting.

*************************************************

What is overfitting? 👶
When your model perform very well on your training set but can't generalize the test
set, because it adjusted a lot to the training set.

*************************************************"""
interview5 = """

How to validate your models? 👶
One of the most common approaches is splitting data into train, validation and test
parts. Models are trained on train data, hyperparameters (for example early stopping)
are selected based on the validation data, the final measurement is done on test
dataset. Another approach is cross-validation: split dataset into K folds and each time
train models on training folds and measure the performance on the validation folds.
Also you could combine these approaches: make a test/holdout dataset and do cross-validation on the rest of the data. The final quality is measured on test dataset.

*************************************************

Why do we need to split our data into three parts: train, validation, and test? 👶
The training set is used to fit the model, i.e. to train the model with the data. The
validation set is then used to provide an unbiased evaluation of a model while fine-tuning hyperparameters. This improves the generalization of the model. Finally, a test
data set which the model has never "seen" before should be used for the final
evaluation of the model. This allows for an unbiased evaluation of the model. The
evaluation should never be performed on the same data that is used for training.
Otherwise the model performance would not be representative.

*************************************************

Can you explain how cross-validation works? 👶
Cross-validation is the process to separate your total training set into two subsets:
training and validation set, and evaluate your model to choose the hyperparameters.
But you do this process iteratively, selecting different training and validation set, in
order to reduce the bias that you would have by selecting only one validation set.

*************************************************"""

interview6 = """

What is K-fold cross-validation? 👶
K fold cross validation is a method of cross validation where we select a
hyperparameter k. The dataset is now divided into k parts. Now, we take the 1st part as
validation set and remaining k-1 as training set. Then we take the 2nd part as validation
set and remaining k-1 parts as training set. Like this, each part is used as validation set
once and the remaining k-1 parts are taken together and used as training set. It should
not be used in a time series data.

*************************************************

How do we choose K in K-fold cross-validation? What’s your favorite K? 👶

There are two things to consider while deciding K: the number of models we get and
the size of validation set. We do not want the number of models to be too less, like 2 or
3. At least 4 models give a less biased decision on the metrics. On the other hand, we
would want the dataset to be at least 20-25% of the entire data. So that at least a ratio
of 3:1 between training and validation set is maintained.
I tend to use 4 for small datasets and 5 for large ones as K.

*************************************************

What is classification? Which models would you use to solve a classification
problem? 👶

Classification problems are problems in which our prediction space is discrete, i.e. there
is a finite number of values the output variable can be. Some models which can be used
to solve classification problems are: logistic regression, decision tree, random forests,
multi-layer perceptron, one-vs-all, amongst others.

*************************************************"""

interview7 = """

What is logistic regression? When do we need to use it? 👶

Logistic regression is a Machine Learning algorithm that is used for binary classification.
You should use logistic regression when your Y variable takes only two values, e.g. True
and False, "spam" and "not spam", "churn" and "not churn" and so on. The variable is
said to be a "binary" or "dichotomous".

*************************************************

Is logistic regression a linear model? Why? 👶

Yes, Logistic Regression is considered a generalized linear model because the outcome
always depends on the sum of the inputs and parameters. Or in other words, the
output cannot depend on the product (or quotient, etc.) of its parameters.

*************************************************

What is sigmoid? What does it do? 👶

A sigmoid function is a type of activation function, and more specifically defined as a
squashing function. Squashing functions limit the output to a range between 0 and 1,
making these functions useful in the prediction of probabilities.
Sigmod(x) = 1/(1+e^{-x})

*************************************************"""

interview8 = """

How do we evaluate classification models? 👶

Depending on the classification problem, we can use the following evaluation metrics:
1. Accuracy
2. Precision
3. Recall
4. F1 Score
5. Logistic loss (also known as Cross-entropy loss)
6. Jaccard similarity coefficient score

*************************************************

What is accuracy? 👶

Accuracy is a metric for evaluating classification models. It is calculated by dividing the
number of correct predictions by the number of total predictions.

*************************************************

Is accuracy always a good metric? 👶

Accuracy is not a good performance metric when there is imbalance in the dataset. For
example, in binary classification with 95% of A class and 5% of B class, a constant
prediction of A class would have an accuracy of 95%. In case of imbalance dataset, we
need to choose Precision, recall, or F1 Score depending on the problem we are trying
to solve.

*************************************************

What is the confusion table? What are the cells in this table? 👶

Confusion table (or confusion matrix) shows how many True positives (TP), True
Negative (TN), False Positive (FP) and False Negative (FN) model has made.

-True Positives (TP): When the actual class of the observation is 1 (True) and the prediction is 1 (True)
-True Negative (TN): When the actual class of the observation is 0 (False) and the prediction is 0 (False)
-False Positive (FP): When the actual class of the observation is 0 (False) and the prediction is 1 (True)
-False Negative (FN): When the actual class of the observation is 1 (True) and the prediction is 0 (False)

Most of the performance metrics for classification models are based on the values of the confusion matrix

*************************************************"""
interview9 = """

What are precision, recall, and F1-score? 👶

-Precision and recall are classification evaluation metrics:
-P = TP / (TP + FP) and R = TP / (TP + FN).
-Where TP is true positives, FP is false positives and FN is false negatives
-In both cases the score of 1 is the best: we get no false positives or false negatives and only true positives.
-F1 is a combination of both precision and recall in one score (harmonic mean):
-F1 = 2 * PR / (P + R).
-Max F score is 1 and min is 0, with 1 being the best.

*************************************************

Precision-recall trade-off ⭐️
Tradeoff means increasing one parameter would lead to decreasing of other. Precision-recall tradeoff occur due to increasing one of the parameter(precision or recall) while keeping the model same.
In an ideal scenario where there is a perfectly separable data, both precision and recall
can get maximum value of 1.0. But in most of the practical situations, there is noise in
the dataset and the dataset is not perfectly separable. There might be some points of
positive class closer to the negative class and vice versa. In such cases, shifting the
decision boundary can either increase the precision or recall but not both. Increasing
one parameter leads to decreasing of the other.

*************************************************

What is the ROC curve? When to use it? ⭐️
ROC stands for Receiver Operating Characteristics. The diagrammatic representation
that shows the contrast between true positive rate vs false positive rate. It is used when
we need to predict the probability of the binary outcome.

*************************************************

TO SEE MORE :


"""