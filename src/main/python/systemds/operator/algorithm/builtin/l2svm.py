# -------------------------------------------------------------
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# -------------------------------------------------------------

# Autogenerated By   : src/main/python/generator/generator.py
# Autogenerated From : scripts/builtin/l2svm.dml

from typing import Dict, Iterable

from systemds.operator import OperationNode, Matrix, Frame, List, MultiReturn, Scalar
from systemds.script_building.dag import OutputType
from systemds.utils.consts import VALID_INPUT_TYPES

def l2svm(X: OperationNode, Y: OperationNode, **kwargs: Dict[str, VALID_INPUT_TYPES]):
    """
    :param X: matrix X of feature vectors
    :param Y: matrix Y of class labels have to be a single column
    :param intercept: No Intercept ( If set to TRUE then a constant bias column is added to X)
    :param epsilon: Procedure terminates early if the reduction in objective function value is less than epsilon (tolerance) times the initial objective function value.
    :param lambda: Regularization parameter (lambda) for L2 regularization
    :param maxIterations: Maximum number of conjugate gradient iterations
    :param maxii: -
    :param verbose: Set to true if one wants print statements updating on loss.
    :param columnId: The column Id used if one wants to add a ID to the print statement, Specificly usefull when L2SVM is used in MSVM.
    :return: 'OperationNode' containing model matrix 
    """
    params_dict = {'X':X, 'Y':Y}
    params_dict.update(kwargs)
    return Matrix(X.sds_context,
		'l2svm',
		named_input_nodes=params_dict)


    