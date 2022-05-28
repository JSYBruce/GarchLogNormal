# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from customtyping import Float64Array, Int32Array, ArrayLike, ArrayLike1D, Float64Array
from typing import Callable, List, Optional, Sequence, Tuple, Union
from scipy.special import gamma
from numpy import (
    abs,
    array,
    asarray,
    empty,
    exp,
    int64,
    integer,
    isscalar,
    log,
    nan,
    ndarray,
    ones_like,
    pi,
    sign,
    sqrt,
    sum,
)
from scipy.special import comb, gamma, gammainc, gammaincc, gammaln
import numpy as np

class LogNormal():
    """
    t + normal distribution for use with ARCH models

    Parameters
    ----------
    """

    def __init__(
        self) -> None:
        self._name = "LogNormal"
        self.name = "LogNormal"
        self.num_params = 1
    def constraints(self) -> Tuple[Float64Array, Float64Array]:
        return array([[1, 0], [-1, 0], [0, 1], [0, -1]]), array([2.05, -300.0, -1, -1])


    def bounds(self, bas: Float64Array) -> List[Tuple[float, float]]:
        return []

    def loglikelihood(
        self,
        parameters: Union[Sequence[float], ArrayLike1D],
        bas: ArrayLike,
        sigma2: ArrayLike,
        individual: bool = False,
    ) -> Union[float, Float64Array]:
        r"""Computes the log-likelihood of assuming residuals are log-normally
        distributed, conditional on the variance

        Parameters
        ----------
        parameters : ndarray
            The normal likelihood has no shape parameters. Empty since the
            standard normal has no shape parameters.
        bas  : ndarray
            The bas to use in the log-likelihood calculation
        sigma2 : ndarray
            Conditional variances of resids
        individual : bool, optional
            Flag indicating whether to return the vector of individual log
            likelihoods (True) or the sum (False)

        Returns
        -------
        ll : float
            The log-likelihood

        Notes
        -----
        The log-likelihood of a single data point x is

        .. math::

        """
        m = parameters[0]
        
        px = exp(- (log(bas) - m)**2 / 2 / sigma2) / (bas * sqrt(2 * pi * sigma2 ))
        
        lls = log(px)
        if individual:
            return lls
        else:
            return sum(lls)

    def starting_values(self, std_resid: Float64Array) -> Float64Array:
        return empty(0)
    

    