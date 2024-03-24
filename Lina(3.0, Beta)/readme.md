# Lina (3.0)

## Introduction
Lina 3.0 is a text generating model designed to generate text and answer user questions. It is free to use and open source. Lina is primarily trained for mathematical purposes, ranging from simple arithmetic operations like addition and subtraction to more complex mathematical problems. Additionally, Lina serves as a coding assistant, providing support in programming tasks.

## Features
- Text generation
- Mathematical problem solving
- Coding assistance

## Launch Details
- Version: 3.0
- Launch Date: Pending (15/07/2024)

## Problems (Current Version)
- None reported

## Fixes (From Previous Version)
- None reported

## Usage
To use Lina 3.0, import the `lina_respond` function from the main file. 

Example usage:
```python
from main import lina_respond

prompt = "Hey, can you help me solve my math homework?"
response = lina_respond(prompt, 'auto', False, False)[1]
print(response)
```

The `lina_respond` function takes four parameters:
1. `prompt`: User input or query.
2. `length`: Number of words to generate ('auto' for complete sentence).
3. `verbose`: True/False, to print the generating text in terminal.
4. `continue_prompt`: True/False, to continue the previous broken prompt (recommended to be False unless using the web version).

## Source Code
The source code for Lina can be found on GitHub: https://github.com/mrlwitwma/lina/

## Show Support
Support MrLwitwma by:
- Donating to him
  - https://donate.mrlwitwma.in (Site may be down or not working sometimes)
- Subscribing/following his social media accounts:
  - YouTube: https://youtube.com/@mrlwitwma
  - Instagram: https://instagram.com/mrlwitwma
  - GitHub: https://github.com/mrlwitwma
- Using Lina online at https://lina.mrlwitwma.com. If the link is unavailable, check MrLwitwma's channel pages for details on the new site.

## License
This software is free to use. You can share the main file on GitHub with your friends. However, stealing and selling it is forbidden. Using this software and claiming it as your own is also forbidden. Strict actions will be taken against such violations. If you use this model in your videos, please make sure to mention the model and creator: Lina(3.0) by MrLwitwma [Mr(Mister), Lwitwma(Lwi-tw-ma)].

## Disclaimer
Lina does not have the ability to respond to answers based on previous texts.

## Creator's Message
It is a Small Language Model so it is mostly inaccurate. Lina's Larger and more accurate model is currently under work, I am currently gathering more data for it to feed and also it takes a lot of time to train model with a CPU. Please considering Donating or Subscribing/Following my Social Media.
