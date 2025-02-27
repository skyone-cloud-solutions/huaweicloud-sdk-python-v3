# coding: utf-8

from __future__ import absolute_import

# import SisClient
from huaweicloudsdksis.v1.sis_client import SisClient
from huaweicloudsdksis.v1.sis_async_client import SisAsyncClient
# import models into sdk package
from huaweicloudsdksis.v1.model.analysis_info import AnalysisInfo
from huaweicloudsdksis.v1.model.analysis_info_result import AnalysisInfoResult
from huaweicloudsdksis.v1.model.audio_config import AudioConfig
from huaweicloudsdksis.v1.model.collect_transcriber_job_request import CollectTranscriberJobRequest
from huaweicloudsdksis.v1.model.collect_transcriber_job_response import CollectTranscriberJobResponse
from huaweicloudsdksis.v1.model.config import Config
from huaweicloudsdksis.v1.model.create_vocabulary_request import CreateVocabularyRequest
from huaweicloudsdksis.v1.model.create_vocabulary_response import CreateVocabularyResponse
from huaweicloudsdksis.v1.model.custom_result import CustomResult
from huaweicloudsdksis.v1.model.delete_vocabulary_request import DeleteVocabularyRequest
from huaweicloudsdksis.v1.model.delete_vocabulary_response import DeleteVocabularyResponse
from huaweicloudsdksis.v1.model.flash_result import FlashResult
from huaweicloudsdksis.v1.model.flash_score_result import FlashScoreResult
from huaweicloudsdksis.v1.model.fluency import Fluency
from huaweicloudsdksis.v1.model.multi_modal_config import MultiModalConfig
from huaweicloudsdksis.v1.model.phoneme import Phoneme
from huaweicloudsdksis.v1.model.phoneme_fluency import PhonemeFluency
from huaweicloudsdksis.v1.model.phoneme_pronunciation import PhonemePronunciation
from huaweicloudsdksis.v1.model.post_create_vocab_req import PostCreateVocabReq
from huaweicloudsdksis.v1.model.post_custom_tts_req import PostCustomTTSReq
from huaweicloudsdksis.v1.model.post_multi_modal_assessment_req import PostMultiModalAssessmentReq
from huaweicloudsdksis.v1.model.post_short_audio_assessment_req import PostShortAudioAssessmentReq
from huaweicloudsdksis.v1.model.post_short_audio_req import PostShortAudioReq
from huaweicloudsdksis.v1.model.post_transcriber_jobs import PostTranscriberJobs
from huaweicloudsdksis.v1.model.pronunciation import Pronunciation
from huaweicloudsdksis.v1.model.push_transcriber_jobs_request import PushTranscriberJobsRequest
from huaweicloudsdksis.v1.model.push_transcriber_jobs_response import PushTranscriberJobsResponse
from huaweicloudsdksis.v1.model.put_update_vocab_req import PutUpdateVocabReq
from huaweicloudsdksis.v1.model.recognize_flash_asr_request import RecognizeFlashAsrRequest
from huaweicloudsdksis.v1.model.recognize_flash_asr_response import RecognizeFlashAsrResponse
from huaweicloudsdksis.v1.model.recognize_short_audio_request import RecognizeShortAudioRequest
from huaweicloudsdksis.v1.model.recognize_short_audio_response import RecognizeShortAudioResponse
from huaweicloudsdksis.v1.model.result import Result
from huaweicloudsdksis.v1.model.run_audio_assessment_request import RunAudioAssessmentRequest
from huaweicloudsdksis.v1.model.run_audio_assessment_response import RunAudioAssessmentResponse
from huaweicloudsdksis.v1.model.run_multi_modal_assessment_request import RunMultiModalAssessmentRequest
from huaweicloudsdksis.v1.model.run_multi_modal_assessment_response import RunMultiModalAssessmentResponse
from huaweicloudsdksis.v1.model.run_tts_request import RunTtsRequest
from huaweicloudsdksis.v1.model.run_tts_response import RunTtsResponse
from huaweicloudsdksis.v1.model.segment import Segment
from huaweicloudsdksis.v1.model.sentences import Sentences
from huaweicloudsdksis.v1.model.show_vocabularies_params import ShowVocabulariesParams
from huaweicloudsdksis.v1.model.show_vocabularies_request import ShowVocabulariesRequest
from huaweicloudsdksis.v1.model.show_vocabularies_response import ShowVocabulariesResponse
from huaweicloudsdksis.v1.model.show_vocabulary_request import ShowVocabularyRequest
from huaweicloudsdksis.v1.model.show_vocabulary_response import ShowVocabularyResponse
from huaweicloudsdksis.v1.model.transcriber_config import TranscriberConfig
from huaweicloudsdksis.v1.model.transcriber_result import TranscriberResult
from huaweicloudsdksis.v1.model.tts_config import TtsConfig
from huaweicloudsdksis.v1.model.update_vocabulary_request import UpdateVocabularyRequest
from huaweicloudsdksis.v1.model.update_vocabulary_response import UpdateVocabularyResponse
from huaweicloudsdksis.v1.model.vocab_info import VocabInfo
from huaweicloudsdksis.v1.model.word import Word
from huaweicloudsdksis.v1.model.word_fluency import WordFluency
from huaweicloudsdksis.v1.model.word_info import WordInfo
from huaweicloudsdksis.v1.model.word_pronunciation import WordPronunciation

