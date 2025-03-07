import os
import torch
from transformers import pipeline
from datasets import load_dataset
import soundfile as sf
from IPython.display import Audio
from diffusers import DiffusionPipeline, FluxPipeline, DPMSolverMultistepScheduler

DEVICE = "mps"
print("Models are stored in: " + torch.hub.get_dir())

# classifier = pipeline("sentiment-analysis", device=DEVICE)
# result = classifier("Yeah, it's ok.")
# print(result)

# ner = pipeline("ner", grouped_entities=True, device=DEVICE)
# result = ner("Barack Obama was the 44th president of the United States.")
# print(result)

# question_answering = pipeline("question-answering", device=DEVICE)
# result = question_answering(
#     question="Where do I work?",
#     context="My name is Sylvain and I work at Hugging Face in Brooklyn",
# )
# print(result)

# summarizer = pipeline("summarization", device=DEVICE)
# text = "Google is bringing its upgraded note-taking app to its One AI Premium plan. That means subscribers will now gain access to NotebookLM Plus at no added cost, which offers higher usage limits and premium features, like the ability to customize NotebookLM’s responses. Google first launched NotebookLM in 2023, allowing people to use AI to research specific topics and organize notes. The company has since added more interactive features, including a way to dive deeper into YouTube videos as well as transform your research into a podcast with two AI “hosts” that you can also chat with. Google launched the NotebookLM Plus plan for businesses, schools, organizations, and enterprise customers in December. In addition to offering five times more Audio Overviews, notebooks, queries, and sources per notebook, NotebookLM Plus also lets you customize how you share your notebooks and see how many people have viewed them per day. Google currently offers its One AI Premium plan for $19.99 per month with 2TB of storage and access to the company’s Gemini Advanced models, along with Gemini in Workspace apps like Gmail and Docs. Students over the age of 18 in the US can also get the One AI Premium plan for $9.99 per month for one year."
# summary = summarizer(text, max_length=30, min_length=5, do_sample=False)
# print(summary)

# translator = pipeline("translation_en_to_fr", device=DEVICE)
# result = translator("Later on, I'm going to go to the library with my friends; after that we'll all have ice cream. We had ice cream yesterday, but you can never have too much ice cream!")
# print(result)

# classifier = pipeline("zero-shot-classification", device=DEVICE)
# result = classifier(
#     "Getting a new job writing AI systems is a huge change, but a very welcome one.",
#     candidate_labels=["education", "politics", "technology", "business"],
# )
# print(result)

# generator = pipeline("text-generation", device=DEVICE)
# result = generator("In this course, we will teach you how to")
# print(result)

# AUDIO

# synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts", device="cpu") # currently "mps" does not work on my Mac
# embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
# speaker_embeddings = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)
# speech = synthesiser("This is running on my M2 Mac using the 'mps' device which uses Apple Silicon somehow.", forward_params={"speaker_embeddings": speaker_embeddings})
# sf.write("speech.wav", speech["audio"], samplerate=speech["sampling_rate"])
# Audio("speech.wav") # currently silent on my Mac

# VISION

# Runs out of memory on my 8GB Mac (high time for an upgrade!)

# image_gen = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2", torch_dtype=torch.float16, use_safetensors=True, variant="fp16").to(DEVICE)
# image = image_gen("A cartoon of a cheeky monkey in nerdy glasses eating cheese").images[0]
# image.save("monkey_eating_cheese.png")

# And this one won't run at all -- says bitsandbytes compiled without GPU support

# fluxpipe = FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-schnell", torch_dtype=torch.bfloat16).to(DEVICE)
# generator = torch.Generator(device=DEVICE).manual_seed(0)
# prompt="A cartoon of a cheeky monkey in nerdy glasses eating cheese"

# image = fluxpipe(
#     prompt,
#     guidance_scale=0.0,
#     num_inference_steps=4,
#     max_sequence_length=256,
#     generator=generator
# ).images[0]

# image.save("monkey_eating_cheese_flux.png")