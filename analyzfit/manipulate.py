"""Tools for data minipulation."""
import numpy as np

def residual(y,pred):
    """Finds the residual of the actual vs the predicted values.

    Args:
        y (numpy array): An array containing the correct values of the model.
        pred (numpy array): An array containing the predicted values of the model.

    Returns:
        residaul (numpy array): The residual of the data (y-pred).

    Raises:
        ValueError: Raises a value error if y and pred don't have the same number of elements.
    """
    if not isinstance(y, np.ndarray):
        y = np.array(y)
        
    if not isinstance(pred, np.ndarray):
        y = np.array(pred)

    if len(y)!=len(pred):
        raise ValueError("Both y and pred must have the same number of elements.")

    return y-pred

def std_residuals(y,pred):
    """Finds the residual of the actual vs the predicted values.

    Args:
        y (numpy array): An array containing the correct values of the model.
        pred (numpy array): An array containing the predicted values of the model.

    Returns:
        standardized_residaul (numpy array): The standardazied residual of the data (y-pred).
    """

    res = residual(y,pred)
    std = np.std(res)

    return res/std
    
def cooks_dist(y,pred,features):
    """Finds the Cooks distance for the data in the. See:
    https://en.wikipedia.org/wiki/Cook%27s_distance

    Args:
        y (numpy array): An array containing the correct values of the model.
        pred (numpy array): An array containing the predicted values of the model.
        features (numpy ndarray): An array containing the features of the regression model.

    Returns:
        dist (numpy array): An array of the cooks distance for each point in the input data.
    """

    e = residual(y,pred)
    H = hat_diags(features)
    s_sq = np.dot(np.transpose(e),e)/(len(y)-len(features[0]))

    Dist = (H/(1-H)**2)*(e**2)/(s_sq*len(features[0]))
    
    return Dist

def _hat_matrix(X):
    """Finds the hat matrix for of the features in X.

    Args:
        X (numpy ndarray): An array containing the features of the regression model.
    
    Returns:
        H (numpy ndarray): The hat matrix for the regression model.
    """
    return np.dot(X,np.dot(np.linalg.inv(np.dot(np.transpose(X),X)),np.transpose(X)))
    
def hat_diags(X):
    """Finds the diagonals of the hat matrix for the features in X.

    Args:
        X (numpy ndarray): An array containing the features of the regression model.

    Returns:
        hat_diags (numpy array): The diagonals of the hat matrix.
    """

    hat = _hat_matrix(X)

    hat_diags = np.diagonal(hat)

    return hat_diags
