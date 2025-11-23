# week5-image-classifier

# Computer Vision Image Classifier

## Project Overview

This project implements image classification using computer vision concepts from Chapter 24. The AI can recognize objects in images using a neural network trained with Teachable Machine.

## My Classification Task

**Classes:** Rock, Paper, Scissors
**Training Images:** 50+ images per class
**Accuracy:** ???%

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

- I can't get some dependencies to work.
- getting the training pictures was an issue in the beginning to transfer from my phone to my computer
- still dont know if it workes

## Real-World Applications

1. **Medical**: this could be effective if you have it trained on symptems for quick diagnosis
2. **Security**: this could help register people who are bared from entering an establishment
3. **Retail**: this could help register how many items someone has to stop shoplifters

## Ethical Considerations

This could be an issue because if someone can take your data they could simulate you in a computer setting. This is scarry for many reasons because you could have your ideas stolen. This is also an issue because of possible security things with people trying to be malicious.

## What I Learned

I now know how a computer sees. This is cool because I can now do something in the real world to try and make my own ai. This could be a recognission software where I have a camera on my door that tells me what guest is at my door. I also learned that the more data you have the more sure your model can be.
