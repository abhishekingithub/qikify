import numpy as np

class QFFS(object):
    """Qikify feature selection library. Doesn't do much yet; right now only implements
    correlation coefficient-based feature selection.
    """
    
    def __init__(self):
        pass
        
    def run(self, X, y, n_features=10, intercept=True, method='corrcoef'):
        """Do feature selection on the basis of correlation coefficients.
        
        Parameters
        ----------
        X : numpy array of shape [n_samples,n_features]
            Training data

        y : numpy array of shape [n_samples]
            Target values

        n_features : int, optional
            Number of features to retain

        intercept : bool, optional
            Whether the first column is an all-constant intercept and 
            should be excluded

        method : string, optional
            Determines the feature selection method to use.

        Returns
        -------
        features : The X column indices to retain.

        Notes
        -----
        We typically exclude the first column since it is the intercept
        all-constant column.
        """
        
        if method=='corrcoef':
            if intercept:
                cc, cs = self.computeCorrCoefs(X[:,1:],y)
                return np.concatenate(([0],cs[0:n_features] + 1))
            else:
                cc, cs = self.computeCorrCoefs(X,y)
                return cs[0:n_features]
        else:
            raise 'Method Error: specified feature selection method does not exist.'
           

    def computeCorrCoefs(self, X,y):
        """Returns the correlation coefficients between X and y, 
        along with the arg-sorted indices of ranked most-correlated X-to-y vars.
        """
        cc = np.array([np.corrcoef(X[:,i], y)[0,1] for i in xrange(X.shape[1])])
        return cc, np.argsort(-abs(cc))
                
                
                
                