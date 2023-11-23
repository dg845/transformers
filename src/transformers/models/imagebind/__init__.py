# Copyright 2023 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import TYPE_CHECKING

from ...utils import (
    OptionalDependencyNotAvailable,
    _LazyModule,
    is_speech_available,
    is_tokenizers_available,
    is_torch_available,
    is_vision_available,
)


_import_structure = {
    "configuration_imagebind": [
        "IMAGEBIND_PRETRAINED_CONFIG_ARCHIVE_MAP",
        "ImageBindAudioConfig",
        "ImageBindConfig",
        "ImageBindDepthConfig",
        "ImageBindImuConfig",
        "ImageBindOnnxConfig",
        "ImageBindTextConfig",
        "ImageBindThermalConfig",
        "ImageBindVisionConfig",
    ],
    "feature_extraction_imagebind": ["ImageBindImuFeatureExtractor"],
    "processing_imagebind": ["ImageBindProcessor"],
    "tokenization_imagebind": ["ImageBindTokenizer"],
}

# TODO: add dependencies for other modalities, if necessary

try:
    if not is_tokenizers_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["tokenization_imagebind_fast"] = ["ImageBindTokenizerFast"]

try:
    if not is_vision_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["feature_extraction_imagebind"].extend(["ImageBindFeatureExtractor"])
    _import_structure["image_processing_imagebind"] = ["ImageBindImageProcessor", "ImageBindDepthImageProcessor", "ImageBindThermalImageProcessor"]

try:
    if not is_speech_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["feature_extraction_imagebind"].extend(["ImageBindAudioFeatureExtractor"])


try:
    if not is_torch_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["modeling_imagebind"] = [
        "IMAGEBIND_PRETRAINED_MODEL_ARCHIVE_LIST",
        "ImageBindAudioModel",
        "ImageBindAudioModelWithProjection",
        "ImageBindDepthModel",
        "ImageBindDepthModelWithProjection",
        "ImageBindImuModel",
        "ImageBindImuModelWithProjection",
        "ImageBindModel",
        "ImageBindPreTrainedModel",
        "ImageBindTextModel",
        "ImageBindTextModelWithProjection",
        "ImageBindThermalModel",
        "ImageBindThermalModelWithProjection",
        "ImageBindVisionModel",
        "ImageBindVisionModelWithProjection",
    ]

if TYPE_CHECKING:
    from .configuration_imagebind import (
        IMAGEBIND_PRETRAINED_CONFIG_ARCHIVE_MAP,
        ImageBindAudioConfig,
        ImageBindConfig,
        ImageBindDepthConfig,
        ImageBindImuConfig,
        ImageBindOnnxConfig,
        ImageBindTextConfig,
        ImageBindThermalConfig,
        ImageBindVisionConfig,
    )
    from .feature_extraction_imagebind import ImageBindImuFeatureExtractor
    from .processing_imagebind import ImageBindProcessor
    from .tokenization_imagebind import ImageBindTokenizer

    try:
        if not is_tokenizers_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .tokenization_imagebind_fast import ImageBindTokenizerFast

    try:
        if not is_vision_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .feature_extraction_imagebind import ImageBindFeatureExtractor
        from .image_processing_imagebind import ImageBindImageProcessor, ImageBindDepthImageProcessor, ImageBindThermalImageProcessor

    try:
        if not is_speech_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .feature_extraction_imagebind import ImageBindAudioFeatureExtractor

    try:
        if not is_torch_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .modeling_imagebind import (
            IMAGEBIND_PRETRAINED_MODEL_ARCHIVE_LIST,
            ImageBindAudioModel,
            ImageBindAudioModelWithProjection,
            ImageBindDepthModel,
            ImageBindDepthModelWithProjection,
            ImageBindImuModel,
            ImageBindImuModelWithProjection,
            ImageBindModel,
            ImageBindPreTrainedModel,
            ImageBindTextModel,
            ImageBindTextModelWithProjection,
            ImageBindThermalModel,
            ImageBindThermalModelWithProjection,
            ImageBindVisionModel,
            ImageBindVisionModelWithProjection,
        )

else:
    import sys

    sys.modules[__name__] = _LazyModule(__name__, globals()["__file__"], _import_structure, module_spec=__spec__)