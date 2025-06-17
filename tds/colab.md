## Notebooks: Google Colab

[Google Colab](https://colab.research.google.com/) is a free, cloud-based Jupyter notebook environment that's become indispensable for data scientists and ML practitioners. It's particularly valuable because it provides free access to GPUs and TPUs, and for easy sharing of code and execution results.

While Colab is excellent for prototyping and learning, its free tier has limitations - notebooks time out after 12 hours, and GPU access can be inconsistent.

Learn how to mount Google Drive for persistent storage, manage dependencies with `!pip install` commands, as these are common pain points when getting started.

[![Get started with Google Colaboratory (3 min)](https://i.ytimg.com/vi_webp/inN8seMm7UI/sddefault.webp)](https://youtu.be/inN8seMm7UI
<youtube_summary>This video introduction to Google Colab, presented by Jake VanderPlas, explains that Colab is an executable document platform within Google Drive that allows users to write, run, and share Python code. Similar to Jupyter notebooks, Colab notebooks consist of cells containing code, text, images, and more, which execute on a cloud-based runtime without requiring local setup. Users can run code using shortcuts like Shift-Enter and generate dynamic outputs, including interactive visualizations with libraries like Altair. Text cells support Markdown formatting for creating narratives, headings, lists, and math formulas. Notebooks can be shared via Google Drive or exported to GitHub and are compatible with Jupyter environments. Jake highlights the Seedbank project as a resource for example notebooks, such as the Neural Style Transfer demo. For further learning, users can visit colab.research.google.com to access tutorials and a welcome notebook. The video series continues with a follow-up by Lawrence, covering TensorFlow installation and GPU runtime use. Jake encourages viewers to subscribe for more Colab content.</youtube_summary>
)

- [Google Colab features you may have missed](https://youtu.be/rNgswRZ2C1Y
<youtube_summary>Nate from the Colab team presents three lesser-known but powerful Colab features to enhance productivity:

1. **Interactive Table for Pandas DataFrames**: This Colab extension allows dynamic exploration of DataFrames without re-executing code cells. After enabling it via the data table module, users can sort, paginate, and filter data interactively (including regex and value bounds filtering). This speeds up the data exploration feedback loop by enabling direct manipulation and searching within displayed tables.

2. **Execution History**: Accessible via View > Executed code history, this side panel shows a linear record of all executed cells and their outputs in the current Notebook session. It helps track previous iterations of code, verify session state, and recall how results were achieved. Users can jump to past executions or create scratch cells prepopulated with previous code for quick testing without cluttering the main Notebook. Scratch cells affect session state and appear in the history but only persist while the tab is open.

3. **Command Palette**: Opened with Ctrl + Shift + P or via the Tools menu, this feature provides autocomplete access to all Colab commands and UI menu options. It enables rapid execution of tasks like restarting runtimes, viewing logs, creating scratch cells, or adjusting settings, making it easy to find and use Colab features without navigating menus.

Together, these features improve efficiency in data analysis, code iteration, and command access within Colab Notebooks.</youtube_summary>
)
- [How to mount Google Drive to Google Colab](https://youtu.be/8HvugBq5NKg
<youtube_summary>To mount Google Drive in Google Colab, expand the side menu and click on "Mount Drive." Then, click "Connect to Google Drive." Thanks for watching and subscribe for more videos.</youtube_summary>
)
- [How to take advantage of GPUs and TPUs for your ML project](https://youtu.be/tCYSce6l8gA
<youtube_summary>Paige Bailey, a Developer Advocate for TensorFlow, explains the use of specialized hardware like GPUs (Graphics Processing Units) and TPUs (Tensor Processing Units) to accelerate training of machine learning models such as Convolutional Neural Networks (CNNs) and Generative Adversarial Networks (GANs). These accelerators enable parallel processing, significantly reducing training time from days or weeks to minutes. Google Colab allows free access to GPUs and TPUs. To enable these, users select Runtime > Change Runtime Type and choose GPU or TPU.

For GPUs, Paige demonstrates installing TensorFlow 2.0 with GPU support and confirms GPU availability using a test command. Training a basic Keras model on the MNIST dataset on GPU took about 43 seconds, compared to 69 seconds on CPU, showing a substantial speed boost. Users can also check system hardware details (CPU, RAM, GPU) via specific commands in Colab.

For TPUs, Paige showcases a more complex example: training a two-layer forward LSTM model to predict Shakespearean text using Keras. The TPU runtime is selected similarly, and the model is converted to TPU format using Keras methods (fit, predict, evaluate). Although training is lengthy due to the vast Shakespeare corpus, after several epochs the model generates Shakespeare-like scripts, which improve with added layers, nodes, and TPU clusters.

Paige encourages viewers to accelerate their machine learning projects with GPUs and TPUs in Google Colab and teases an upcoming video on upgrading TensorFlow code to version 2.0. She invites users to share their TensorFlow projects on Twitter using #PoweredbyTF and subscribe to the TensorFlow YouTube channel for more updates.</youtube_summary>
)
