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
# Autogenerated From : scripts/builtin/img_shear.dml

from typing import Dict, Iterable

from systemds.operator import OperationNode, Matrix, Frame, List, MultiReturn, Scalar
from systemds.script_building.dag import OutputType
from systemds.utils.consts import VALID_INPUT_TYPES

def img_shear(img_in: OperationNode, shear_x: float, shear_y: float, fill_value: float):
    """
    :param img_in: Input image as 2D matrix with top left corner at [1, 1]
    :param shear_x: Shearing factor for horizontal shearing
    :param shear_y: Shearing factor for vertical shearing
    :param fill_value: The background color revealed by the shearing
    :return: 'OperationNode' containing output image as 2d matrix with top left corner at [1, 1] 
    """
    params_dict = {'img_in':img_in, 'shear_x':shear_x, 'shear_y':shear_y, 'fill_value':fill_value}
    return Matrix(img_in.sds_context,
		'img_shear',
		named_input_nodes=params_dict)


    