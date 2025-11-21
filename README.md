# week5-image-classifier

# Computer Vision Image Classifier

## Project Overview

This project implements image classification using computer vision concepts from Chapter 24. The AI can recognize objects in images using a neural network trained with Teachable Machine.

## My Classification Task

**Classes:** Rock, Paper, Scissors
**Training Images:** 50+ images per class
**Accuracy:** [Your test accuracy]%

## How to Run

1. **Install Requirements**

```bash
pip install -r requirements.txt
```

2. **Test the Classifier**

```bash
python test_classifier.py
```

3. **Web Interface**

```bash
python web_interface.py
```

Visit http://localhost:5000

## How Computer Vision Works

### Image as Numbers

Every image is a grid of pixels. Each pixel has RGB values (0-255 for Red, Green, Blue).

### Feature Detection

The neural network learns to detect:

- **Edges**: Where colors change sharply
- **Shapes**: Combinations of edges
- **Patterns**: Repeated features
- **Objects**: Complex combinations

### My Model's Process

1. Resize image to 224x224 pixels
2. Normalize pixel values
3. Pass through neural network
4. Get probability for each class
5. Return highest probability as prediction

## Challenges I Encountered

[Write 2-3 specific challenges and solutions]

## Real-World Applications

1. **Medical**: [Example]
2. **Security**: [Example]
3. **Retail**: [Example]

## Ethical Considerations

[Write 2-3 thoughts on privacy and bias in computer vision]

## What I Learned

[3-4 sentences about computer vision concepts you now understand]
