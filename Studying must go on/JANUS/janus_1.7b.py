import torch
from transformers import AutoModelForCausalLM
from janus.models import MultiModalityCausalLM, VLChatProcessor
from janus.utils.io import load_pil_images

# 1) 모델 경로 지정
model_path = "deepseek-ai/Janus-1.3B"

# 2) MPS 사용 가능 여부 확인
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
print(f"Using device: {device}")

# 3) VLChatProcessor 로드
vl_chat_processor = VLChatProcessor.from_pretrained(model_path)
tokenizer = vl_chat_processor.tokenizer

# 4) 모델 로드
print("Loading model...")
vl_gpt: MultiModalityCausalLM = AutoModelForCausalLM.from_pretrained(
    model_path,
    trust_remote_code=True,
    use_flash_attention_2=False,
)

# bfloat16 대신 float16(half) 또는 float32 사용
# float16에서 문제가 있다면 float32로 시도하세요.
vl_gpt = vl_gpt.to(torch.bfloat16).to(device).eval()
print("Model loaded!")

# 5) 대화 내용 준비
conversation = [
    {
        "role": "User",
        "content": "<image_placeholder>\nConvert the formula into latex code.",
        "images": ["images/equation.png"],  # 실제 경로가 유효해야 합니다.
    },
    {"role": "Assistant", "content": ""},
]

# 6) 이미지 로드 및 입력 준비
pil_images = load_pil_images(conversation)
prepare_inputs = vl_chat_processor(
    conversations=conversation,
    images=pil_images,
    force_batchify=True
).to(device)

# 7) 이미지 임베딩 준비
inputs_embeds = vl_gpt.prepare_inputs_embeds(**prepare_inputs)

# 8) 텍스트 생성
outputs = vl_gpt.language_model.generate(
    inputs_embeds=inputs_embeds,
    attention_mask=prepare_inputs.attention_mask,
    pad_token_id=tokenizer.eos_token_id,
    bos_token_id=tokenizer.bos_token_id,
    eos_token_id=tokenizer.eos_token_id,
    max_new_tokens=512,
    do_sample=False,
    use_cache=True,
)

# 9) 결과 디코딩
answer = tokenizer.decode(outputs[0].cpu().tolist(), skip_special_tokens=True)
print(f"{prepare_inputs['sft_format'][0]}", answer)