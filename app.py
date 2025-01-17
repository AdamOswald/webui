import os
from subprocess import getoutput

gpu_info = getoutput('nvidia-smi')
if("A10G" in gpu_info):
    os.system(f"pip install -q https://github.com/camenduru/stable-diffusion-webui-colab/releases/download/0.0.15/xformers-0.0.15.dev0+4c06c79.d20221205-cp38-cp38-linux_x86_64.whl")
elif("T4" in gpu_info):
    os.system(f"pip install -q https://github.com/camenduru/stable-diffusion-webui-colab/releases/download/0.0.15/xformers-0.0.15.dev0+1515f77.d20221130-cp38-cp38-linux_x86_64.whl")

os.system(f"git clone -b v1.5 https://github.com/camenduru/stable-diffusion-webui /home/user/app/stable-diffusion-webui")
os.chdir("/home/user/app/stable-diffusion-webui")

# ----------------------------Please duplicate this space and delete this block if you don't want to see the extra header----------------------------
os.system(f"wget -q https://github.com/AdamOswald/webui/raw/main/header_patch.py -O /home/user/app/header_patch.py")
os.system(f"sed -i -e '/demo:/r /home/user/app/header_patch.py' /home/user/app/stable-diffusion-webui/modules/ui.py")
# ---------------------------------------------------------------------------------------------------------------------------------------------------

os.system(f"wget -q https://github.com/AdamOswald/webui/raw/main/env_patch.py -O /home/user/app/env_patch.py")
os.system(f"sed -i -e '/import image_from_url_text/r /home/user/app/env_patch.py' /home/user/app/stable-diffusion-webui/modules/ui.py")

# ------------------------------------------------------------------v1.5-----------------------------------------------------------------------------
os.system(f'''sed -i -e "s/document.getElementsByTagName('gradio-app')\[0\].shadowRoot/!!document.getElementsByTagName('gradio-app')[0].shadowRoot ? document.getElementsByTagName('gradio-app')[0].shadowRoot : document/g" /home/user/app/stable-diffusion-webui/script.js''')
os.system(f"sed -i -e 's/                show_progress=False,/                show_progress=True,/g' /home/user/app/stable-diffusion-webui/modules/ui.py")
os.system(f"sed -i -e 's/shared.demo.launch/shared.demo.queue().launch/g' /home/user/app/stable-diffusion-webui/webui.py")
os.system(f"sed -i -e 's/ outputs=\[/queue=False, &/g' /home/user/app/stable-diffusion-webui/modules/ui.py")
os.system(f"sed -i -e 's/               queue=False,  /                /g' /home/user/app/stable-diffusion-webui/modules/ui.py")
# ---------------------------------------------------------------------------------------------------------------------------------------------------

