# -*- coding: utf-8 -*-
# Copyright 2024 Ant Group Co., Ltd.
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

from .base_infer import Infer
from .hf_infer import HFTxt2TxtInfer, HFTxt2ImgInfer, VLLMTxt2TxtInfer
from .api_infer import (
    AnthropicTxt2TxtInfer,
    BaichuanTxt2TxtInfer,
    CohereTxt2TxtInfer,
    MidJourneyTxt2ImgInfer,
    MoonshotTxt2TxtInfer,
    OpenAITxt2TxtInfer,
    OpenAITxt2ImgInfer,
    StabilityAITxt2ImgInfer,
    TongyiQwenTxt2TxtInfer,
)
