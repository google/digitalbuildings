# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" Type annotations for the configuration scoring tool """

from typing import Dict, List, Tuple, Any
from validate.entity_instance import EntityInstance
from score.constants import FileTypes, DimensionCategories

CloudDeviceId = str
FileType = FileTypes
DeserializedFile = Dict[CloudDeviceId, EntityInstance]
DeserializedFilesDict = Dict[FileType, DeserializedFile]
DimensionName = str
TranslationsDict = Dict[FileType, List[Tuple[str, Any]]]
DimensionCategory = DimensionCategories
