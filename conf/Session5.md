# Responsible AI Team and Gemma

## Core Philosophy
- **AI for All**: Developing AI that benefits everyone.

## Gemini Open Model
- **Diversity in Extensions/Operations**: Gemini offers various extensions and operational capabilities.
- **Framework Compatibility**: Compatible with multiple frameworks such as Torch, Jax, and AS.
- **Project Collaboration**: Reach out to the team for project collaborations using Gemma.

## Key Gemma Models
### Pali Gemma
- **Vision to Text Model**: Handles captioning, segmentation, and detection.
- **Parameters**: 2B parameters, allows fine-tuning.
- **Image Resolutions**: Supports 224 / 448 resolutions.

### Gemma 2
- **Resources**:
  - [AI Studio](https://aistudio.google.com)
  - [Gemma Cookbook on GitHub](https://github.com/google-gemini/Gemma-cookbook)
  - [Gemma Documentation](https://ai.google.dev/gemma)

## Gemma Fine-Tuning
- **LoRA (Low-Rank Adaptation)**: Lightweight fine-tuning tool.
- **Offline Usage**: Can be fully downloaded and used offline.
- **Keras Integration**: Easy to import and use with Keras.

### Example Usage
```python
import keras
from gemma import Gemma

gemma = Gemma()
result = gemma.generate("Prompt text here", max_length=32)
print(result)

```
# Real Time Translation Ex
```python
def build(name: str, lang_source: str, lang_target: str, text: str) -> str:
    return f"""translate from {lang_source} to {lang_target}. Output only the translation.
<{lang_source}>
{text}
</{lang_source}>
<{lang_target}>"""

def translate(text: str, lang_src: str, lang_tar: str, **kwargs) -> str:
    prompt = build("translate", lang_src, lang_tar, text)
    output = gemma.generate(prompt, **kwargs)
    output = output[len(prompt):].split('</')[0]
    return output.strip()

# Example usage
translated_text = translate('Hello, world!', 'English', 'Korean', max_length=64)
print(translated_text)
```
# Paligemma Integration
``` python
import keras_nlp.models.paligemmaCasualLM as paligemma
import tensorflow as tf

# Load model
paligemma_model = paligemma.from_preset('./paligemma')
paligemma_model.summary()

# Process image
img = tf.io.read_file('photo.jpeg')
img = tf.io.decode_image(img)
img = tf.image.resize(img, (224, 224))

# Generate output
output = paligemma_model.generate({'images': img, 'prompts': 'ocr'})
print(output)
```

## Transparency and Robust Evaluation

	•	RAI Guidance: Following responsible AI guidelines.
	•	Model Debugging: Utilizing linting tools.
	•	Safety Classifiers: State-of-the-art text classification for bespoke text.
	•	LLM Comparator: Facilitates model fine-tuning and comparison (see LLM Comparator).

## Subsections for Instructions

	•	Detailed instructions for using various aspects of the Gemma framework are provided to ensure comprehensive understanding and ease of use.


--------------
-----
----
----
# 원문
Last Session 

Responsible AI team

Gemma 

- AI 는 모두를 위해 개발되어야 한다….

- 

- Gemini 의 오픈 모델

- extend / operation 의 다양성을 제공하는중. 

- 호환 되는 다수의 framework 존재 torch, Jax , AS, etc., 

- gemma 써서 프로젝트 만들때, 그냥 연락 해봐라 재미나겠다. 라는데

- Gemma/ CodeGemma/ Gemma

Pali Gemma : Vision to Text model

Captioning, 2B param, -> allowing fine-tuning

Segmentation, detection, captioning

224 / 448 사용함

Gemma 2 -> 

Aistudio.google.com

github.com/google-gemini/Gemma-cookbook

ai.google.dev/gemma


Gemma finetuning ->

	enable_lora <- what is low length … <- fine tuning tools

	very light weight
	
	다운로드 받아서 사용하면 됨
	gemma 완벽하게 offline 상황에서 돌아감

	import 는 keras 활용하면 쉬움
	
	사용법은 gemma = ~~ 하고 불러오고
	
	gemma.generate (“ㅇ너마ㅣㅓㅏㅣ” max_legnth=32)


	semi real time translator 로 동작 할 수 있다.

	
Def build (name: str, … ) -> str: <- 이거 아웃풋이 str 인거로 됨 ㄹㅈㄷ
	return f”””translate from {lang_source} to {lang_target}. Output only the translation.
<{lang_src}>
{text}
</{lang_src}>
<{lang_tar}>”””

print(buld(…))

Prompt = build(…..)
Gemma.generate(prompt, max_length=64)

하면 프롬프트 값으로 나와서 프롬프트 엔지니어링에 쓸 수 있음

Def translate(text” str, lang_src: str, lang_tar:str, **kwargs)-> str:
	prompt = build(…)
	output = gemma.generate(prompt, **kwargs)
	output = output[len(prompt):]
	output = output.split(‘</‘)[0]
	return output

Translate (‘jkasldjaskl’, English, Korean, max_len=64)
‘’’
->  OUTPUT TEXT (kor)


Def translate(text” str, lang_src: str, lang_tar:str, **kwargs)-> str:
	prompt = build(…)
	output = gemma.generate(prompt, **kwargs)
	output = output[len(prompt):]
	output = output.split(‘</‘)[0]
	return output.strip()

Translate (‘OUTPUT TEXT’, Korean, English, max_len=64)
‘’’
->  OUTPUT TEXT (eng)


Paligemma = keras_nlp.models.paligemmaCasualLM.from_preset(‘./paligemma’)


paligemma.summay()

Import tensor flow as tf

Img = tf.io.read_file(‘photo.jpeg’)
Img = tf.io.decode_image(img)
Img = tf. image.resize(img, (224, 224))


Output = paligemma.generat({‘images’: img, ‘prompts’: ‘ocr’}) <- see detail for paligemma details

Gemma can be used as semi realtime because it is very small and light model


Transparent and robust evaluation

- RAI guidance
- Model Debugging -> Lint using -> 
- Safety Classifiers -> code lab there -> text classification SOTA -> but in bespoke text 
- LLM Comparator -> fine tune the model and, comparison is easier pair-code.github.io/llm-comparator 


Subsections for instructions







