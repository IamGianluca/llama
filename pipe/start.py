import torch
import transformers
from torch import cuda


device = f"cuda:{cuda.current_device()}" if cuda.is_available() else "cpu"
print(f"Device avialble is on {device}")

model_id = "meta-llama/Llama-2-13b-chat-hf"
bnb_config = transformers.BitsAndBytesConfig(
    bnb_4bit_compute_dtype=torch.bfloat16,
    load_in_4bit=True,
)

model_config = transformers.AutoConfig.from_pretrained(
    model_id,
)

tokenizer = transformers.AutoTokenizer.from_pretrained(
    model_id,
)

model = transformers.AutoModelForCausalLM.from_pretrained(
    model_id,
    trust_remote_code=True,
    config=model_config,
    quantization_config=bnb_config,
    device_map="auto",
)

generate_text = transformers.pipeline(
    model=model,
    tokenizer=tokenizer,
    # device=0,
    # return_full_text=True,
    task="text-generation",
    # temperature=0.0,
    max_new_tokens=100,
    repetition_penalty=1.1,
)
while True:
    prompt = input("Please enter your prompt: ")
    output = generate_text(prompt)[0]["generated_text"]
    print(output)