if "IS_SHARED_UI" in os.environ:
    os.system(f"sed -i -e '/(modelmerger_interface, \"Checkpoint Merger\", \"modelmerger\"),/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
    os.system(f"sed -i -e '/(train_interface, \"Train\", \"ti\"),/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
    os.system(f"sed -i -e '/extensions_interface, \"Extensions\", \"extensions\"/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
    os.system(f"sed -i -e '/settings_interface, \"Settings\", \"settings\"/d' /home/user/app/stable-diffusion-webui/modules/ui.py")

    os.system(f"rm -rfv /home/user/app/stable-diffusion-webui/scripts/")
    
    os.system(f"wget -q https://github.com/AdamOswald/webui/raw/main/shared-config.json -O /home/user/app/shared-config.json")
    os.system(f"wget -q https://github.com/AdamOswald/webui/raw/main/shared-ui-config.json -O /home/user/app/shared-ui-config.json")

    os.system(f"wget -q {os.getenv('MODEL_LINK')} -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/{os.getenv('MODEL_NAME')}")
    os.system(f"wget -q {os.getenv('VAE_LINK')} -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/{os.getenv('VAE_NAME')}")
    os.system(f"wget -q {os.getenv('YAML_LINK')} -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/{os.getenv('YAML_NAME')}")
    
    os.system(f"python launch.py --force-enable-xformers --disable-console-progressbars --enable-console-prompts --ui-config-file /home/user/app/shared-ui-config.json --ui-settings-file /home/user/app/shared-config.json --no-progressbar-hiding --cors-allow-origins huggingface.co,hf.space")
elif "IS_API" in os.environ:
    os.system(f"sed -i -e '/(txt2img_interface, \"txt2img\", \"txt2img\"),/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
    os.system(f"sed -i -e '/(img2img_interface, \"img2img\", \"img2img\"),/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
    os.system(f"sed -i -e '/(extras_interface, \"Extras\", \"extras\"),/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
    os.system(f"sed -i -e '/(pnginfo_interface, \"PNG Info\", \"pnginfo\"),/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
    os.system(f"sed -i -e '/(modelmerger_interface, \"Checkpoint Merger\", \"modelmerger\"),/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
    os.system(f"sed -i -e '/(train_interface, \"Train\", \"ti\"),/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
    os.system(f"sed -i -e '/extensions_interface, \"Extensions\", \"extensions\"/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
    os.system(f"sed -i -e '/settings_interface, \"Settings\", \"settings\"/d' /home/user/app/stable-diffusion-webui/modules/ui.py")

    os.system(f"wget -q {os.getenv('MODEL_LINK')} -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/{os.getenv('MODEL_NAME')}")
    os.system(f"wget -q {os.getenv('VAE_LINK')} -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/{os.getenv('VAE_NAME')}")
    os.system(f"wget -q {os.getenv('YAML_LINK')} -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/{os.getenv('YAML_NAME')}")
    
    os.system(f"python launch.py --force-enable-xformers --disable-console-progressbars --enable-console-prompts --ui-config-file /home/user/app/ui-config.json --ui-settings-file /home/user/app/config.json --no-progressbar-hiding --cors-allow-origins=https://camenduru-unity.hf.space --api")
else:
    os.system(f"sed -i -e '/(train_interface, \"Train\", \"ti\"),/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
    os.system(f"sed -i -e '/extensions_interface, \"Extensions\", \"extensions\"/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
    os.system(f"sed -i -e '/settings_interface, \"Settings\", \"settings\"/d' /home/user/app/stable-diffusion-webui/modules/ui.py")

    # Please duplicate this space and delete # character in front of the custom script you want to use or add here more custom scripts with same structure os.system(f"wget -q https://CUSTOM_SCRIPT_URL -O /home/user/app/stable-diffusion-webui/scripts/CUSTOM_SCRIPT_NAME.py")
    os.system(f"wget -q https://gist.github.com/camenduru/9ec5f8141db9902e375967e93250860f/raw/d0bcf01786f20107c329c03f8968584ee67be12a/run_n_times.py -O /home/user/app/stable-diffusion-webui/scripts/run_n_times.py")
    
    # Please duplicate this space and delete # character in front of the extension you want to use or add here more extensions with same structure os.system(f"git clone https://EXTENSION_GIT_URL /home/user/app/stable-diffusion-webui/extensions/EXTENSION_NAME")
    #os.system(f"git clone https://github.com/camenduru/stable-diffusion-webui-artists-to-study /home/user/app/stable-diffusion-webui/extensions/stable-diffusion-webui-artists-to-study")
    os.system(f"git clone https://github.com/yfszzx/stable-diffusion-webui-images-browser /home/user/app/stable-diffusion-webui/extensions/stable-diffusion-webui-images-browser")
    os.system(f"git clone https://github.com/deforum-art/deforum-for-automatic1111-webui /home/user/app/stable-diffusion-webui/extensions/deforum-for-automatic1111-webui")
    os.system(f"git clone https://github.com/camenduru/stable-diffusion-webui-huggingface /home/user/app/stable-diffusion-webui/extensions/stable-diffusion-webui-huggingface")
    os.system(f"git clone https://github.com/bbc-mc/merge-percentage-visualize /home/user/app/stable-diffusion-webui/extensions/merge-percentage-visualize")
    os.system(f"git clone https://github.com/bbc-mc/sdweb-merge-board /home/user/app/stable-diffusion-webui/extensions/sdweb-merge-board")
    os.system(f"git clone https://github.com/bbc-mc/sdweb-merge-block-weighted-gui /home/user/app/stable-diffusion-webui/extensions/sdweb-merge-block-weighted-gui")
    os.system(f"git clone https://github.com/arenatemp/stable-diffusion-webui-model-toolkit /home/user/app/stable-diffusion-webui/extensions/stable-diffusion-webui-model-toolkit")
    os.system(f"git clone https://github.com/lodimasq/batch-checkpoint-merger /home/user/app/stable-diffusion-webui/extensions/batch-checkpoint-merger")
    os.system(f"git clone https://github.com/eyriewow/merge-models /home/user/app/stable-diffusion-webui/extensions/merge-models")
    os.system(f"git clone https://github.com/OedoSoldier/enhanced-img2img /home/user/app/stable-diffusion-webui/extensions/enhanced-img2img")
    os.system(f"git clone https://github.com/Maurdekye/model-kitchen /home/user/app/stable-diffusion-webui/extensions/model-kitchen")
    os.system(f"git clone https://github.com/hako-mikan/sd-webui-supermerger /home/user/app/stable-diffusion-webui/extensions/sd-webui-supermerger")
    os.system(f"git clone https://github.com/j4ded/sdweb-merge-block-weighted-gui /home/user/app/stable-diffusion-webui/extensions/sdweb-merge-block-weighted-gui-alt")
    os.system(f"git clone https://github.com/kex0/batch-face-swap /home/user/app/stable-diffusion-webui/extensions/batch-face-swap")
    os.system(f"git clone https://github.com/pkuliyi2015/multidiffusion-upscaler-for-automatic1111 /home/user/app/stable-diffusion-webui/extensions/multidiffusion-upscaler-for-automatic1111")
    os.system(f"git clone https://github.com/klimaleksus/stable-diffusion-webui-embedding-merge /home/user/app/stable-diffusion-webui/extensions/stable-diffusion-webui-embedding-merge")
    os.system(f"git clone https://github.com/fropych/mine-diffusion /home/user/app/stable-diffusion-webui/extensions/mine-diffusion")
    os.system(f"git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui-pixelization /home/user/app/stable-diffusion-webui/extensions/stable-diffusion-webui-pixelization")
    os.system(f"git clone https://github.com/Akegarasu/sd-webui-model-converter /home/user/app/stable-diffusion-webui/extensions/sd-webui-model-converter")
    os.system(f"git clone https://github.com/yfszzx/stable-diffusion-webui-inspiration /home/user/app/stable-diffusion-webui/extensions/stable-diffusion-webui-inspiration") 
    os.system(f"git clone https://github.com/toriato/easy-stable-diffusion /home/user/app/stable-diffusion-webui/extensions/easy-stable-diffusion")   
    os.system(f"git clone https://github.com/camenduru/stable-diffusion-webui-converter /home/user/app/stable-diffusion-webui/extensions/stable-diffusion-webui-converter")
    os.system(f"git clone https://github.com/camenduru/batchlinks-webui /home/user/app/stable-diffusion-webui/extensions/batchlinks-webui")
    os.system(f"git clone https://github.com/mix1009/model-keyword /home/user/app/stable-diffusion-webui/extensions/model-keyword")
    os.system(f"git clone https://github.com/klimaleksus/stable-diffusion-webui-conditioning-highres-fix /home/user/app/stable-diffusion-webui/extensions/stable-diffusion-webui-conditioning-highres-fix")
    os.system(f"git clone https://github.com/tkalayci71/embedding-inspector /home/user/app/stable-diffusion-webui/extensions/embedding-inspector")
    os.system(f"git clone https://github.com/CodeExplode/stable-diffusion-webui-embedding-editor /home/user/app/stable-diffusion-webui/extensions/stable-diffusion-webui-embedding-editor")
    os.system(f"git clone https://github.com/Kahsolt/stable-diffusion-webui-sonar /home/user/app/stable-diffusion-webui/extensions/stable-diffusion-webui-sonar")
    
    # Please duplicate this space and delete # character in front of the model you want to use or add here more ckpts with same structure os.system(f"wget -q https://CKPT_URL -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/CKPT_NAME.ckpt")
    #os.system(f"wget -q https://huggingface.co/nitrosocke/Arcane-Diffusion/resolve/main/arcane-diffusion-v3.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/arcane-diffusion-v3.ckpt")
    os.system(f"wget -q https://huggingface.co/DGSpitzer/Cyberpunk-Anime-Diffusion/resolve/main/Cyberpunk-Anime-Diffusion.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/Cyberpunk-Anime-Diffusion.ckpt")
    os.system(f"wget -q https://huggingface.co/prompthero/midjourney-v4-diffusion/resolve/main/mdjrny-v4.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/mdjrny-v4.ckpt")
    #os.system(f"wget -q https://huggingface.co/nitrosocke/mo-di-diffusion/resolve/main/moDi-v1-pruned.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/moDi-v1-pruned.ckpt")
    #os.system(f"wget -q https://huggingface.co/Fictiverse/Stable_Diffusion_PaperCut_Model/resolve/main/PaperCut_v1.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/PaperCut_v1.ckpt")
    #os.system(f"wget -q https://huggingface.co/lilpotat/sa/resolve/main/samdoesarts_style.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/samdoesarts_style.ckpt")
    os.system(f"wget -q https://huggingface.co/hakurei/waifu-diffusion-v1-3/resolve/main/wd-v1-3-float32.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/wd-v1-3-float32.ckpt")
    os.system(f"wget -q https://huggingface.co/CompVis/stable-diffusion-v-1-4-original/resolve/main/sd-v1-4.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/sd-v1-4.ckpt")
    os.system(f"wget -q https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/v1-5-pruned-emaonly.ckpt")
    os.system(f"wget -q https://huggingface.co/runwayml/stable-diffusion-inpainting/resolve/main/sd-v1-5-inpainting.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/sd-v1-5-inpainting.ckpt")
    os.system(f"wget -q https://huggingface.co/Falon/sangonomiya-kokomi/resolve/main/Sangonomiya_Kokomi.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/Sangonomiya_Kokomi.ckpt")
    os.system(f"wget -q https://huggingface.co/katakana/2D-Mix/resolve/main/2D-Mix.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/2D-Mix.ckpt")
    os.system(f"wget -q https://huggingface.co/katakana/Anime-Merged/resolve/main/Anime-Merged.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/Anime-Merged.ckpt")
    os.system(f"wget -q https://huggingface.co/TheRafal/everything-v1/resolve/main/everything-v1-3.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/everything-v1-3.ckpt")
    os.system(f"wget -q https://huggingface.co/Eppinette/Cyberware/resolve/main/cyberware_V3_m_cyberware_token_style_class_word.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/cyberware_V3_m_cyberware_token_style_class_word.ckpt")
    os.system(f"wget -q https://huggingface.co/Eppinette/Cyberware/resolve/main/cyberware_trinart_cyberware_token_style_class_word.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/cyberware_trinart_cyberware_token_style_class_word.ckpt")
    #os.system(f"wget -q https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/v1-5-pruned-emaonly.ckpt")
    #os.system(f"wget -q https://huggingface.co/runwayml/stable-diffusion-inpainting/resolve/main/sd-v1-5-inpainting.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/sd-v1-5-inpainting.ckpt")
    #os.system(f"wget -q https://huggingface.co/Linaqruf/anything-v3.0/resolve/main/Anything-V3.0-pruned.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/Anything-V3.0-pruned.ckpt")
    #os.system(f"wget -q https://huggingface.co/Linaqruf/anything-v3.0/resolve/main/Anything-V3.0.vae.pt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/Anything-V3.0-pruned.vae.pt")
    #os.system(f"wget -q https://huggingface.co/stabilityai/stable-diffusion-2/resolve/main/768-v-ema.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/768-v-ema.ckpt")
    os.system(f"wget -q https://raw.githubusercontent.com/Stability-AI/stablediffusion/main/configs/stable-diffusion/v2-inference-v.yaml -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/768-v-ema.yaml")
    os.system(f"wget -q https://huggingface.co/stabilityai/stable-diffusion-2-1/resolve/main/v2-1_768-ema-pruned.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/v2-1_768-ema-pruned.ckpt")
    os.system(f"wget -q https://raw.githubusercontent.com/Stability-AI/stablediffusion/main/configs/stable-diffusion/v2-inference-v.yaml -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/v2-1_768-ema-pruned.yaml")

    os.system(f"wget -q {os.getenv('MODEL_LINK')} -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/{os.getenv('MODEL_NAME')}")
    os.system(f"wget -q {os.getenv('VAE_LINK')} -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/{os.getenv('VAE_NAME')}")
    os.system(f"wget -q {os.getenv('YAML_LINK')} -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/{os.getenv('YAML_NAME')}")

    os.system(f"python launch.py --force-enable-xformers --ui-config-file /home/user/app/ui-config.json --ui-settings-file /home/user/app/config.json --disable-console-progressbars --enable-console-prompts --no-progressbar-hiding --cors-allow-origins huggingface.co,hf.space --api --skip-torch-cuda-test")
    
