from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Project, Skill, ContactMessage
from .forms import ContactForm


def get_projects():
    return [
        {
            'title': 'Seizure Prediction System',
            'description': 'Real-time epilepsy seizure prediction using EEG signals with deep learning. Achieved 94.7% accuracy using CNN-LSTM hybrid architecture on the CHB-MIT scalp EEG dataset.',
            'category': 'dl',
            'category_label': 'Deep Learning',
            'tech_stack': ['Python', 'TensorFlow', 'CNN-LSTM', 'EEG', 'Signal Processing', 'NumPy'],
            'github_url': 'https://github.com/shoyab778',
            'live_url': '',
            'color': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
            'icon': '🧠',
            'is_featured': True,
        },
        {
            'title': 'Fake News Detector',
            'description': 'BERT-based NLP pipeline for misinformation detection with 96.2% F1 score. Fine-tuned on LIAR and FakeNewsNet datasets with attention visualization.',
            'category': 'nlp',
            'category_label': 'NLP',
            'tech_stack': ['Python', 'BERT', 'Transformers', 'HuggingFace', 'PyTorch', 'Flask'],
            'github_url': 'https://github.com/shoyab778',
            'live_url': '',
            'color': 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
            'icon': '📰',
            'is_featured': True,
        },
        {
            'title': 'AI Image Generator',
            'description': 'Stable Diffusion-based text-to-image generation system with custom LoRA fine-tuning. Supports style transfer, inpainting, and upscaling pipelines.',
            'category': 'gen',
            'category_label': 'Generative AI',
            'tech_stack': ['Python', 'Stable Diffusion', 'LoRA', 'CLIP', 'Diffusers', 'Gradio'],
            'github_url': 'https://github.com/shoyab778',
            'live_url': '',
            'color': 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
            'icon': '🎨',
            'is_featured': True,
        },
        {
            'title': 'Real-Time Object Detection',
            'description': 'YOLOv8-based custom object detection for industrial safety monitoring. Trained on 15K+ annotated images with 89ms inference on edge devices.',
            'category': 'cv',
            'category_label': 'Computer Vision',
            'tech_stack': ['Python', 'YOLOv8', 'OpenCV', 'PyTorch', 'Roboflow', 'TensorRT'],
            'github_url': 'https://github.com/shoyab778',
            'live_url': '',
            'color': 'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
            'icon': '👁️',
            'is_featured': True,
        },
        {
            'title': 'Sentiment Analysis API',
            'description': 'Production-grade multilingual sentiment analysis REST API serving 10K+ requests/day. Built with FastAPI, deployed on AWS with auto-scaling.',
            'category': 'nlp',
            'category_label': 'NLP',
            'tech_stack': ['Python', 'FastAPI', 'BERT', 'Docker', 'AWS', 'Redis'],
            'github_url': 'https://github.com/shoyab778',
            'live_url': '',
            'color': 'linear-gradient(135deg, #fa709a 0%, #fee140 100%)',
            'icon': '💬',
            'is_featured': False,
        },
        {
            'title': 'Medical Image Segmentation',
            'description': 'U-Net based semantic segmentation for tumor detection in MRI scans. Dice score of 0.91 on BraTS2023 benchmark, published research paper.',
            'category': 'cv',
            'category_label': 'Computer Vision',
            'tech_stack': ['Python', 'U-Net', 'PyTorch', 'MONAI', 'ITK', 'SimpleITK'],
            'github_url': 'https://github.com/shoyab778',
            'live_url': '',
            'color': 'linear-gradient(135deg, #a18cd1 0%, #fbc2eb 100%)',
            'icon': '🔬',
            'is_featured': False,
        },
    ]


def get_skills():
    return {
        'languages': [
            {'name': 'Python', 'proficiency': 95, 'icon': '🐍'},
            {'name': 'JavaScript', 'proficiency': 75, 'icon': '⚡'},
            {'name': 'SQL', 'proficiency': 80, 'icon': '🗃️'},
            {'name': 'C++', 'proficiency': 65, 'icon': '⚙️'},
            {'name': 'R', 'proficiency': 60, 'icon': '📊'},
        ],
        'aiml': [
            {'name': 'Deep Learning', 'proficiency': 92, 'icon': '🧠'},
            {'name': 'NLP / LLMs', 'proficiency': 90, 'icon': '💬'},
            {'name': 'Computer Vision', 'proficiency': 88, 'icon': '👁️'},
            {'name': 'Reinforcement Learning', 'proficiency': 72, 'icon': '🎮'},
            {'name': 'Generative AI', 'proficiency': 85, 'icon': '🎨'},
        ],
        'frameworks': [
            {'name': 'PyTorch', 'proficiency': 90, 'icon': '🔥'},
            {'name': 'TensorFlow / Keras', 'proficiency': 88, 'icon': '🌊'},
            {'name': 'HuggingFace', 'proficiency': 85, 'icon': '🤗'},
            {'name': 'Django', 'proficiency': 82, 'icon': '🌐'},
            {'name': 'FastAPI', 'proficiency': 78, 'icon': '⚡'},
            {'name': 'Scikit-learn', 'proficiency': 92, 'icon': '🔬'},
        ],
        'tools': [
            {'name': 'VS Code', 'proficiency': 90, 'icon': '💻'},
            {'name': 'Git / GitHub', 'proficiency': 90, 'icon': '📦'},
            {'name': 'AWS / GCP', 'proficiency': 72, 'icon': '☁️'},
            {'name': 'Jupyter / Colab', 'proficiency': 95, 'icon': '📓'},
            {'name': 'MLflow', 'proficiency': 70, 'icon': '📈'},
        ],
    }


def home(request):
    all_projects = get_projects()
    skills = get_skills()
    form = ContactForm()

    if request.method == 'POST' and 'contact_submit' in request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
            messages.success(request, "Your message has been sent! I'll get back to you soon.")
            return redirect('home')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors})

    context = {
        'projects': all_projects,
        'skills': skills,
        'form': form,
        'featured_projects': [p for p in all_projects if p['is_featured']],
    }
    return render(request, 'base/home.html', context)


def about(request):
    return render(request, 'base/about.html', {})


def projects(request):
    all_projects = get_projects()
    category = request.GET.get('category', 'all')
    filtered = [p for p in all_projects if p['category'] == category] if category != 'all' else all_projects
    return render(request, 'base/projects.html', {
        'projects': filtered,
        'all_projects': all_projects,
        'active_category': category,
    })


def skills(request):
    return render(request, 'base/skills.html', {'skills': get_skills()})


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            messages.success(request, "Message sent! I'll respond within 24 hours.")
            return redirect('contact')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors})
    return render(request, 'base/contact.html', {'form': form})
